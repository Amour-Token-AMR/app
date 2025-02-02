# backend/app/routes/ico.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.blockchain_service import buy_tokens
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["ICO"])

class ICOParticipation(BaseModel):
    walletAddress: str
    amount: float  # Montant en ETH

@router.post("/ico/participate")
async def participate_ico(participation: ICOParticipation, db: Session = Depends(get_db)):
    """
    Permet à un utilisateur de participer à l'ICO.
    - Enregistre la participation en base (optionnel).
    - Appelle le smart contract pour acheter des tokens.
    Retourne l'identifiant de la transaction blockchain.
    """
    try:
        tx_hash = buy_tokens(participation.walletAddress, participation.amount)
        # Ici, vous pouvez enregistrer la participation dans la DB via le session 'db'
        return {"transactionId": tx_hash}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


import requests

def trigger_n8n_workflow(payload: dict):
    n8n_url = "http://n8n:5678/webhook/ico-participation"
    headers = {"Content-Type": "application/json"}
    response = requests.post(n8n_url, json=payload, headers=headers)
    return response.status_code
