export default function ({ $axios }) {
    $axios.onError((error) => {
      console.error("Axios error:", error);
    });
  }
  