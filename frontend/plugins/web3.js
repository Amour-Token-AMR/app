import Web3 from "web3";

export default ({ app }, inject) => {
  let web3;
  if (process.client && typeof window.ethereum !== "undefined") {
    web3 = new Web3(window.ethereum);
    window.ethereum
      .request({ method: "eth_requestAccounts" })
      .then(() => {
        console.log("Wallet connected via Web3");
      })
      .catch((error) => {
        console.error("Web3 wallet connection error:", error);
      });
  } else {
    const provider = new Web3.providers.HttpProvider(
      "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    );
    web3 = new Web3(provider);
    console.warn("No wallet detected, using public provider");
  }
  inject("web3", web3);
};
