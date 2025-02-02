# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, auth, ico, blockchain
from app.core.database import engine, Base
import logging

# Création de l'instance FastAPI
app = FastAPI(
    title="$AMR Backend API",
    description="API for $AMR - Amour Token project",
    version="1.0.0"
)

# Configuration CORS (à adapter en production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Création des tables dans la base de données (si elles n'existent pas déjà)
Base.metadata.create_all(bind=engine)

# Inclusion des routeurs
app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(ico.router, prefix="/api/v1")
app.include_router(blockchain.router, prefix="/api/v1")

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logger.info("Backend API started and ready to receive requests.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
