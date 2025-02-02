# backend/app/routes/auth.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import create_access_token, verify_password

router = APIRouter(tags=["Auth"])

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/auth/login")
async def login(data: LoginData):
    """
    Authentifie l'utilisateur et retourne un token JWT.
    (Exemple simplifié, remplacez par une vraie recherche dans votre DB)
    """
    # Exemple d'utilisateur fictif
    dummy_username = "testuser"
    dummy_password_hash = "$2b$12$KIXQm0Z3kfrpNUv9YpXl2O1hX/UV8zCMy/fKq0.lDnKz8p0DzjHni"  # hash de 'password'
    
    if data.username != dummy_username or not verify_password(data.password, dummy_password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": data.username})
    return {"access_token": token, "token_type": "bearer"}
