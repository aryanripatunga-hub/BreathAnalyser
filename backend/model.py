import io

import base64

import numpy as np

import torch

import torch.nn as nn

import librosa

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from torchvision import models

from pathlib import Path

CLASS_NAMES = ["Healthy", "Asthma", "COPD", "Pneumonia"]

SAMPLE_RATE = 22050

MAX_DURATION = 20

N_MELS = 128

TARGET_SIZE = 224

_model = None

_device = None

def get_device() -> str:

    if torch.cuda.is_available():

        return "cuda"

    return "cpu"

def load_model(model_path: str | Path) -> nn.Module:

    global _model, _device

    _device = get_device()

    model_path = Path(model_path)

    if not model_path.exists():

        raise FileNotFoundError(

            f"Model weights not found at {model_path}. "

            "Please place 'model_best2.pth' in the backend/ directory."

        )

    model = models.resnet18(weights=None)

    model.fc = nn.Linear(512, len(CLASS_NAMES))

    model.load_state_dict(

        torch.load(str(model_path), map_location=_device, weights_only=True)

    )

    model = model.to(_device)

    model.eval()

    _model = model

    print(f"[OK] Model loaded successfully on {_device}")

    return model

def get_model() -> nn.Module:

    if _model is None:

        raise RuntimeError("Model not loaded. Call load_model() first.")

    return _model

def _load_audio(audio_path: str | Path) -> tuple[np.ndarray, int]:

    audio, sr = librosa.load(str(audio_path), sr=SAMPLE_RATE, duration=MAX_DURATION)

    return audio, sr

def _audio_to_mel_tensor(audio: np.ndarray, sr: int) -> torch.Tensor:

    mel = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=N_MELS)

    mel_db = librosa.power_to_db(mel, ref=np.max)

    mel_db = np.resize(mel_db, (TARGET_SIZE, TARGET_SIZE))

    tensor = torch.tensor(mel_db, dtype=torch.float32)

    tensor = tensor.unsqueeze(0).repeat(3, 1, 1)

    tensor = (tensor - tensor.mean()) / (tensor.std() + 1e-6)

    tensor = tensor.unsqueeze(0)

    return tensor

def generate_spectrogram_base64(audio: np.ndarray, sr: int) -> str:

    fig, ax = plt.subplots(figsize=(8, 3), dpi=120)

    fig.patch.set_facecolor("#0f172a")

    ax.set_facecolor("#0f172a")

    mel = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=N_MELS)

    mel_db = librosa.power_to_db(mel, ref=np.max)

    img = librosa.display.specshow(

        mel_db, sr=sr, x_axis="time", y_axis="mel", ax=ax, cmap="magma"

    )

    cbar = fig.colorbar(img, ax=ax, format="%+2.0f dB")

    cbar.ax.yaxis.set_tick_params(color="white")

    cbar.outline.set_edgecolor("white")

    plt.setp(cbar.ax.yaxis.get_ticklabels(), color="white")

    ax.set_title("Mel Spectrogram", color="white", fontsize=11)

    ax.tick_params(colors="white")

    ax.xaxis.label.set_color("white")

    ax.yaxis.label.set_color("white")

    for spine in ax.spines.values():

        spine.set_edgecolor("#334155")

    plt.tight_layout()

    buf = io.BytesIO()

    fig.savefig(buf, format="png", bbox_inches="tight",

                facecolor=fig.get_facecolor(), edgecolor="none")

    plt.close(fig)

    buf.seek(0)

    return base64.b64encode(buf.read()).decode("utf-8")

def generate_waveform_data(

    audio: np.ndarray, sr: int, num_points: int = 200

) -> list[float]:

    if len(audio) == 0:

        return [0.0] * num_points

    chunk_size = max(1, len(audio) // num_points)

    downsampled = []

    for i in range(0, len(audio), chunk_size):

        chunk = audio[i : i + chunk_size]

        rms = float(np.sqrt(np.mean(chunk ** 2)))

        downsampled.append(round(rms, 4))

    downsampled = downsampled[:num_points]

    while len(downsampled) < num_points:

        downsampled.append(0.0)

    max_val = max(downsampled) if max(downsampled) > 0 else 1.0

    downsampled = [round(v / max_val, 4) for v in downsampled]

    return downsampled

def predict(audio_path: str | Path) -> dict:

    model = get_model()

    device = _device

    descriptions = {

        "Healthy": (

            "No abnormal breath sounds detected. Breathing patterns appear normal. "

            "Regular check-ups are still recommended to maintain respiratory health."

        ),

        "Asthma": (

            "Possible wheezing detected in the airways, consistent with asthma patterns. "

            "Wheezing is caused by narrowed airways due to inflammation. "

            "Please consult a pulmonologist for proper diagnosis and management."

        ),

        "COPD": (

            "Crackling or obstructive sounds detected, consistent with Chronic Obstructive "

            "Pulmonary Disease patterns. COPD involves progressive airflow limitation. "

            "Please consult a doctor for spirometry testing and treatment options."

        ),

        "Pneumonia": (

            "Abnormal fluid-like sounds detected in the lungs, consistent with pneumonia. "

            "This suggests possible infection causing inflammation and fluid buildup in the air sacs. "

            "Please seek medical attention promptly for diagnosis and antibiotic treatment."

        ),

    }

    audio, sr = _load_audio(audio_path)

    duration = round(len(audio) / sr, 2)

    spectrogram_b64 = generate_spectrogram_base64(audio, sr)

    waveform = generate_waveform_data(audio, sr)

    tensor = _audio_to_mel_tensor(audio, sr).to(device)

    with torch.no_grad():

        logits = model(tensor)

        probs = torch.softmax(logits, dim=1)[0].cpu().numpy()

    confidences = {

        CLASS_NAMES[i]: round(float(probs[i]) * 100, 2)

        for i in range(len(CLASS_NAMES))

    }

    top_idx = int(probs.argmax())

    top_class = CLASS_NAMES[top_idx]

    top_confidence = round(float(probs[top_idx]) * 100, 1)

    return {

        "confidences": confidences,

        "top_class": top_class,

        "top_confidence": top_confidence,

        "description": descriptions[top_class],

        "spectrogram": spectrogram_b64,

        "waveform": waveform,

        "duration": duration,

    }

