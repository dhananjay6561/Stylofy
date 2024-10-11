from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.DATABASE_NAME]

async def connect_to_mongo():
    try:
        await client.server_info()
        print("Connected to MongoDB")
    except Exception:
        print("Unable to connect to MongoDB")

async def close_mongo_connection():
    client.close()
    print("MongoDB connection closed")