import cv2,numpy as np
from .model import ensure_model

CLASSES=["angry","disgust","fear","happy","sad","surprise","neutral"]

class EmotionPredictor:
    def __init__(self):
        self.model=ensure_model()
        self.detector=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

    def predict(self, image_bytes):
        image=cv2.imdecode(np.frombuffer(image_bytes,np.uint8),cv2.IMREAD_COLOR)
        if image is None: raise ValueError("Invalid image.")
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces=self.detector.detectMultiScale(gray,1.15,5)
        if len(faces)==0: raise ValueError("No face detected. Please upload a clear portrait.")
        x,y,w,h=max(faces,key=lambda z:z[2]*z[3])
        face=cv2.resize(gray[y:y+h,x:x+w],(48,48)).astype("float32")/255.0
        # Original model expects a 48x48 grayscale image.
        tensor=face.reshape(1,48,48,1)
        probs=self.model.predict(tensor,verbose=0)[0]
        # Handle models whose class order follows the common FER-2013 convention.
        if len(probs)!=len(CLASSES):
            raise RuntimeError(f"Model returned {len(probs)} classes; expected {len(CLASSES)}.")
        i=int(np.argmax(probs))
        return {
            "expression":CLASSES[i],
            "confidence":float(probs[i]),
            "probabilities":{c:float(v) for c,v in zip(CLASSES,probs)},
            "face_box":{"x":int(x),"y":int(y),"width":int(w),"height":int(h)}
        }
