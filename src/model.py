import os, requests
from tensorflow.keras.models import load_model

MODEL_PATH="models/emotion_model.h5"
MODEL_URL="https://raw.githubusercontent.com/Nysa44/Picture-Based-Emotion-Detector/main/emotion_model.h5"

def ensure_model():
    os.makedirs("models",exist_ok=True)
    if not os.path.exists(MODEL_PATH):
        print("Downloading trained emotion model...")
        r=requests.get(MODEL_URL,timeout=180)
        r.raise_for_status()
        with open(MODEL_PATH,"wb") as f:f.write(r.content)
    return load_model(MODEL_PATH)
