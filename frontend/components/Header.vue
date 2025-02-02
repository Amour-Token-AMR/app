<template>
    <nav class="navbar">
      <div class="navbar-left">
        <img
          src="https://avatars.githubusercontent.com/u/197024059?s=200&v=4"
          alt="Amour Token Logo"
          class="navbar-logo"
        />
        <span class="navbar-title">$AMR Amour App</span>
      </div>
      <div class="navbar-center">
        <div class="navbar-stat">
          <span class="stat-value-small" id="navMessageCount">1,234</span>
          <span class="stat-label-small">Messages</span>
        </div>
        <div class="navbar-stat">
          <span class="stat-value-small" id="navTokenPrice">$2.45</span>
          <span class="stat-label-small">$AMR Price</span>
        </div>
      </div>
      <div class="navbar-right">
        <nuxt-link to="/ico" class="nav-link">ICO</nuxt-link>
        <a
          href="https://github.com/Amour-Token-AMR/token/blob/main/whitepaper.md"
          class="nav-link"
          target="_blank"
        >Whitepaper</a>
        <button class="connect-wallet" @click="$emit('connect-wallet')">
          {{ walletText }}
        </button>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    props: {
      walletText: {
        type: String,
        default: "Connect Wallet"
      }
    }
  };
  </script>
  
  <style scoped>
  /* Les styles spécifiques au header sont déjà définis dans le CSS global */
  </style>
  