# Building-A-Simple-Blockchain-Simulation
Demonstration of basic understanding of programming, problem-solving, and blockchain concepts by creating a simple blockchain simulation by using Python 

A)Overview:

This project is a basic blockchain simulation implemented in Python. It demonstrates how blockchain works, including features like hashing, proof-of-work, chain validation, and tampering detection.

B)Features:

Block structure with index, timestamp, transactions, previous hash, and current hash.

SHA-256 hashing for securing blocks.

Proof-of-Work mechanism to validate block addition.

Chain validation to detect tampering.

Demonstration of blockchain security by modifying block data and checking integrity.

C)Installation:

Prerequisites-

Ensure you have Python installed on your system.

D)Steps:

1)Clone this repository:
git clone <repository_url>
cd simple-blockchain

2)Run the script:
python blockchain.py

E) Usage

The script initializes a blockchain with a genesis block.

It adds new blocks with dummy transactions.

The blockchain integrity is checked before and after tampering with a block.

F)Example Output:

Blockchain before tampering:
{Block details...}
Is chain valid? True

Blockchain after tampering:
{Tampered block details...}
Is chain valid? False

G) Future Improvements:

Implement a transaction pool before mining.

Add network nodes to simulate a decentralized system.

Implement a simple user interface.
