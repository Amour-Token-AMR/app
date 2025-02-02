# ========================================
# Stage 1: Base
# ========================================
FROM node:18-alpine AS base

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

# Copier le code source complet dans l'image
COPY . .

# ========================================
# Stage 2: Build
# ========================================
FROM base AS build

# Compiler l'application Nuxt (génère le dossier .nuxt et optimise les assets)
RUN yarn build

# ========================================
# Stage 3: Production
# ========================================
FROM node:18-alpine AS production

# Définir le répertoire de travail
WORKDIR /app

# Copier les artefacts de build générés
COPY --from=build /app/.nuxt .nuxt
COPY --from=build /app/static static

# Copier également package.json et yarn.lock pour installer uniquement les dépendances de production
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --production

# Exposer le port de l'application
EXPOSE 3000

# Démarrer l'application en mode production
CMD ["yarn", "start"]

# ========================================
# Stage 4: Development
# ========================================
FROM base AS development

# Exposer le port de l'application en mode développement
EXPOSE 3000

# Lancer Nuxt en mode développement avec hot-reload
CMD ["yarn", "dev"]
