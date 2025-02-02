#!/bin/bash
set -e
# Ce script crée une base de données portant le même nom que l’utilisateur, si elle n’existe pas.
psql -v ON_ERROR_STOP=1 --username "$DEV_POSTGRES_USER" --dbname "$DEV_POSTGRES_DB" <<-'EOSQL'
   SELECT 'CREATE DATABASE "$DEV_POSTGRES_USER"' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$DEV_POSTGRES_USER')\gexec
EOSQL
