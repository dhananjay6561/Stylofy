from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from typing import List
from app.db.mongodb import database
from app.models.wardrobe_item import WardrobeItemModel, WardrobeItemOut
from app.core.security import get_current_user
from app.models.user import UserOut
import aiofiles
import os

router = APIRouter()

@router.post("/items", response_model=WardrobeItemOut)
async def create_wardrobe_item(item: WardrobeItemModel, current_user: UserOut = Depends(get_current_user)):
    item_dict = item.dict()
    item_dict["user_id"] = current_user.id
    new_item = await database["wardrobe_items"].insert_one(item_dict)
    created_item = await database["wardrobe_items"].find_one({"_id": new_item.inserted_id})
    return WardrobeItemOut(**created_item)

@router.get("/items", response_model=List[WardrobeItemOut])
async def read_wardrobe_items(current_user: UserOut = Depends(get_current_user)):
    items = await database["wardrobe_items"].find({"user_id": current_user.id}).to_list(1000)
    return [WardrobeItemOut(**item) for item in items]

@router.post("/upload")
async def upload_image(file: UploadFile = File(...), current_user: UserOut = Depends(get_current_user)):
    UPLOAD_DIR = "uploads"
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(UPLOAD_DIR, f"{current_user.id}_{file.filename}")
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    
    return {"filename": file.filename, "file_path": file_path}