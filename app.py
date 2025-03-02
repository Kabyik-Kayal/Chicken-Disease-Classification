import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from Chicken_disease_classifier.utils.common import decodeImage
from Chicken_disease_classifier.pipeline.predict import PredictionPipeline
from Chicken_disease_classifier.utils.logger import logger

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    try:
        os.system("python main.py")
        return "Training done successfully!"
    except Exception as e:
        logger.error(f"Error during training: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        logger.info("Prediction request received")
        image = request.json['image']
        logger.info("Decoding image")
        decodeImage(image, clApp.filename)
        logger.info("Image decoded. Starting prediction")
        result = clApp.classifier.predict()
        logger.info(f"Prediction result: {result}")
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    clApp = ClientApp()
    logger.info("Starting application")
    app.run(host='0.0.0.0', port=5000, debug=False)