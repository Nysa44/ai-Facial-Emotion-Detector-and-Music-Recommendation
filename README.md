# AI Facial Expression & Music Recommendation Platform

A production-style computer vision application that analyzes a face in an uploaded image, predicts a facial-expression category with a trained CNN, displays confidence probabilities, and recommends music based on the predicted expression.

## Features
- Trained CNN model (`emotion_model.h5`) loaded from the original project
- OpenCV face detection
- Seven facial-expression classes
- Confidence/probability visualization
- Image upload workflow
- Music recommendation engine
- REST API
- Responsive dashboard UI
- Input validation and error handling
- Docker support
- Health endpoint

## Expression classes
Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral.

## Run
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

If `models/emotion_model.h5` is not present, the application downloads the trained model from the original public repository automatically on first start.

Open http://127.0.0.1:5000.

## API
`POST /api/predict` with multipart field `image`.

`GET /api/health` returns model status.

## Note
This project predicts visible facial-expression patterns. It does not claim to determine a person's internal emotional state.
