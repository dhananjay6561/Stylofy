from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.security import create_access_token, verify_password
from app.core.config import settings
from app.db.mongodb import database
from app.models.user import UserInDB, UserOut

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await database["users"].find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserOut)
async def register(user: UserInDB):
    existing_user = await database["users"].find_one({"username": user.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    user_dict = user.dict()
    user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
    new_user = await database["users"].insert_one(user_dict)
    created_user = await database["users"].find_one({"_id": new_user.inserted_id})
    return UserOut(**created_user)