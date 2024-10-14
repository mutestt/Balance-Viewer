# Base Wallet Balance Viewer

## Description

**Base Wallet Balance Viewer** is a simple and intuitive service for checking wallet balances on the Base blockchain. The application allows users to enter a wallet address and retrieve the current balance in ETH.

## Technologies

- **Python**: Backend logic and blockchain interaction via Web3.py
- **Flask**: Web framework for creating the web interface
- **Web3.py**: Library for interacting with EVM-compatible blockchains
- **HTML/CSS**: Creating a simple and clean user interface

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/base-wallet-balance-viewer.git
    cd base-wallet-balance-viewer
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure RPC URL:**

    In the `app.py` file, replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID or another RPC URL for Base.

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Enter a Base wallet address in the input field.
2. Click the "Check Balance" button.
3. View the wallet balance displayed on the page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, contact me at [your email] or open an issue in the repository.
