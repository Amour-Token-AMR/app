<!-- pages/index.vue -->
<template>
  <div>
    <Header />
    <section class="hero">
      <h1>Bienvenue dans l'univers d'Amour Token ($AMR)</h1>
      <p>Découvrez la révolution blockchain portée par l'amour et la confiance.</p>
      <nuxt-link to="/ico" class="btn-primary">Participer à l'ICO</nuxt-link>
    </section>
    <section class="features">
      <div class="feature" v-for="feature in features" :key="feature.id">
        <h3>{{ feature.title }}</h3>
        <p>{{ feature.description }}</p>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script>
import Header from '~/components/Header.vue'
import Footer from '~/components/Footer.vue'

export default {
  components: { Header, Footer },
  data() {
    return {
      features: [
        { id: 1, title: 'Sécurité', description: 'Des transactions sécurisées et transparentes.' },
        { id: 2, title: 'Innovation', description: 'Une ICO repensée pour une nouvelle ère blockchain.' },
        { id: 3, title: 'Communauté', description: 'Un projet construit par et pour sa communauté.' }
      ]
    }
  }
}
</script>

<style scoped>
.hero {
  text-align: center;
  margin: 3rem 0;
}
.btn-primary {
  background-color: #ff4081;
  color: #fff;
  padding: 0.75rem 1.5rem;
  border-radius: 5px;
  text-decoration: none;
}
.features {
  display: flex;
  justify-content: space-around;
  margin: 2rem 0;
}
.feature {
  flex: 1;
  margin: 0 1rem;
  text-align: center;
}
</style>

