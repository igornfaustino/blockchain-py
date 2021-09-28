import json
import hashlib

from typing import List
from datetime import datetime


class Miner():
    @staticmethod
    def proof_of_work(last_proof):
        proof = 0
        while Blockchain.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof


class Block():
    def __init__(self, index, transaction, proof, previous_hash=None) -> None:
        self.index = index
        self.transaction = transaction
        self.timestamp = int(datetime.now().timestamp())
        self.proof = proof
        self.previous_hash = previous_hash

    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True)

    def toJson(self) -> str:
        return self.__dict__

    def to_hash(self):
        return hashlib.sha256(self.__str__().encode()).hexdigest()


class Blockchain():
    def __init__(self) -> None:
        self.chain: List[Block] = []
        self.current_transactions = []

        self.create_block(100, 0)

    def clear_pending_block_info(self):
        self.current_transactions = []

    def create_block(self, proof, previous_hash) -> Block:
        index = len(self.chain) + 1
        block = Block(index, self.current_transactions, proof, previous_hash)

        self.clear_pending_block_info()
        self.chain.append(block)

        return block

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        self.current_transactions.append(transaction)

        return len(self.chain)

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self) -> Block:
        return self.chain[-1]
    
    @property
    def serializableChain(self) -> list:
        return list(map(lambda block : block.toJson(), self.chain))
