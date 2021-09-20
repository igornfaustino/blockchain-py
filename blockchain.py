from datetime import datetime
from typing import List
import json
import hashlib


class Block():
    def __init__(self, index, transaction, proof, previous_hash=None) -> None:
        self.index = index
        self.transaction = transaction
        self.timestamp = int(datetime.now().timestamp())
        self.proof = proof
        self.previous_hash = None

    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True)

    def to_hash(self):
        return hashlib.sha256(self.__str__().encode()).hexdigest()


class Blockchain():
    def __init__(self) -> None:
        self.chain: List[Block] = []
        self.current_transaction = []

        self.create_block(None, None)

    def clear_pending_block_info(self):
        self.current_transaction = []

    def create_block(self, proof, previous_hash) -> Block:
        index = len(self.chain) + 1
        block = Block(index, self.current_transaction, proof, previous_hash)

        self.clear_pending_block_info()
        self.chain.append(block)

        return block

    @property
    def last_block(self) -> Block:
        return self.chain[-1]


blockchain = Blockchain()
print(blockchain.last_block)
