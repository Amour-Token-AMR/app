# ========================================
# Stage 1: Base
# ========================================
FROM node:23.2.0-alpine3.19 AS base

# Définir le répertoire de travail
WORKDIR /app

# Définir les variables d'environnement pour npm
ENV NODE_ENV=development
#ENV NPM_CONFIG_UPDATE_NOTIFIER=false

# Installer les dépendances système requises pour les modules natifs
RUN apk add --no-cache libc6-compat python3 make g++

# Copier les fichiers de dépendances et installer les packages avec cache optimisé
COPY package.json yarn.lock ./
RUN --mount=type=cache,target=/usr/local/share/.cache/yarn/v6 \
    yarn install --frozen-lockfile --network-timeout 1000000

# ========================================
# Stage 2: Build
# ========================================
FROM base AS build

# Passage en mode développement pour les dépendances de build
ENV NODE_ENV=development

# Installer les dépendances de développement
RUN --mount=type=cache,target=/usr/local/share/.cache/yarn/v6 \
    yarn install --frozen-lockfile --network-timeout 1000000

# Copier le code source complet dans l'image
COPY . .

# Compiler l'application Nuxt avec cache pour les artefacts de build
RUN --mount=type=cache,target=/app/.nuxt \
    --mount=type=cache,target=/app/.output \
    yarn build

# ========================================
# Stage 3: Production
# ========================================
FROM node:23.2.0-alpine3.19 AS production

WORKDIR /app

# Copier uniquement les fichiers nécessaires pour la production
COPY --from=build --chown=node:node /app/.output ./.output
COPY --from=build /app/static ./static
COPY --from=build /app/public ./public
COPY --from=build /app/package.json ./package.json

# Utiliser un utilisateur non-root pour la sécurité
USER node

EXPOSE 3000
ENV NITRO_PORT=3000
ENV NODE_ENV=development
#ENV NODE_ENV=production

CMD ["node", ".output/server/index.mjs"]

# ========================================
# Stage 4: Development
# ========================================
FROM base AS development

ENV NODE_ENV=development

RUN --mount=type=cache,target=/usr/local/share/.cache/yarn/v6 \
    yarn install --frozen-lockfile

COPY . .

EXPOSE 3000

CMD ["yarn", "dev", "--hostname", "0.0.0.0"]