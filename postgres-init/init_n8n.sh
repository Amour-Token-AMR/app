#!/bin/bash
set -e

# Définir des valeurs par défaut si les variables d'environnement ne sont pas définies
: ${N8N_POSTGRES_USER:=n8n_user}
: ${N8N_POSTGRES_PASSWORD:=n8n_password}
: ${N8N_POSTGRES_DB:=amr_n8n}

echo "Utilisation de N8N_POSTGRES_USER: ${N8N_POSTGRES_USER}"
echo "Utilisation de N8N_POSTGRES_PASSWORD: ${N8N_POSTGRES_PASSWORD}"
echo "Utilisation de N8N_POSTGRES_DB: ${N8N_POSTGRES_DB}"

echo "Création du rôle ${N8N_POSTGRES_USER} s'il n'existe pas déjà..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<EOSQL
DO \$\$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = '${N8N_POSTGRES_USER}') THEN
    CREATE ROLE ${N8N_POSTGRES_USER} WITH LOGIN PASSWORD '${N8N_POSTGRES_PASSWORD}';
  END IF;
END
\$\$;
EOSQL

echo "Création de la base de données ${N8N_POSTGRES_DB} avec ${N8N_POSTGRES_USER} en tant que propriétaire, si elle n'existe pas déjà..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<EOSQL
DO \$\$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = '${N8N_POSTGRES_DB}') THEN
    CREATE DATABASE ${N8N_POSTGRES_DB} OWNER ${N8N_POSTGRES_USER};
  END IF;
END
\$\$;
EOSQL

echo "Initialisation de n8n terminée."
