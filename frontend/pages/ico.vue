<!-- pages/ico.vue -->
<template>
  <div>
    <Header />
    <section class="ico-section">
      <h1>Participer à l'ICO</h1>
      <WalletConnect @wallet-connected="onWalletConnected" />
      <div v-if="account">
        <p>Bienvenue, {{ account }} !</p>
        <!-- Formulaire pour participer à l'ICO -->
        <form @submit.prevent="participateICO">
          <label for="amount">Montant en ETH à investir :</label>
          <input type="number" v-model="amount" id="amount" min="0.01" step="0.01" required />
          <button type="submit">Participer</button>
        </form>
        <p v-if="txStatus">{{ txStatus }}</p>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
import WalletConnect from '~/components/WalletConnect.vue'
import Header from '~/components/Header.vue'
import Footer from '~/components/Footer.vue'

export default {
  components: { WalletConnect, Header, Footer },
  data() {
    return {
      account: null,
      amount: 0,
      txStatus: ''
    }
  },
  methods: {
    onWalletConnected(account) {
      this.account = account
    },
    async participateICO() {
      try {
        // Exemple d'appel à une fonction de smart contract (le détail de l'ABI et de l'adresse doit être renseigné)
        const contractABI = [ /* ABI du smart contract */ ]
        const contractAddress = '0xYourContractAddress'
        const contract = new this.$web3.eth.Contract(contractABI, contractAddress)
        
        // Exemple : appel à la fonction 'buyTokens' du contrat
        const tx = await contract.methods.buyTokens(this.account)
          .send({ from: this.account, value: this.$web3.utils.toWei(this.amount.toString(), 'ether') })
        
        this.txStatus = 'Transaction réussie : ' + tx.transactionHash
      } catch (error) {
        console.error('Erreur lors de la participation à l\'ICO:', error)
        this.txStatus = 'Erreur de transaction'
      }
    }
  }
}
</script>

<style scoped>
.ico-section {
  padding: 2rem;
  text-align: center;
}
form {
  margin: 2rem auto;
  max-width: 400px;
  display: flex;
  flex-direction: column;
}
label {
  margin-bottom: 0.5rem;
}
input {
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 3px;
}
button {
  background-color: #ff4081;
  color: white;
  border: none;
  padding: 0.75rem;
  border-radius: 5px;
  cursor: pointer;
}
</style>

