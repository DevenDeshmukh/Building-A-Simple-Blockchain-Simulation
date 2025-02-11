import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)
    
    def add_block(self, transactions):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, last_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.compute_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    def tamper_block(self, index, new_transactions):
        if index < len(self.chain):
            self.chain[index].transactions = new_transactions
            self.chain[index].hash = self.chain[index].compute_hash()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

# Usage
bc = Blockchain()
bc.add_block(["UserA -> UserB: 10 BTC", "UserC -> UserD: 5 BTC"])
bc.add_block(["UserX -> UserY: 3 BTC"])

print("Blockchain before tampering:")
bc.print_chain()

print("Is chain valid?", bc.is_chain_valid())

# Tampering with the blockchain
bc.tamper_block(1, ["UserA -> UserB: 100 BTC"])
print("\nBlockchain after tampering:")
bc.print_chain()
print("Is chain valid?", bc.is_chain_valid())
