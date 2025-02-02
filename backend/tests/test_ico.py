# backend/tests/test_ico.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ico_participation():
    payload = {
        "walletAddress": "0xTestWalletAddress",
        "amount": 0.1
    }
    response = client.post("/api/v1/ico/participate", json=payload)
    # On vérifie que la réponse retourne une transaction (pour l'exemple, on vérifie qu'il y a une clé 'transactionId')
    assert response.status_code == 200
    data = response.json()
    assert "transactionId" in data
