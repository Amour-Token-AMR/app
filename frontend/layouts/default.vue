<template>
    <div>
      <Header :walletText="walletText" @connect-wallet="handleWalletConnect" />
      <nuxt />
      <Footer />
    </div>
  </template>
  
  <script>
  import Header from "~/components/Header.vue";
  import Footer from "~/components/Footer.vue";
  
  export default {
    components: { Header, Footer },
    data() {
      return {
        walletText: "Connect Wallet"
      };
    },
    methods: {
      handleWalletConnect() {
        if (typeof window.ethereum !== "undefined") {
          window.ethereum
            .request({ method: "eth_requestAccounts" })
            .then((accounts) => {
              this.walletText = "0x...." + accounts[0].slice(-4);
            })
            .catch((error) => {
              console.error("Wallet connection error:", error);
            });
        } else {
          window.open("https://metamask.io/download.html", "_blank");
        }
      }
    }
  };
  </script>
  
  <style>
  /* Vous pouvez ajouter ici des styles communs au layout si nécessaire */
  </style>
  