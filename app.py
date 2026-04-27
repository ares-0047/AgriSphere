from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app) # This allows your local HTML files to ping this server safely

# --- API ENDPOINT 1: Crop Prediction ---
@app.route('/api/predict_crop', methods=['POST'])
def predict_crop():
    data = request.json
    
    # Extract values sent from frontend
    n = float(data.get('nitrogen', 0))
    p = float(data.get('phosphorus', 0))
    k = float(data.get('potassium', 0))
    ph = float(data.get('ph', 7.0))
    
    time.sleep(1.5) # Simulate heavy ML model processing time
    
    # 🧠 Faux-ML Logic (Replace with real model.predict() if you have one)
    if n > 80 and ph < 7.0:
        prediction = "Cotton"
    elif n < 40 and p > 40:
        prediction = "Soybean"
    elif ph > 7.5:
        prediction = "Barley"
    else:
        prediction = "Wheat (Sharbati)"

    return jsonify({
        "status": "success",
        "model": "RandomForest_v2.1",
        "recommended_crop": prediction,
        "confidence": round(random.uniform(88.5, 99.1), 2)
    })

# --- API ENDPOINT 2: Disease Computer Vision ---
@app.route('/api/diagnose_disease', methods=['POST'])
def diagnose_disease():
    # Check if an image file was actually sent
    if 'image' not in request.files:
        return jsonify({"error": "No image data received"}), 400
    
    image_file = request.files['image']
    
    time.sleep(2) # Simulate computer vision processing/matrix multiplication
    
    # 🧠 Faux-CNN Logic (Replace with TensorFlow/Keras model if you have one)
    # image_data = image_file.read() -> pass to model...
    
    return jsonify({
        "status": "success",
        "model": "ResNet50_Agri",
        "disease": "Early Blight",
        "severity": "MODERATE",
        "treatment": "Apply copper-based fungicide (Mancozeb 75% WP) at 2g/liter of water.",
        "prevention": "Ensure proper crop rotation and avoid overhead irrigation.",
        "confidence": round(random.uniform(92.0, 98.7), 2)
    })

if __name__ == '__main__':
    print("🚀 AgriSphere AI Microservice is running on port 5000...")
    app.run(debug=True, port=5000)