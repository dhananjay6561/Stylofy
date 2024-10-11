from fastapi import FastAPI
from app.api import auth, users, wardrobe, outfits
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection

app = FastAPI(title=settings.PROJECT_NAME)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(wardrobe.router, prefix="/wardrobe", tags=["wardrobe"])
app.include_router(outfits.router, prefix="/outfits", tags=["outfits"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Virtual Stylist API"}