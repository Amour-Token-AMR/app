# ========================================
# Stage 1: Builder
# ========================================
FROM python:3.10-slim AS builder

WORKDIR /app

# Supprimer le fichier en double (s'il existe)
RUN rm -f /etc/apt/sources.list.d/debian.sources

# Créer ou réécrire /etc/apt/sources.list avec les sources Bookworm en HTTPS
RUN echo "deb https://deb.debian.org/debian bookworm main" > /etc/apt/sources.list && \
    echo "deb https://deb.debian.org/debian bookworm-updates main" >> /etc/apt/sources.list && \
    echo "deb https://deb.debian.org/debian-security bookworm-security main" >> /etc/apt/sources.list

# Mettre à jour apt avec l'option --allow-releaseinfo-change et installer les dépendances système
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends debian-archive-keyring ca-certificates gnupg gcc libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Créer un environnement virtuel et mettre à jour le PATH
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copier requirements.txt et installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip==23.2.1 && \
    pip install --no-cache-dir -r requirements.txt

# Copier l'intégralité du code source dans le stage builder
COPY . .

# ========================================
# Stage 2: Production
# ========================================
FROM builder AS production

# Création d'un utilisateur non-root pour la sécurité
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    chown -R appuser:appuser /app /opt/venv
USER appuser

# Définir le HOME de l'utilisateur et créer le répertoire de cache pip
ENV HOME=/home/appuser
RUN mkdir -p /home/appuser/.cache/pip && chown -R appuser:appuser /home/appuser/.cache

# Variables d'environnement essentielles
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

# Vérifier l'état de l'application via /health
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8000/health || exit 1

ENV WEB_CONCURRENCY=4
CMD ["/bin/sh", "-c", "gunicorn --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers ${WEB_CONCURRENCY:-4} app.main:app"]

# ========================================
# Stage 3: Development
# ========================================
FROM builder AS development

# Définir des variables pour le mode développement
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Créer un utilisateur non-root pour le développement en créant son répertoire HOME (-m)
RUN groupadd -r appuser && useradd -r -m -g appuser appuser && \
    chown -R appuser:appuser /app /opt/venv

# Définir le HOME de l'utilisateur (créé par -m, normalement /home/appuser)
ENV HOME=/home/appuser

# Passer à l'utilisateur non-root
USER appuser

# Créer le répertoire de cache pip
RUN mkdir -p "$HOME/.cache/pip" && chown -R appuser:appuser "$HOME/.cache"

# Exposer le port 8000 et lancer l'application en mode développement (hot-reload)
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

