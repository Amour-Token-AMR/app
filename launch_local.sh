#!/bin/bash
# launch_local.sh
# Ce script est destiné à être exécuté sur macOS en environnement de développement.
# Il vérifie et libère les ports critiques, exécute les tests unitaires, puis redémarre l'ensemble de la stack Docker.

set -euo pipefail

echo "=== Lancement du script local sur macOS ==="

# Fonction de vérification d'un port via lsof sur macOS
check_port() {
  local port=$1
  if lsof -i TCP:"$port" -sTCP:LISTEN >/dev/null 2>&1; then
    echo "Erreur : Le port $port est déjà utilisé."
    return 1
  else
    echo "Le port $port est libre."
    return 0
  fi
}

# Vérifier le port 8080 (utilisé par Traefik ou un autre service critique)
PORT_TO_CHECK=8080
echo "Vérification du port $PORT_TO_CHECK..."
if ! check_port $PORT_TO_CHECK; then
  echo "Tentative de libérer le port $PORT_TO_CHECK..."
  # Sur macOS, utiliser lsof pour obtenir la liste des PID sur le port
  PIDS=$(lsof -ti tcp:$PORT_TO_CHECK)
  if [ -n "$PIDS" ]; then
    echo "Killing process(es) sur le port $PORT_TO_CHECK: $PIDS"
    kill -9 $PIDS || {
      echo "Impossible de tuer certains processus. Veuillez libérer le port manuellement."
      exit 1
    }
  else
    echo "Aucun processus trouvé sur le port $PORT_TO_CHECK."
  fi

  # Re-vérifier le port après la tentative
  sleep 1
  if ! check_port $PORT_TO_CHECK; then
    echo "Erreur : Le port $PORT_TO_CHECK est toujours occupé. Veuillez le libérer manuellement."
    exit 1
  fi
fi

# Arrêter et supprimer les conteneurs existants
echo "Arrêt des conteneurs existants..."
docker compose down

# Nettoyer les ressources Docker inutilisées (optionnel, mais utile en dev)
echo "Nettoyage des ressources Docker inutilisées..."
docker system prune -f

# Exécuter les tests unitaires du backend (adaptable selon vos besoins)
echo "Exécution des tests unitaires du backend..."
docker compose run --rm backend pytest

# Démarrer l'ensemble de la stack en mode développement
echo "Démarrage de l'environnement de développement..."
docker compose up --build -d

# Attendre quelques secondes pour que les conteneurs démarrent correctement
sleep 5

# Afficher l'état des conteneurs
echo "Liste des conteneurs actifs :"
docker compose ps

# Afficher les logs en temps réel pour surveiller le démarrage (Ctrl+C pour quitter)
echo "Affichage des logs en direct (Ctrl+C pour quitter)..."
docker compose logs -f

echo "=== Lancement terminé ==="
