# backend/app/services/blockchain_service.py
import json
import os
from web3 import Web3

# Récupération des variables d'environnement
INFURA_URL = os.getenv("INFURA_URL", "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0xYourContractAddress")

# Chargement de l'ABI du smart contract depuis un fichier (assurez-vous que le chemin soit correct)
with open("app/contracts/AMRTokenABI.json") as f:
    CONTRACT_ABI = json.load(f)

# Initialisation de la connexion à la blockchain
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def buy_tokens(wallet_address: str, amount: float) -> str:
    """
    Appelle la fonction 'buyTokens' du smart contract pour permettre à l'utilisateur
    d'acheter des tokens en investissant un montant en ETH.
    """
    # Récupération de l'adresse et de la clé privée administrateur
    admin_address = os.getenv("ADMIN_ADDRESS", "0xAdminAddress")
    admin_private_key = os.getenv("ADMIN_PRIVATE_KEY", "YOUR_PRIVATE_KEY")
    
    # Construction de la transaction
    tx = contract.functions.buyTokens(wallet_address).buildTransaction({
        'from': admin_address,
        'value': w3.toWei(amount, 'ether'),
        'nonce': w3.eth.getTransactionCount(admin_address),
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei')
    })

    # Signature de la transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=admin_private_key)
    # Envoi de la transaction
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    # Optionnel : Attendre la confirmation de la transaction
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt.transactionHash.hex()
