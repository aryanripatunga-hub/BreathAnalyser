
import os

import tempfile

from contextlib import asynccontextmanager

from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile

from fastapi.concurrency import run_in_threadpool

from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse

from fastapi.staticfiles import StaticFiles

from .model import load_model, predict

from .disease_data import get_all_diseases, get_disease_detail

BACKEND_DIR = Path(__file__).resolve().parent

MODEL_PATH = BACKEND_DIR / "model_best2.pth"

FRONTEND_DIR = BACKEND_DIR.parent / "frontend"

ALLOWED_TYPES = {

    "audio/wav",

    "audio/x-wav",

    "audio/wave",

    "audio/vnd.wave",

    "audio/mpeg",

    "audio/mp3",

    "audio/ogg",

    "audio/flac",

    "audio/webm",

}

MAX_FILE_SIZE = 10 * 1024 * 1024

@asynccontextmanager

async def lifespan(app: FastAPI):

    print("[*] Starting Respiratory Disease Detector API...")

    if MODEL_PATH.exists():

        load_model(MODEL_PATH)

    else:

        print(

            f"[WARNING] Model file not found at {MODEL_PATH}. "

            "The /api/predict endpoint will return errors until the model is available. "

            "Place 'model_best2.pth' in the backend/ directory."

        )

    yield

    print("[*] Shutting down API...")

app = FastAPI(

    title="Respiratory Disease Detector API",

    description=(

        "AI-powered breath sound analysis using a ResNet-18 model "

        "trained on the ICBHI 2017 dataset."

    ),

    version="1.0.0",

    lifespan=lifespan,

)

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

@app.get("/api/health")

async def health_check():

    model_loaded = MODEL_PATH.exists()

    return {

        "status": "healthy",

        "model_loaded": model_loaded,

        "version": "1.0.0",

    }

@app.post("/api/predict")

async def predict_disease(file: UploadFile = File(...)):

    content_type = file.content_type or ""

    filename = file.filename or "upload.wav"

    ext = Path(filename).suffix.lower()

    allowed_extensions = {".wav", ".mp3", ".ogg", ".flac", ".webm"}

    if content_type not in ALLOWED_TYPES and ext not in allowed_extensions:

        raise HTTPException(

            status_code=400,

            detail=(

                f"Unsupported file type: {content_type} ({ext}). "

                "Please upload a .wav, .mp3, .ogg, .flac, or .webm audio file."

            ),

        )

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:

        raise HTTPException(

            status_code=400,

            detail=f"File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)} MB.",

        )

    if len(contents) == 0:

        raise HTTPException(status_code=400, detail="Empty file uploaded.")

    tmp_dir = "/tmp" if os.path.isdir("/tmp") else None

    suffix = ext if ext else ".wav"

    try:

        with tempfile.NamedTemporaryFile(

            delete=False, suffix=suffix, dir=tmp_dir

        ) as tmp:

            tmp.write(contents)

            tmp_path = tmp.name

        result = await run_in_threadpool(predict, tmp_path)

        return JSONResponse(content=result)

    except FileNotFoundError as e:

        raise HTTPException(status_code=503, detail=str(e))

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=f"Prediction failed: {str(e)}",

        )

    finally:

        try:

            os.unlink(tmp_path)

        except (OSError, UnboundLocalError):

            pass

@app.get("/api/diseases")

async def list_diseases():

    return get_all_diseases()

@app.get("/api/diseases/{disease_id}")

async def get_disease(disease_id: str):

    disease = get_disease_detail(disease_id.lower())

    if disease is None:

        raise HTTPException(

            status_code=404,

            detail=f"Disease '{disease_id}' not found. Available: healthy, asthma, copd, pneumonia",

        )

    return disease

if FRONTEND_DIR.exists():

    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")

else:

    @app.get("/")

    async def root():

        return {

            "message": "Respiratory Disease Detector API",

            "docs": "/docs",

            "endpoints": ["/api/health", "/api/predict", "/api/diseases"],

        }

