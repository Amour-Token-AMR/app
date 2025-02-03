#!/bin/bash
set -e

# Environment variables with defaults
: "${DEV_POSTGRES_USER:=postgres}"
: "${DEV_POSTGRES_PASSWORD:=password}"
: "${DEV_POSTGRES_DB:=amr_db}"
: "${N8N_POSTGRES_USER:=n8n_user}"
: "${N8N_POSTGRES_PASSWORD:=n8n_password}"
: "${N8N_POSTGRES_DB:=amr_n8n}"

echo "Initializing databases and users..."
echo "DEV User: ${DEV_POSTGRES_USER}"
echo "DEV DB: ${DEV_POSTGRES_DB}"
echo "N8N User: ${N8N_POSTGRES_USER}"
echo "N8N DB: ${N8N_POSTGRES_DB}"

# Execute as PostgreSQL superuser
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<EOSQL
-- Update DEV user password if exists
DO \$\$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${DEV_POSTGRES_USER}') THEN
    EXECUTE format('ALTER ROLE %I WITH PASSWORD %L', 
      '${DEV_POSTGRES_USER}', '${DEV_POSTGRES_PASSWORD}');
  ELSE
    CREATE ROLE "${DEV_POSTGRES_USER}" WITH 
      LOGIN 
      SUPERUSER 
      CREATEDB 
      CREATEROLE 
      INHERIT 
      REPLICATION 
      PASSWORD '${DEV_POSTGRES_PASSWORD}';
  END IF;
END \$\$;

-- Create DEV database if not exists
SELECT 'CREATE DATABASE "${DEV_POSTGRES_DB}" 
  WITH OWNER "${DEV_POSTGRES_USER}"
  ENCODING ''UTF8''
  LC_COLLATE ''C''
  LC_CTYPE ''C''
  TEMPLATE template0'
WHERE NOT EXISTS (
  SELECT 1 FROM pg_database 
  WHERE datname = '${DEV_POSTGRES_DB}'
)\gexec

-- Create N8N user if not exists
SELECT 'CREATE ROLE "${N8N_POSTGRES_USER}" WITH 
    LOGIN 
    NOSUPERUSER 
    NOCREATEDB 
    NOCREATEROLE 
    INHERIT 
    NOREPLICATION 
    CONNECTION LIMIT -1 
    PASSWORD ''${N8N_POSTGRES_PASSWORD}'''
WHERE NOT EXISTS (
  SELECT 1 FROM pg_roles 
  WHERE rolname = '${N8N_POSTGRES_USER}'
)\gexec

-- Create N8N database if not exists
SELECT 'CREATE DATABASE "${N8N_POSTGRES_DB}" 
  WITH OWNER "${N8N_POSTGRES_USER}"
  ENCODING ''UTF8''
  LC_COLLATE ''C''
  LC_CTYPE ''C''
  TEMPLATE template0'
WHERE NOT EXISTS (
  SELECT 1 FROM pg_database 
  WHERE datname = '${N8N_POSTGRES_DB}'
)\gexec

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE "${DEV_POSTGRES_DB}" TO "${DEV_POSTGRES_USER}";
GRANT ALL PRIVILEGES ON DATABASE "${N8N_POSTGRES_DB}" TO "${N8N_POSTGRES_USER}";

-- Revoke public access
REVOKE CONNECT ON DATABASE "${DEV_POSTGRES_DB}" FROM PUBLIC;
REVOKE CONNECT ON DATABASE "${N8N_POSTGRES_DB}" FROM PUBLIC;
EOSQL

echo "Database initialization completed successfully."