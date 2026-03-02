# escrow.py

# In-memory storage
escrows = {}  # {chat_id: {buyer, seller, amount, status, buyer_wallet, seller_wallet}}

# Replace these with your actual TRC20 addresses
DEFAULT_BUYER_WALLET = "TRuHXCeJXJ9L8temLhLzdeXwruRuV3HHtR"
DEFAULT_SELLER_WALLET = "TRuHXCeJXJ9L8temLhLzdeXwruRuV3HHtR"

def create_escrow(chat_id, buyer, seller, amount):
    escrows[chat_id] = {
        "buyer": buyer,
        "seller": seller,
        "amount": amount,
        "status": "Pending",
        "buyer_wallet": DEFAULT_BUYER_WALLET,
        "seller_wallet": DEFAULT_SELLER_WALLET
    }
    return escrows[chat_id]

def get_escrow(chat_id):
    return escrows.get(chat_id, None)

def release_escrow(chat_id):
    escrow = escrows.get(chat_id, None)
    if escrow and escrow["status"] != "Released":
        escrow["status"] = "Released"
        return escrow
    return None

def cancel_escrow(chat_id):
    if chat_id in escrows:
        del escrows[chat_id]
        return True
    return False

def format_escrow(data):
    return (f"Buyer: {data['buyer']}\nBuyer Wallet: {data['buyer_wallet']}\n"
            f"Seller: {data['seller']}\nSeller Wallet: {data['seller_wallet']}\n"
            f"Amount: {data['amount']}\nStatus: {data['status']}")
