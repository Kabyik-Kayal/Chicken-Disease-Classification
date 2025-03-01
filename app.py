import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from Chicken_disease_classifier.utils.common import decodeImage
from Chicken_disease_classifier.pipeline.predict import PredictionPipeline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)  # Simplify CORS setup

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['POST'])
@cross_origin()
def trainRoute():
    os.system("dvc repro")
    return "Training Completed!!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        if request.is_json:
            image = request.json.get('image')
            if not image:
                return jsonify({"error": "No image data provided"})
        else:
            return jsonify({"error": "Request must be JSON"})
            
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        print(f"Prediction error: {str(e)}")  # Add logging
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=5000, debug=False)