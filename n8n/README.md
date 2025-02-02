# n8n - Plateforme d'automatisation

Ce dossier contient l'ensemble des fichiers de configuration, workflows, et credentials pour l'installation et la personnalisation de n8n.

## Structure du Dossier

- **credentials/** : Fichiers de credentials (SMTP, API keys, etc.).
- **environment/** : Fichier(s) d'environnement spécifiques à n8n.
- **workflows/** : Workflows exportés en JSON et leur documentation.
- **n8n.config.json** : Configuration personnalisée pour n8n.
  
## Utilisation

- **Montage en Volume** : Le dossier `n8n/` sera monté dans le container sur `/home/node/.n8n`, ce qui permet de conserver et versionner toutes vos configurations et workflows.
- **Mise à jour automatique** : À chaque démarrage du container, les modifications apportées en local seront prises en compte.

Consultez les README dans les sous-dossiers pour plus de détails sur chaque type de fichier.
