<template>
    <button class="connect-wallet" @click="handleConnect">{{ buttonText }}</button>
  </template>
  
  <script>
  export default {
    data() {
      return {
        buttonText: "Connect Wallet",
        isConnected: false
      };
    },
    methods: {
      async handleConnect() {
        if (!this.isConnected) {
          if (typeof window.ethereum !== "undefined") {
            try {
              const accounts = await window.ethereum.request({
                method: "eth_requestAccounts"
              });
              this.isConnected = true;
              this.buttonText = "0x...." + accounts[0].slice(-4);
              this.$emit("wallet-connected", accounts[0]);
            } catch (error) {
              console.error("User denied account access", error);
            }
          } else {
            window.open("https://metamask.io/download.html", "_blank");
          }
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .connect-wallet {
    background-color: #ff4081;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>
  