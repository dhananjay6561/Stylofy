from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Virtual Stylist"
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "virtual_stylist"
    SECRET_KEY: str = "your-secret-key"  # Change this in production!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()