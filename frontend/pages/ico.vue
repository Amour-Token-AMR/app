<template>
  <div>
    <div class="ico-content">
      <h1>Participate in the ICO</h1>
      <WalletConnect @wallet-connected="onWalletConnected" />
      <div v-if="walletAddress">
        <p>Welcome, {{ walletAddress }}!</p>
        <form @submit.prevent="participateICO">
          <label for="amount">Amount in ETH to invest:</label>
          <input
            type="number"
            v-model="amount"
            id="amount"
            min="0.01"
            step="0.01"
            required
          />
          <button type="submit">Participate</button>
        </form>
        <p v-if="txStatus">{{ txStatus }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import WalletConnect from "~/components/WalletConnect.vue";

export default {
  components: { WalletConnect },
  data() {
    return {
      walletAddress: null,
      amount: 0,
      txStatus: ""
    };
  },
  methods: {
    onWalletConnected(address) {
      this.walletAddress = address;
    },
    async participateICO() {
      try {
        const response = await this.$axios.$post("/ico/participate", {
          walletAddress: this.walletAddress,
          amount: this.amount
        });
        this.txStatus = "Transaction successful: " + response.transactionId;
      } catch (error) {
        console.error("ICO participation error:", error);
        this.txStatus = "Transaction failed.";
      }
    }
  }
};
</script>

<style scoped>
.ico-content {
  padding: 100px 20px;
  text-align: center;
}
form {
  margin: 20px auto;
  max-width: 400px;
  display: flex;
  flex-direction: column;
}
label {
  margin-bottom: 8px;
}
input {
  padding: 8px;
  margin-bottom: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  padding: 10px;
  background-color: #ff4081;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
