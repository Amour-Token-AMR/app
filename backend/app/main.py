# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, auth, ico, blockchain

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logger.info("Application démarrée et prête à recevoir des requêtes.")

app = FastAPI(
    title="AMR Backend API",
    description="API pour le projet $AMR - Amour Token",
    version="1.0.0"
)

# Middleware CORS (à affiner en production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre selon les besoins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes avec préfixe commun
app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(ico.router, prefix="/api/v1")
app.include_router(blockchain.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
