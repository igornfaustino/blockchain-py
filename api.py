
import hashlib
import json
from blockchain import Blockchain, Miner
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, request, jsonify

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block.proof
    proof = Miner.proof_of_work(last_proof)

    blockchain.add_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    previous_hash = last_block.to_hash()
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block.index,
        'transactions': block.transaction,
        'proof': block.proof,
        'previous_hash': block.previous_hash,
    }

    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.serializableChain,
        'length': len(blockchain.serializableChain),
    }
    
    return response, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
