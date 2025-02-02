// plugins/web3.js
import Web3 from 'web3'

export default ({ app }, inject) => {
  let web3

  // Vérifier la présence d'un provider (MetaMask)
  if (process.client && typeof window.ethereum !== 'undefined') {
    web3 = new Web3(window.ethereum)
    // Demander la permission à l'utilisateur
    window.ethereum.request({ method: 'eth_requestAccounts' })
      .then(() => {
        console.log('Wallet connecté')
      })
      .catch((error) => {
        console.error('Erreur de connexion au wallet:', error)
      })
  } else {
    // Fallback vers un provider public (optionnel)
    const provider = new Web3.providers.HttpProvider('https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID')
    web3 = new Web3(provider)
    console.warn('Aucun wallet détecté, utilisation du provider public')
  }

  // Injecter web3 dans le contexte Nuxt et Vue instance
  inject('web3', web3)
}

