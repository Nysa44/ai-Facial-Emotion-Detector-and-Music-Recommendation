from flask import Flask,render_template,request,jsonify
from src.predictor import EmotionPredictor
from src.recommender import recommend

app=Flask(__name__)
predictor=None

def get_predictor():
    global predictor
    if predictor is None: predictor=EmotionPredictor()
    return predictor

@app.get("/")
def home(): return render_template("index.html")

@app.get("/api/health")
def health():
    try:
        get_predictor()
        return jsonify({"status":"healthy","model":"loaded"})
    except Exception as e:
        return jsonify({"status":"error","error":str(e)}),503

@app.post("/api/predict")
def predict():
    if "image" not in request.files:
        return jsonify({"error":"Upload an image using the image field."}),400
    try:
        result=get_predictor().predict(request.files["image"].read())
        result["recommendations"]=recommend(result["expression"])
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error":str(e)}),400
    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
