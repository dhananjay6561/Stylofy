from fastapi import APIRouter, Depends, HTTPException, status
from app.db.mongodb import database
from app.models.user import UserOut
from app.core.security import get_current_user

router = APIRouter()

@router.get("/me", response_model=UserOut)
async def read_users_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserOut)
async def update_user(user_update: UserUpdate, current_user: UserOut = Depends(get_current_user)):
    update_data = user_update.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    
    await database["users"].update_one({"_id": current_user.id}, {"$set": update_data})
    updated_user = await database["users"].find_one({"_id": current_user.id})
    return UserOut(**updated_user)