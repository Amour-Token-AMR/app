// nuxt.config.js
export default {
  // Mode SSR pour un SEO optimisé
  ssr: true,
  
  // Target: 'server' pour le rendu côté serveur
  target: 'server',

  // Global page headers
  head: {
    title: 'AMR - Amour Token',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Découvrez AMR, le token d\'amour pour une ICO innovante' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS
  css: [
    '~/assets/styles/main.scss'
  ],

  // Plugins à charger avant l'initialisation de l'app
  plugins: [
    '~/plugins/web3.js',
    '~/plugins/axios.js'
  ],

  // Auto import des composants
  components: true,

  // Modules Nuxt
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/sitemap'
  ],

  // Configuration d'Axios (appel vers le backend)
  axios: {
    baseURL: process.env.API_URL || 'http://localhost:8000/api/v1'
  },

  // Configuration du build
  build: {
    // Possibilité d'ajouter des loaders, plugins de webpack, etc.
  },

  // Variables d'environnement
  env: {
    API_URL: process.env.API_URL || 'http://localhost:8000/api/v1',
    NODE_ENV: process.env.NODE_ENV || 'development'
  }
}

