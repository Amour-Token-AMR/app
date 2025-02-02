# logviewer/Dockerfile
FROM python:3.10-slim AS base

WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application (ici, notre service de logs)
COPY . .

EXPOSE 9000

CMD ["uvicorn", "live_log_service:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
