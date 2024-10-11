from fastapi import APIRouter, UploadFile, File
from app.models.image_recognition import ImageRecognitionModel
from app.models.outfit_recommendation import OutfitRecommendationModel
from typing import List
import aiofiles
import os

router = APIRouter()
image_model = ImageRecognitionModel()
outfit_model = OutfitRecommendationModel()

@router.post("/recognize")
async def recognize_image(file: UploadFile = File(...)):
    UPLOAD_DIR = "uploads"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    predictions = image_model.predict(file_path)
    os.remove(file_path)
    
    return {"predictions": predictions}

@router.post("/recommend")
async def recommend_outfit(wardrobe_items: List[dict]):
    outfit = outfit_model.recommend(wardrobe_items)
    return {"recommended_outfit": outfit}