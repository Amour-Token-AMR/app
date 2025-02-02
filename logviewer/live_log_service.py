# logviewer/live_log_service.py
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI(title="Service de suivi des logs en live (Dev)")

async def tail_log(file_path: str):
    """
    Générateur asynchrone qui lit en continu le fichier de log et émet chaque nouvelle ligne via SSE.
    """
    try:
        with open(file_path, "r") as log_file:
            # Se positionner à la fin du fichier pour ne récupérer que les nouvelles lignes
            log_file.seek(0, 2)
            while True:
                line = log_file.readline()
                if line:
                    # Le préfixe "data:" est nécessaire pour le format SSE, suivi de deux sauts de ligne.
                    yield f"data: {line}\n\n"
                else:
                    # Attendre un court instant avant de relire (pour éviter une boucle trop rapide)
                    await asyncio.sleep(0.1)
    except FileNotFoundError:
        # Si le fichier n'existe pas, attendre et réessayer (utile en développement)
        while True:
            yield "data: [Erreur] Fichier de log introuvable...\n\n"
            await asyncio.sleep(5)

@app.get("/logs")
async def get_logs():
    """
    Endpoint qui retourne un StreamingResponse contenant le flux de logs.
    Le client doit être compatible SSE (ex: un navigateur ou une application dédiée).
    """
    # Remplacez "app.log" par le chemin de votre fichier de log.
    log_file_path = "app.log"
    return StreamingResponse(tail_log(log_file_path), media_type="text/event-stream")
