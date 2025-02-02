# backend/app/config.py
import os

class Settings:
    JWT_SECRET: str = os.getenv("JWT_SECRET", "MaSuperCleSecrete")
    DB_URI: str = os.getenv("DB_URI", "postgresql://user:password@db:5432/amr_db")
    REDIS_URI: str = os.getenv("REDIS_URI", "redis://redis:6379/0")

settings = Settings()
