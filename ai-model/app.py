# ai-model/app.py
import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Ollama AI Model Service",
    description="Service wrapping Ollama for $AMR Token AI inferences",
    version="1.0"
)

# Schéma d'entrée pour l'inférence
class InferenceInput(BaseModel):
    userId: str
    prompt: str  # Le prompt à envoyer au modèle

# Récupération des paramètres Ollama depuis les variables d'environnement
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/run")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "default-model")

@app.post("/infer")
def infer(input: InferenceInput):
    """
    Endpoint d'inférence.
    Il envoie le prompt à Ollama et renvoie la réponse du modèle.
    """
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": input.prompt
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        # On suppose que la réponse d'Ollama comporte un champ "output"
        return {
            "result": "approved",         # Vous pouvez adapter cette logique
            "confidence": 0.95,             # Valeur fictive pour l'exemple
            "message": data.get("output", "No output provided by Ollama")
        }
    except requests.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
