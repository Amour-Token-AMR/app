# ai-model/Dockerfile
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances et installer les packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port 8500
EXPOSE 8500

# Démarrer l'application avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8500"]
