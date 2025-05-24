from pydantic_settings import BaseSettings
from typing import Optional
import secrets
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "FASTAPI-Tasks"
    
    # API
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    SQLALCHEMY_DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "sqlite:///./fastapi-tasks.db"
    )
    
    # Redis
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    
    # CORS
    BACKEND_CORS_ORIGINS: list = [
        origin.strip()
        for origin in os.getenv("BACKEND_CORS_ORIGINS", "*").split(",")
    ]
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 