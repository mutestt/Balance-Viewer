from flask import Flask, render_template, request
from web3 import Web3

app = Flask(__name__)

# Replace with your RPC URL
BASE_RPC_URL = "https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

@app.route('/', methods=['GET', 'POST'])
def index():
    balance = None
    error = None
    if request.method == 'POST':
        address = request.form.get('address')
        if web3.isAddress(address):
            try:
                balance_wei = web3.eth.get_balance(address)
                balance_eth = web3.fromWei(balance_wei, 'ether')
                balance = f"{balance_eth} ETH"
            except Exception as e:
                error = f"Error fetching balance: {str(e)}"
        else:
            error = "Invalid wallet address."
    return render_template('index.html', balance=balance, error=error)

if __name__ == '__main__':
    app.run(debug=True)
