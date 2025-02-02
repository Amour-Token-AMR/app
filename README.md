# AI PROMPTS
_THIS_IS_A_SECRET_

1\. Analyse Technique & Vision Globale
--------------------------------------

### Objectifs fonctionnels

-   **Phase 1 -- Landing pré-ICO** : Site vitrine informatif (SEO optimisé, pages statiques dynamiques) réalisé avec Nuxt/Vue, afin de présenter le projet et collecter les leads.
-   **Phase 2 -- Application ICO** : Application décentralisée (DApp) qui permettra aux utilisateurs de se connecter via un wallet web3 (ex. MetaMask) et de participer à l'ICO du token **$AMR**.
-   **Phase 3 -- Application V1** : Une application complète et évolutive qui intègre toutes les fonctionnalités business, interagit avec des smart contracts et offre une expérience utilisateur riche.

### Objectifs techniques

-   **Modularité et scalabilité** : Chaque brique doit pouvoir être montée, mise à jour et scalée indépendamment.
-   **Séparation des environnements** : Un mode "prod" (avec IA en mode déporté) et un mode "dev" (avec IA locale pour itérations rapides).
-   **Interconnexion via des API standardisées** : Tous les services communiqueront via des API REST (ou GraphQL) ou par message via un bus (ici, Redis peut jouer un rôle de cache / broker pour certains messages).
-   **Observabilité & Monitoring** : Intégration d'un système de log management et monitoring (ELK/Loki+Grafana, Prometheus) pour assurer la qualité et la performance de l'ensemble.

* * * * *

2\. Identification des briques techniques
-----------------------------------------

### A. **Frontend (Landing & DApp)**

-   **Nuxt/Vue.js** :
    -   **Landing Page** : Pages informatives, blog, pages légales...
    -   **DApp** : Intégration d'un module web3 pour interagir avec le wallet et afficher l'ICO.
-   **SSR & SEO** : La landing doit être pré-rendue pour le référencement.

### B. **Backend (API & Services métier)**

-   **Python (FastAPI/Flask)** :
    -   **API Gateway** : Point d'entrée pour la communication entre le frontend et le backend.
    -   **Business Logic** : Gestion des inscriptions, des transactions ICO, etc.
    -   **Interface Blockchain** : Appels aux smart contracts via web3.py.
-   **Contrats Smart Contracts (Solidity)** :
    -   **Token $AMR** : Définition des interfaces ERC20 (ou ERC777...) et gestion des fonctions ICO.
    -   **Interfaces d'interaction** : Exposer une API ou des événements que le backend va consommer.

### C. **Workflow & Automatisation**

