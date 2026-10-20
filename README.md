# BreathAnalysis — Respiratory Disease Detector

BreathAnalysis is an AI-powered respiratory disease detection system that analyzes breath sound recordings using a deep learning ResNet-18 model trained on the ICBHI 2017 Respiratory Sound Database. It classifies breath recordings into four categories: **Healthy**, **Asthma**, **COPD**, or **Pneumonia**.

## Project Team
- **Aryan K Ail**
- **Ayush Khare**
- **Abhinav Racha**
- **Aditya Singh**

*R.V. College of Engineering, Bengaluru*

*This project is built for educational and research purposes only and is not a substitute for professional medical diagnosis or clinical evaluation.*

---

## Key Features
1. **Interactive Audio Input**:
   - **Upload File**: Drag and drop or browse for `.wav`, `.mp3`, `.ogg`, or `.flac` files up to 10MB.
   - **Live Microphone Recording**: Capture up to 20 seconds of breathing sound in real-time directly through the browser.
   - **Audio Playback**: Listen back to your recorded audio before submitting for analysis.
2. **AI Visualization**:
   - Dynamic audio waveform rendering.
   - Interactive donut chart showing confidence distribution across conditions.
   - Mel Spectrogram frequency rendering (revealing what the deep learning model sees).
3. **Medical Encyclopedia**:
   - Comprehensive information tabs for each condition: Definition, Symptoms, Causes, Severity Stages, Diagnosis, Treatment, Medications, and Medical References.
4. **PDF Report Generation**:
   - Downloadable diagnostic report with spectrogram visualization and confidence scores.

---

## Tech Stack
- **Backend**: FastAPI, PyTorch (ResNet-18 classification), Librosa (Audio processing & Mel Spectrogram generation), Matplotlib, Uvicorn.
- **Frontend**: HTML5, Vanilla CSS3 (modern glassmorphic design system), Vanilla JS, Chart.js.
- **Model**: ResNet-18 fine-tuned on the ICBHI 2017 Respiratory Sound Database.

---

## How to Run Locally

### Prerequisites
- Python 3.10+ installed on your system.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/respiratory-disease-detector.git
   cd respiratory-disease-detector
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # Linux / macOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Ensure the trained model weights file `model_best2.pth` is placed in the `backend/` directory.

5. Start the server:
   ```bash
   python -m uvicorn backend.main:app --reload
   ```

6. Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Project Structure
```text
respiratory-disease-detector/
│
├── backend/
│   ├── __init__.py
│   ├── disease_data.py       # Disease encyclopedia data
│   ├── main.py               # FastAPI application setup and API endpoints
│   ├── model.py              # PyTorch inference, spectrogram & waveform logic
│   ├── model_best2.pth       # Fine-tuned ResNet-18 model weights (44.8 MB)
│   └── requirements.txt      # Python dependencies
│
├── frontend/
│   ├── app.js                # Core JS logic (file upload, mic capture, charts)
│   ├── index.css             # Glassmorphic responsive dark theme CSS
│   └── index.html            # SPA template (main UI, modal)
│
└── .vscode/
    └── launch.json           # VS Code Run/Debug profile
```

## Model Architecture

The classification pipeline uses a **ResNet-18** convolutional neural network:

1. Audio is loaded at 22,050 Hz sample rate and converted to a **128-band Mel Spectrogram**.
2. The spectrogram is resized to **224×224** pixels and normalized (z-score standardization).
3. The single-channel spectrogram is replicated to 3 channels (matching ResNet's expected RGB input).
4. The final fully-connected layer is replaced with a 4-class output layer (Healthy, Asthma, COPD, Pneumonia).
5. Softmax probabilities determine the predicted class and confidence scores.

Training was performed on the **ICBHI 2017 Respiratory Sound Database**, a widely-used benchmark dataset for lung sound classification research.
