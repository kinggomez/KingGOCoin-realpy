import hashlib
import time
import random

class Blockchain:
    def __init__(self):
        self.aiminers = [200000]
        self.pending_transaction = []
        self.blocks = []
        self.advanced_miners = []
        self.mining_spaces = []
        self.approved_minig_method = []
        self.user_miners = []
        self.creators = ["King Gomez"]
        self.user_ids = []
        self.user_publickey = []
        self.sold_miningspaces = []
        self.nftrequests = []
        self.stored_hash = []
        self.approvedrequest = []

    def new_block(self, hash, previous_hash, transaction_recipient, transaction_sender, transaction_amount, sender_public, receiver_public):
        block = {
            "previous_hash": 0**64,
            "transaction_sender": "KING",
            "transaction_recipient": "KING",
            "transaction_amount": 200,
            "sender_public": "KING",
            "receiver_public": "KING",
            "genesis_hash": hashlib.sha256(block).hexdigest()
        }
        self.blocks.append(block)
        self.stored_hash.append(self.genesis_hash)

    def create_block(self, hash, previous_hash, transaction_recipient, transaction_sender, transaction_amount, sender_public, receiver_public):
        user_block = {
            "previous_hash": self.genesis_hash,
            "transaction_sender": name,
            "transaction_recipient": recipient,
            "transaction_amount": amount,
            "sender_public": public,
            "receiver_public": secpublic,
            "hash": hashlib.sha256(user_block).hexdigest()
        }
        name = "KingGomez"
        recipient = "Tola"
        amount = 2550
        public = "89cc4fd"
        secpublic = "9adbbshgkj"
        self.blocks.append(user_block)
blockchain = Blockchain()
print(blockchain.blocks)