-   **n8n (workflow automation en Node.js/Python)**
    -   Automatisation des tâches récurrentes (envoi d'emails, notifications, traitements batch...).
    -   Intégration avec d'autres briques via API REST, webhooks ou connexion directe à la DB.

### D. **Bases de Données & Caches**

-   **DB Stockage (PostgreSQL/MySQL)** :
    -   Stockage persistant des données utilisateurs, historiques ICO, logs applicatifs...
-   **DB Redis** :
    -   Cache, sessions, files d'attente rapide (et potentiellement message broker pour certains workflows).

### E. **Log Management & Monitoring**

-   **Stack ELK ou Loki + Grafana/Prometheus** :
    -   Agrégation et visualisation des logs et métriques de chaque service.
    -   Alerting et tableau de bord pour le monitoring en temps réel.

### F. **Modèle IA**

-   **Service IA (Python -- TensorFlow/PyTorch)**
    -   En **prod** : IA déportée dans un container dédié (ou via une API hébergée) pour le traitement en temps réel ou en batch.
    -   En **dev** : Version locale pour tests et ajustements.
-   **Cas d'usage potentiel** : Analyse de comportements, recommandations personnalisées, modération de contenu...

### G. **Infrastructure & Reverse Proxy**

-   **Nginx** (ou Traefik) pour :
    -   Gérer la distribution des requêtes (HTTPS, load balancing).
    -   Agir en point d'entrée unique et router vers les différents containers (front, API, etc.).

* * * * *

3\. Interconnexions et Interfaces entre les briques
---------------------------------------------------

Pour assurer une communication claire et modulable, nous définirons des **contrats d'interface** (API contracts, webhooks, events) pour chaque service :

### A. **Frontend ↔ Backend API**

-   **Contrat** : API REST (OpenAPI/Swagger)
    -   **Endpoints** : `/api/v1/auth`, `/api/v1/ico`, `/api/v1/blockchain`, etc.
    -   **Sécurité** : JWT, OAuth2 selon les besoins.
-   **Interface Web3** : Frontend via web3.js pour interagir directement avec le smart contract (lecture d'état, envoi de transactions).

### B. **Backend ↔ Blockchain**

-   **Contrat** : Wrapper en Python (web3.py) pour communiquer avec les smart contracts.
    -   **Interfaces** : Méthodes du token $AMR, événements (ICO start/stop, transactions...).

### C. **Backend ↔ Workflow (n8n)**

-   **Contrat** : Webhooks et appels d'API
    -   Le backend déclenche des workflows (ex. envoi d'email, notifications) en appelant l'API n8n.
    -   n8n peut également surveiller la DB ou Redis pour lancer des workflows.

### D. **Backend ↔ Base de Données**

-   **Contrat** : Connexion via ORM (SQLAlchemy, etc.) avec un schéma de DB bien documenté.
    -   Séparation claire entre la DB « stockage » et Redis « cache/session/message broker ».

### E. **Service IA ↔ Backend**

-   **Contrat** : API REST ou gRPC
    -   Envoi de données pour inférence et réception des résultats.
    -   Documenter les endpoints et les schémas JSON pour les entrées/sorties.

### F. **Logs & Monitoring**

-   **Contrat** : Logs envoyés par stdout ou par agents (Filebeat, Promtail) vers la stack ELK/Loki.
    -   Utiliser des formats JSON pour faciliter l'indexation et la recherche.

* * * * *

4\. Fichiers de Configuration Modulables
----------------------------------------

Pour garder la configuration flexible, nous allons externaliser toutes les variables d'environnement et paramètres dans des fichiers dédiés :

-   **.env** : Variables globales (ex. DB_URI, REDIS_URI, JWT_SECRET, etc.)
-   **docker-compose.yml** : Définition des services avec la possibilité de surcharger via des fichiers `docker-compose.override.yml` pour dev/prod.
-   **config.yaml / config.json** : Fichiers de configuration pour les applications (backend, n8n, IA) permettant de paramétrer le comportement sans redéployer.
-   **nginx.conf** : Configuration Nginx modulaire pour le reverse proxy.
-   **openapi.yaml** : Spécification de l'API (contrat entre Frontend et Backend).
-   **Smart Contracts** : Fichiers de configuration (truffle-config.js ou hardhat.config.js) pour déployer les contrats sur différentes blockchains (testnet/mainnet).

5\. Actions et Roadmap Détaillée
--------------------------------

1.  **Conception de l'Architecture Globale :**

    -   Établir un schéma détaillé des interactions entre les services.
    -   Définir les API contracts (OpenAPI pour le backend, schémas JSON pour le service IA...).
2.  **Mise en Place des Services Individuels :**

    -   **Frontend Nuxt/Vue** : Création des pages de la landing, intégration du module web3 pour la DApp.
    -   **Backend Python** : Choix du framework (FastAPI recommandé pour sa rapidité et documentation auto via OpenAPI), développement des endpoints pour ICO, gestion des utilisateurs, etc.
    -   **Smart Contracts** : Développement et tests sur un réseau de test (ex. Rinkeby, Goerli) avec Hardhat ou Truffle.
    -   **n8n** : Configuration des workflows de notifications, emails, triggers automatiques.
    -   **DB & Redis** : Installation et configuration avec schémas de données bien documentés.
    -   **Log Management** : Déploiement de la stack ELK ou Loki + Grafana et intégration des agents de logs dans chaque container.
    -   **Service IA** : Développement, entraînement et déploiement du modèle IA en mode déporté et en version locale pour dev.
    -   **Reverse Proxy (Nginx)** : Configuration de Nginx pour router correctement le trafic vers le frontend et l'API, gestion SSL.
3.  **Définition des Interfaces et Contrats d'Échange :**

    -   Rédiger la documentation OpenAPI.
    -   Créer des schémas JSON pour les échanges avec le service IA.
    -   Définir les événements et webhooks pour l'interaction entre backend et n8n.
4.  **Intégration & Tests :**

    -   Tests unitaires et d'intégration pour chaque brique.
    -   Tests de bout en bout sur l'interconnexion (ex. de la landing à l'exécution d'une transaction ICO).
    -   Mise en place de CI/CD pour automatiser les tests et les déploiements.
5.  **Mise en Production et Scalabilité :**

    -   Configuration de l'orchestration via Docker Compose (puis passage éventuel à Kubernetes pour plus de scalabilité).
    -   Monitoring et log management opérationnels.
    -   Optimisation de la sécurité (authentification, chiffrement, sécurité des endpoints blockchain).

_______________

Roadmap Complète du Projet $AMR - Amour Token
=============================================

**Phase 0 -- Préparatifs & Conception**
--------------------------------------

### **Étape 0.1 : Recueil des Exigences et Analyse des Besoins**

-   **Objectifs fonctionnels et techniques**
    -   Définir les besoins de la landing pré-ICO, de la DApp ICO et de l'application V1.
    -   Identifier les exigences non-fonctionnelles : scalabilité, sécurité, haute disponibilité.
-   **Livrables :**
    -   Document de spécifications fonctionnelles et techniques.
    -   Liste des parties prenantes, cas d'utilisation et user stories.

### **Étape 0.2 : Conception de l'Architecture Globale & Définition des Interfaces**

-   **Objectifs :**
    -   Concevoir l'architecture modulaire et évolutive.
    -   Définir les contrats d'interface entre les briques (API REST/OpenAPI, webhooks, schémas JSON pour IA, etc.).
-   **Livrables :**
    -   **Diagramme d'architecture** global (schémas visuels incluant le Frontend, Backend, Smart Contracts, n8n, DB, Redis, Log Management, IA et Reverse Proxy).
    -   **Document de définition des API contracts et interfaces** (spécifications OpenAPI pour le Backend, description des endpoints IA, etc.).

* * * * *

**Phase 1 -- Mise en Place de l'Environnement de Développement et de l'Infrastructure CI/CD**
--------------------------------------------------------------------------------------------

### **Étape 1.1 : Environnement de Développement & Configuration de la Stack Dockerisée**

-   **Objectifs :**
    -   Mettre en place la base d'un environnement de développement local avec Docker et Docker Compose.
    -   Créer les fichiers de configuration génériques (.env, docker-compose.yml, configuration Nginx, etc.).
-   **Livrables :**
    -   **Documentation d'installation et de configuration** de l'environnement (prérequis, guide de démarrage).
    -   **Dockerfile(s) et docker-compose.yml** initial de l'ensemble des services (Frontend, Backend, DB, Redis, n8n, Log Management, IA, Reverse Proxy).

### **Étape 1.2 : Configuration CI/CD et Gestion des Secrets**

-   **Objectifs :**
    -   Mettre en place un pipeline CI/CD (GitHub Actions, GitLab CI ou autre) pour automatiser les tests, builds et déploiements.
    -   Configurer un système de gestion des variables d'environnement et des secrets (ex. .env, Vault).
-   **Livrables :**
    -   **Scripts CI/CD** pour le build, les tests et le déploiement.
    -   **Documentation CI/CD** et instructions pour le déploiement multi-environnements (dev, staging, prod).

* * * * *

**Phase 2 -- Développement des Composants Applicatifs**
------------------------------------------------------

### **Étape 2 : Développement du Frontend (Landing Page & DApp)**

-   **Objectifs :**
    -   Créer la landing page sous Nuxt/Vue avec SSR pour le SEO.
    -   Intégrer les fonctionnalités de la DApp (connexion via wallet web3, interaction avec les smart contracts).
-   **Livrables :**
    -   **Structure du projet Nuxt/Vue** (arborescence, composants, pages).
    -   **Configuration Web3** dans le frontend pour interagir avec MetaMask et lire les données de la blockchain.
    -   **Documentation technique et guide d'implémentation** du frontend.

### **Étape 3 : Développement du Backend (API & Business Logic)**

-   **Objectifs :**
    -   Développer l'API en Python (FastAPI de préférence) qui servira de passerelle entre le frontend et les services métiers.
    -   Intégrer la logique de gestion des inscriptions, transactions ICO, et interactions avec la blockchain via web3.py.
-   **Livrables :**
    -   **Code source du Backend** avec documentation (structure, endpoints, authentification, gestion d'erreurs).
    -   **Spécification OpenAPI** complète décrivant l'ensemble des endpoints.
    -   **Exemples de tests unitaires et d'intégration** pour le backend.

### **Étape 4 : Développement et Déploiement des Smart Contracts**

-   **Objectifs :**
    -   Créer et tester les smart contracts (contrat $AMR, ICO, etc.) en Solidity.
    -   Déployer ces contrats sur un réseau de test (ex. Goerli) et préparer la migration vers le mainnet.
-   **Livrables :**
    -   **Code source des Smart Contracts** (contrat ERC20/777 pour $AMR et logiques ICO).
    -   **Configuration Hardhat/Truffle** pour le déploiement et les tests.
    -   **Documentation et rapports de tests** (tests unitaires, scénarios d'audit).

### **Étape 5 : Mise en Place des Workflows d'Automatisation avec n8n**

-   **Objectifs :**
    -   Automatiser des tâches clés (envoi d'emails, notifications, triggers suite à des événements blockchain ou DB).
-   **Livrables :**
    -   **Workflows configurés dans n8n** avec export/import des flows.
    -   **Documentation des triggers et des actions** disponibles via n8n.

* * * * *

**Phase 3 -- Mise en Production et Intégration des Services Complémentaires**
----------------------------------------------------------------------------

### **Étape 6 : Mise en Place de la Base de Données et Configuration de Redis**

-   **Objectifs :**
    -   Déployer la base de données (PostgreSQL) pour le stockage persistant.
    -   Configurer Redis pour le cache, la gestion des sessions et le message broker.
-   **Livrables :**
    -   **Schémas de la base de données** et scripts de migration (ex. avec Alembic).
    -   **Documentation de la configuration Redis** et cas d'usage.

### **Étape 7 : Mise en Place de la Gestion de Logs et du Monitoring**

-   **Objectifs :**
    -   Installer et configurer la stack de log management (ELK ou Loki + Grafana/Prometheus) pour assurer le suivi et la traçabilité de l'application.
-   **Livrables :**
    -   **Fichiers de configuration ELK/Loki**.
    -   **Dashboard Grafana/Prometheus** pour le monitoring.
    -   **Documentation sur la gestion des logs** et procédures d'alerting.

### **Étape 8 : Déploiement et Intégration du Service IA**

-   **Objectifs :**
    -   Containeriser et déployer le modèle IA (en mode prod déporté et mode dev local).
    -   Définir les endpoints d'inférence (REST ou gRPC) pour permettre une intégration fluide avec le backend.
-   **Livrables :**
    -   **Code et Dockerfile du Service IA** (en TensorFlow/PyTorch).
    -   **Documentation des endpoints IA**, formats d'échange de données et exemples d'appels.
    -   **Tests d'intégration** entre le backend et le service IA.

* * * * *

**Phase 4 -- Tests, Intégration Finale et Mise en Production**
-------------------------------------------------------------

### **Étape 9 : Tests, Intégration et Validation de l'Ensemble**

-   **Objectifs :**
    -   Mettre en place des tests unitaires, d'intégration et end-to-end pour toutes les briques.
    -   Effectuer des tests de charge et de sécurité.
-   **Livrables :**
    -   **Suite de tests automatisés** (unitaires, intégration, e2e).
    -   **Rapports de tests** et indicateurs de performance.
    -   **Documentation sur les procédures de test et validation**.

### **Étape 10 : Documentation Complète et Déploiement en Production**

-   **Objectifs :**
    -   Compiler l'ensemble de la documentation technique (Wiki, ReadTheDocs, diagrammes, guides de déploiement).
    -   Déployer la stack en production avec un suivi continu via CI/CD et monitoring.
-   **Livrables :**
    -   **Documentation complète** de la stack et de ses évolutions.
    -   **Procédures de déploiement** et guides de mise à jour.
    -   **Plan de maintenance et roadmap évolutive** post-MVP.

* * * * *

**Plan d'Action Immédiat**
==========================

Dans les prochaines réponses, nous allons détailler **chaque étape** avec :

1.  **Les documents techniques** (diagrammes, spécifications, guides d'implémentation).
2.  **Les fichiers de configuration** (Dockerfile, docker-compose.yml, fichiers de configuration d'API et de log management).
3.  **Les exemples de code** et scripts d'automatisation (CI/CD, déploiement de smart contracts, etc.).

Pour commencer, **la prochaine réponse sera consacrée à la Phase 0 -- Conception de l'Architecture Globale & Définition des Interfaces**. Nous y aborderons :

-   Le document de spécifications fonctionnelles et techniques.
-   Le diagramme d'architecture global (Front, Backend, Smart Contracts, n8n, DB, Redis, Log Management, IA et Reverse Proxy).
-   La documentation détaillée des contrats d'interface (spécification OpenAPI, schémas JSON pour IA, description des webhooks, etc.).