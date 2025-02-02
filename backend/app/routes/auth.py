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
    Authentifie l'utilisateur et retourne un token JWT en cas de succès.
    (Exemple simplifié – à adapter pour utiliser une vraie base d'utilisateurs)
    """
    dummy_username = "testuser"
    # Pour la démonstration, le mot de passe haché est codé en dur.
    dummy_password_hash = "$2b$12$KIXQm0Z3kfrpNUv9YpXl2O1hX/UV8zCMy/fKq0.lDnKz8p0DzjHni"  # bcrypt('password')
    
    if data.username != dummy_username or not verify_password(data.password, dummy_password_hash):
        raise HTTPException(status_code=401, detail="Identifiants invalides")
    
    token = create_access_token({"sub": data.username})
    return {"access_token": token, "token_type": "bearer"}
