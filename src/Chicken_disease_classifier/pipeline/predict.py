import numpy as np
import os
import logging
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Setup basic logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def predict(self):
        try:
            # Check if file exists
            if not os.path.exists(self.filename):
                logging.error(f"File not found: {self.filename}")
                return [{"error": "File not found"}]
            
            # Check if model exists
            model_path = os.path.join("artifacts", "training", "model.h5")
            if not os.path.exists(model_path):
                logging.error(f"Model not found at {model_path}")
                return [{"error": "Model not found"}]
            
            # Load model
            model = load_model(model_path)
            
            # Load and preprocess image
            try:
                test_image = image.load_img(self.filename, target_size=(224, 224))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis=0)
                
                # Make prediction
                result = model.predict(test_image)
                prediction_idx = np.argmax(result, axis=1)
                
                # Generate response
                if prediction_idx[0] == 1:
                    prediction = 'Healthy'
                else:
                    prediction = 'Coccidiosis'
                
                logging.info(f"Prediction completed successfully: {prediction}")
                return [{"image": prediction}]
                
            except Exception as e:
                logging.error(f"Error processing image: {str(e)}")
                return [{"error": f"Image processing error: {str(e)}"}]
                
        except Exception as e:
            logging.error(f"Prediction error: {str(e)}")
            return [{"error": f"Prediction failed: {str(e)}"}]