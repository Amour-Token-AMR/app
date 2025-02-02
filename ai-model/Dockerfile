# ai-model/Dockerfile

#################################
# Stage 1: Base
#################################
FROM python:3.10-slim AS base

WORKDIR /app

# Installer les dépendances système minimales (ici gcc est utile pour compiler certaines dépendances Python)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier des dépendances et installer les packages Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

#################################
# Stage 2: Production
#################################
FROM base AS production

# Créer et utiliser un utilisateur non-root pour des raisons de sécurité
RUN groupadd -r appuser && useradd -r -g appuser appuser \
    && chown -R appuser:appuser /app
USER appuser

# Optionnel : définir des variables d'environnement spécifiques à la production
ENV MODEL_ENV=production

# Exposer le port 8500 et lancer l'application sans rechargement automatique
EXPOSE 8500
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8500"]

#################################
# Stage 3: Development
#################################
FROM base AS development

# Créer et utiliser un utilisateur non-root pour le développement
RUN groupadd -r appuser && useradd -r -g appuser appuser \
    && chown -R appuser:appuser /app
USER appuser

# Définir des variables d'environnement spécifiques au développement
ENV MODEL_ENV=development

# Exposer le port 8500 et lancer l'application avec reload pour faciliter l'itération
EXPOSE 8500
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8500", "--reload"]
