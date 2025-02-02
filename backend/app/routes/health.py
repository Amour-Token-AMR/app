# backend/app/routes/health.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Vérifie que l'API est opérationnelle.
    """
    return {"status": "ok"}
