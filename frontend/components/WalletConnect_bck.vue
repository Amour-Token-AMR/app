<!-- components/WalletConnect.vue -->
<template>
  <div class="wallet-connect">
    <button @click="connectWallet" v-if="!account">Se connecter avec MetaMask</button>
    <div v-else>
      <p>Connecté en tant que : {{ account }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      account: null
    }
  },
  methods: {
    async connectWallet() {
      try {
        // Utilisation de l'instance web3 injectée
        const accounts = await this.$web3.eth.requestAccounts()
        this.account = accounts[0]
        this.$emit('wallet-connected', this.account)
      } catch (error) {
        console.error('Erreur lors de la connexion du wallet:', error)
      }
    }
  },
  mounted() {
    // Optionnel : vérifier si le wallet est déjà connecté
    this.$web3.eth.getAccounts()
      .then(accounts => {
        if (accounts.length > 0) {
          this.account = accounts[0]
          this.$emit('wallet-connected', this.account)
        }
      })
  }
}
</script>

<style scoped>
.wallet-connect {
  margin: 1rem 0;
}
button {
  background-color: #ff4081;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 5px;
  cursor: pointer;
}
</style>

