import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

class ImageRecognitionModel:
    def __init__(self):
        self.model = MobileNetV2(weights='imagenet')

    def predict(self, image_path):
        image = Image.open(image_path).resize((224, 224))
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        predictions = self.model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        return [
            {"label": label, "confidence": float(confidence)}
            for _, label, confidence in decoded_predictions
        ]