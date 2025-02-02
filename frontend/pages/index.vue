<template>
  <div>
    <!-- La navbar, le header et le footer seront intégrés via le layout par défaut -->
    <div id="particles-js"></div>
    <div class="content">
      <section class="hero">
        <h1>Express Love on the Blockchain</h1>
        <p>Turn Your Emotions Into Digital Treasures</p>
        <input
          type="text"
          class="message-input"
          placeholder="Write your crypto-love message here..."
          maxlength="280"
          v-model="message"
        />
        <button class="submit-btn" @click="submitMessage">
          Submit Message 💎
        </button>
      </section>
      <section class="stats">
        <div class="stats-grid">
          <div class="stat-item">
            <div class="stat-value" id="messageCount">1,234</div>
            <div class="stat-label">Messages Created</div>
          </div>
          <div class="stat-item">
            <div class="stat-value" id="tokenValue">$2.45</div>
            <div class="stat-label">$AMR Price</div>
          </div>
          <div class="stat-item">
            <div class="stat-value" id="totalLocked">$1.2M</div>
            <div class="stat-label">Total Love Locked</div>
          </div>
        </div>
      </section>
      <section class="features">
        <div class="feature-card">
          <div class="feature-icon">🤖💘</div>
          <h3>AI-Powered</h3>
          <p>
            Our AI transforms your emotions into unique blockchain poetry
          </p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">💎💰</div>
          <h3>Earn Tokens</h3>
          <p>Get $AMR tokens for every heartfelt message created</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🌟🔥</div>
          <h3>Community Voting</h3>
          <p>
            Vote for the most romantic messages to earn rewards
          </p>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ""
    };
  },
  mounted() {
    // Initialisation de tsParticles
    if (typeof tsParticles !== "undefined") {
      tsParticles.load("particles-js", {
        particles: {
          number: { value: 80, density: { enable: true, value_area: 800 } },
          color: { value: "#ff1b6b" },
          shape: { type: "heart" },
          opacity: { value: 0.5 },
          size: { value: 3, random: true },
          line_linked: {
            enable: true,
            distance: 150,
            color: "#ff1b6b",
            opacity: 0.4,
            width: 1
          },
          move: {
            enable: true,
            speed: 2,
            direction: "none",
            random: false,
            straight: false,
            out_mode: "out",
            bounce: false
          }
        },
        interactivity: {
          detect_on: "canvas",
          events: {
            onhover: { enable: true, mode: "repulse" },
            onclick: { enable: true, mode: "push" },
            resize: true
          }
        },
        retina_detect: true
      });
    }
    // Lancement des animations GSAP
    if (typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined") {
      gsap.registerPlugin(ScrollTrigger);
      gsap.from(".hero h1", {
        duration: 1,
        y: 50,
        opacity: 0,
        ease: "power3.out"
      });
      gsap.from(".hero p", {
        duration: 1,
        y: 30,
        opacity: 0,
        delay: 0.3,
        ease: "power3.out"
      });
      gsap.from(".feature-card", {
        duration: 0.8,
        y: 50,
        opacity: 0,
        stagger: 0.2,
        scrollTrigger: {
          trigger: ".features",
          start: "top center"
        }
      });
    }
    // Synchronisation initiale des statistiques (optionnel)
    this.syncStats();
  },
  methods: {
    submitMessage() {
      console.log("Message submitted:", this.message);
      // Intégrer ici l'appel API pour enregistrer le message
    },
    syncStats() {
      const messageCount = document.getElementById("messageCount").textContent;
      const tokenValue = document.getElementById("tokenValue").textContent;
      if (document.getElementById("navMessageCount"))
        document.getElementById("navMessageCount").textContent = messageCount;
      if (document.getElementById("navTokenPrice"))
        document.getElementById("navTokenPrice").textContent = tokenValue;
    }
  }
};
</script>

<style scoped>
/* Vous pouvez ajouter ici des styles spécifiques à cette page si nécessaire */
</style>
