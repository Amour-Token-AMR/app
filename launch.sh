#!/bin/bash
# launch.sh
# Ce script est destiné à être exécuté au démarrage de l'environnement de développement (ou de production)
# afin d'arrêter les anciens conteneurs, vérifier les ports, exécuter les tests et redémarrer l'ensemble de la stack.

set -euo pipefail

# Fonction pour vérifier si un port est libre
function check_port() {
  local port=$1
  if lsof -i TCP:"$port" -sTCP:LISTEN >/dev/null 2>&1; then
    echo "Erreur : Le port $port est déjà utilisé."
    return 1
  else
    echo "Port $port est libre."
    return 0
  fi
}

echo "=== Lancement du script de démarrage global ==="

# Vérifier les ports critiques (par exemple 8080 pour Traefik)
# Vous pouvez ajouter d'autres vérifications de ports si nécessaire.
if ! check_port 8080; then
  echo "Tentative de libérer le port 8080..."
  # Attention : Cette commande demande les droits sudo et tue les processus qui utilisent le port.
  sudo fuser -k 8080/tcp || {
    echo "Impossible de libérer le port 8080. Veuillez le libérer manuellement."
    exit 1
  }
  # Re-vérifier le port après avoir tenté de le libérer
  check_port 8080 || exit 1
fi

# Arrêter et nettoyer les conteneurs existants
echo "Arrêt des conteneurs existants..."
docker compose down

# (Optionnel) Nettoyer les volumes et réseaux non utilisés
echo "Nettoyage des ressources Docker inutilisées..."
docker system prune -f

# Exécuter les tests unitaires du backend (adaptable selon vos besoins)
echo "Exécution des tests unitaires du backend..."
docker compose run --rm backend pytest

# Vous pouvez ajouter ici des commandes pour exécuter d'autres tests (par exemple, tests du frontend ou tests E2E).

# Démarrer l'ensemble de la stack avec reconstruction des images
echo "Démarrage de l'ensemble de la stack..."
docker compose up --build -d

# Optionnel : Attendre quelques secondes pour laisser le temps aux conteneurs de démarrer
sleep 5

# Vérifier l'état de quelques services clés (par exemple, backend, frontend, ai-model)
echo "Vérification de l'état des conteneurs..."
docker compose ps

# Afficher les logs en temps réel pour surveiller le démarrage (Ctrl+C pour quitter)
echo "Affichage des logs en direct (Ctrl+C pour quitter)..."
docker compose logs -f

# Fin du script
echo "Le lancement global est terminé."
