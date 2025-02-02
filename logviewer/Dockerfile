# Stage 1: Base
FROM python:3.10-slim AS base
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Stage 2: Development
FROM base AS development
EXPOSE 9000
CMD ["uvicorn", "live_log_service:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]

# (Optionnel) Vous pouvez ajouter un stage production si besoin.
