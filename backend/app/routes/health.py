# backend/app/routes/health.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint de vérification de l'état du service.
    Retourne 'ok' si l'API est opérationnelle.
    """
    return {"status": "ok"}
