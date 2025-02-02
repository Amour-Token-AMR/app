export default {
  ssr: true,
  target: 'server',
  head: {
    title: "$AMR The AMOUR Token - Express Love on the Blockchain",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      {
        hid: "description",
        name: "description",
        content:
          "Transform your emotions into blockchain poetry with $AMR token. Write love messages, earn rewards, and join a community of romantic crypto enthusiasts. Start expressing love on Web3 today!"
      }
    ],
    link: [
      {
        rel: "icon",
        type: "image/svg+xml",
        href:
          "data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20xml%3Aspace%3D%22preserve%22%20viewBox%3D%220%200%20128%20128%22%3E%3Cpath%20d%3D%22M93.99%208.97c-21.91%200-29.96%2022.39-29.96%2022.39s-7.94-22.39-30-22.39c-16.58%200-35.48%2013.14-28.5%2043.01s58.56%2067.08%2058.56%2067.08%2051.39-37.21%2058.38-67.08c6.98-29.87-10.56-43.01-28.48-43.01%22%20style%3D%22fill%3A%23f44336%22/%3E%3Cpath%20d%3D%22M30.65%2011.2c17.2%200%2025.74%2018.49%2028.5%2025.98.39%201.07%201.88%201.1%202.33.06L64%2031.35C60.45%2020.01%2050.69%208.97%2034.03%208.97c-6.9%200-14.19%202.28-19.86%207.09%205.01-3.29%2010.88-4.86%2016.48-4.86M93.99%208.97c-5.29%200-10.11%201.15-13.87%203.47%202.64-1.02%205.91-1.24%209.15-1.24%2016.21%200%2030.72%2012.29%2024.17%2040.7-5.62%2024.39-38.46%2053.98-48.49%2065.27-.64.72-.86%201.88-.86%201.88s51.39-37.21%2058.38-67.08c6.98-29.86-10.53-43-28.48-43%22"
      },
      {
        rel: "stylesheet",
        href:
          "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap"
      }
    ],
    script: [
      { src: "https://cdn.jsdelivr.net/npm/tsparticles@2.0.6/tsparticles.bundle.min.js", defer: true },
      { src: "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js", defer: true },
      { src: "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js", defer: true }
    ]
  },
  css: ["~/assets/css/main.css"],
  plugins: ["~/plugins/web3.js", "~/plugins/axios.js"],
  modules: ["@nuxtjs/axios"],
  axios: {
    baseURL: process.env.API_URL || "http://localhost:8000/api/v1"
  },
  env: {
    API_URL: process.env.API_URL || "http://localhost:8000/api/v1"
  },
  build: {
    // Configuration d'optimisation si nécessaire
  }
};
