# -----------------------------
# Builder Stage: install system dependencies, create venv, install Python packages, copy source code
FROM python:3.10-slim AS builder

WORKDIR /app

# Installer les dépendances système
RUN apt-get update \
  && apt-get install -y --no-install-recommends debian-archive-keyring \
  && apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev curl \
  && rm -rf /var/lib/apt/lists/*

# Créer un environnement virtuel et mettre à jour le PATH
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copier le fichier des dépendances et installer les packages Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip==23.2.1 \
    && pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application dans le stage builder
COPY . .

# -----------------------------
# Production Stage
FROM builder AS production

# Création d'un utilisateur non-root pour la sécurité
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    chown -R appuser:appuser /app && \
    chown -R appuser:appuser /opt/venv
USER appuser

# Définir quelques variables d'environnement pour améliorer la lisibilité et la fiabilité
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Exposer le port 8000
EXPOSE 8000

# Définir une vérification de santé (vérifie l'endpoint /health)
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8000/health || exit 1

# Utiliser une commande shell pour permettre l'expansion de la variable WEB_CONCURRENCY
# WEB_CONCURRENCY peut être défini via l'environnement; sinon, la valeur par défaut 4 est utilisée
ENV WEB_CONCURRENCY=4
CMD ["/bin/sh", "-c", "gunicorn --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers ${WEB_CONCURRENCY:-4} app.main:app"]

# -----------------------------
# Development Stage
FROM builder AS development

# Définir des variables pour le mode développement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Création d'un utilisateur non-root pour le développement également
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    chown -R appuser:appuser /app && \
    chown -R appuser:appuser /opt/venv
USER appuser

# Exposer le port 8000
EXPOSE 8000

# Lancer Uvicorn avec l'option --reload pour activer le hot-reload en développement
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
