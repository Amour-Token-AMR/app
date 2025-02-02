#!/bin/bash
# Ce script crée la structure du projet backend pour l'application FastAPI

# Création des dossiers
mkdir -p backend/app/routes
mkdir -p backend/app/models
mkdir -p backend/app/schemas
mkdir -p backend/app/services
mkdir -p backend/app/core
mkdir -p backend/tests

# Création des fichiers vides
touch backend/app/main.py
touch backend/app/config.py

touch backend/app/routes/health.py
touch backend/app/routes/auth.py
touch backend/app/routes/ico.py
touch backend/app/routes/blockchain.py

touch backend/app/models/user.py

touch backend/app/schemas/user_schema.py

touch backend/app/services/blockchain_service.py
touch backend/app/services/notification_service.py

touch backend/app/core/database.py
touch backend/app/core/security.py

touch backend/tests/test_health.py
touch backend/tests/test_ico.py

touch backend/requirements.txt
touch backend/Dockerfile

echo "Structure du projet 'backend' créée avec succès."

