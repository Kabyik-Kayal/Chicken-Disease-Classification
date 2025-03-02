import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import logging
import traceback
import time

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('prediction')

    def predict(self):
        try:
            self.logger.info(f"Starting prediction for {self.filename}")
            start_time = time.time()
            
            # Check if the file exists
            if not os.path.exists(self.filename):
                self.logger.error(f"Image file not found: {self.filename}")
                return [{"error": "Image file not found"}]
                
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
            model_path = os.path.join(BASE_DIR, "artifacts", "training", "model.h5")
            
            if not os.path.exists(model_path):
                self.logger.error(f"Model file not found: {model_path}")
                return [{"error": "Model not found"}]
            
            self.logger.info(f"Loading model from {model_path}")
            model = load_model(model_path)
            self.logger.info("Model loaded successfully")
            
            imagename = self.filename
            self.logger.info(f"Processing image: {imagename}")
            test_image = image.load_img(imagename, target_size = (224,224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            
            self.logger.info("Running prediction")
            result = np.argmax(model.predict(test_image), axis=1)
            self.logger.info(f"Raw prediction result: {result}")
            
            prediction = 'Healthy' if result[0] == 1 else 'Coccidiosis'
            self.logger.info(f"Prediction: {prediction}")
            self.logger.info(f"Prediction completed in {time.time() - start_time:.2f} seconds")
            
            return [{"image": prediction}]
            
        except Exception as e:
            self.logger.error(f"Error in prediction: {str(e)}")
            self.logger.error(traceback.format_exc())
            return [{"error": str(e)}]