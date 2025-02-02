# Image de base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système si nécessaire
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copier le fichier de dépendances et installer les packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le reste de l’application
COPY . .

# Exposer le port utilisé par Uvicorn (par défaut 8000)
EXPOSE 8000

# Lancer l’application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

