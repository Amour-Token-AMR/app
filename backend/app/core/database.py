# backend/app/core/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DB_URI", "postgresql://user:password@db:5432/amr_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Fournit une session de base de données pour les endpoints.
    À utiliser avec FastAPI via Depends().
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
