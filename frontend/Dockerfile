FROM node:18-alpine

WORKDIR /app

# Copier package.json et yarn.lock pour profiter du cache
COPY package.json *.lock ./

RUN npm install

# Copier le reste du code
COPY . .

# Construire l’application Nuxt
RUN npm build

EXPOSE 3000

# Lancer le serveur Nuxt en mode production
CMD ["npm", "start"]
