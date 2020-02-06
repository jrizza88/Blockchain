# Paste your version of blockchain.py from the basic_block_gp
# folder here

import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

# DONE new_block
# DONE hash
# DONE proof_of_work
# DONE valid_proof
# DONE /chain endpoint
# DONE /mine endpoint

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        ## self.chain = [{index, timestamp, etc.}]
        ## self.current_transactions = [{sender: 'Jam', recipient:'Rose', amount: 10}]
        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        A block should have:
        * Index
        * Timestamp
        * List of current transactions
        * The proof used to mine this block
        * The hash of the previous block

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            # you do not zero index here..you use length so that it can print the current num of the index
            'index': len(self.chain) + 1,
            # in js it is time.now
            'timestamp': time(),
            # list of current transaactions 
            'transactions': self.current_transactions,

            'proof': proof,
            # self.previous_hash none is used optional, the 'or' statement is to handle non none  cases. 
            # previous block originally already starts at 1, you use the code after 
            # you put all the blocks in self.chain. 
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        # Append the block to the chain
        self.chain.append(block)
        # Return the new block
        return block

    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block

        :param block": <dict> Block
        "return": <str>
        """
        # Step 1: convert block / dictionary / object into usable string
        # Step 2: hash that string and return it
        # Step 3: profit $$

        # Use json.dumps to convert json into a string
        # Use hashlib.sha256 to create a hash
        # It requires a `bytes-like` object, which is what
        # .encode() does.
        # It converts the Python string into a byte string.
        # We must make sure that the Dictionary is Ordered,
        # or we'll have inconsistent hashes

        # Step 1
        # Create the string_object: convert block to a string
        # json.dumps creates it to a string. 
        # dictionaries are not kept in order; Lists are!
        string_object = json.dumps(block, sort_keys=True)
        # Create the block_string
        block_string = string_object.encode()

        # Step 2
        # Hash this string using sha256
        hash_object = hashlib.sha256(block_string)
        hash_string = hash_object.hexdigest()

        # By itself, the sha256 function returns the hash in a raw string
        # that will likely include escaped characters.
        # This can be hard to read, but .hexdigest() converts the
        # hash to a string of hexadecimal characters, which is
        # easier to work with and understand

        # Return the hashed block string in hexadecimal format
        # Gonna look like this:
        # '2c931fa172ec39bc333089e0dc03e904a61a0384b994e418249d1e3320f199c1'
        return hash_string
    # property is a built python syntax that let's use you last_block as a property. 
    # last_block function, but after you instiate it you can refer to it like a property.
    #  i.e. blockchain.last_block
    @property
    def last_block(self):
        return self.chain[-1]

    # def proof_of_work(self):
    #     """
    #     Simple Proof of Work Algorithm
    #     Stringify the block and look for a proof.
    #     Loop through possibilities, checking each one against `valid_proof`
    #     in an effort to find a number that is a valid proof
    #     :return: A valid proof for the provided block
    #     """
    #     # Stringify the block
    #     string_object = json.dumps(self.last_block, sort_keys=True)

    #     proof = 0

    #     while self.valid_proof(string_object, proof) is False:
    #         proof += 1

    #     return proof
    # let's you use this method without instiating this instance
    # Blockchain.valid_proof 
    @staticmethod
    def valid_proof(block_string, proof):
        """
        Validates the Proof:  Does hash(block_string, proof) contain 3
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        guess = f'{block_string}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        if guess_hash[:6] == '000000':
            print(guess_hash)
            return True
        return False

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()



@app.route('/mine', methods=['POST'])
def mine():
    # Run the proof of work algorithm to get the next proof

    proof = blockchain.proof_of_work()

    # Forge the new Block by adding it to the chain with the proof
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': 'We mined a new block!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        # TODO: Return the chain and its current length
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/last_block', methods=['GET'])
def 

# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)