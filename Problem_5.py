'''
5. Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created and text strings as the data.

We can breakdown the blockchain down into having 3 main parts.
- First is the information hash
- The next main component is the block on the blockchain
- Finally link all of this together in a block chain
'''

from datetime import datetime
import hashlib


class Block:

    def __init__(self, data, previous_hash):
        current_datetime = datetime.now().strftime("%H:%M:%S")
        self.timestamp = current_datetime
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def append(self, data):
        """ Append a value to the end of the BlockChain. """

        if self.tail is None:
            self.tail = Block(data=data, previous_hash=None)

        else:
            self.tail = Block(data=data, previous_hash=self.tail)


    def size(self):
        """ Return the size or length of the BlockChain. """
        position_head = self.tail
        length = 0

        while position_head is not None:
            position_head = position_head.previous_hash
            length += 1

        return length

    def format(self):
        """Transforms the BlockChain content into a list"""
        block_dict = {}
        block = self.tail
        while block:
            block_dict['data'] = block.data
            block_dict['timestamp'] = block.timestamp
            block_dict['hash'] = block.hash
            block = block.previous_hash
        return block_dict



blockchain = BlockChain()

print(blockchain.size())
# 0
print(blockchain.format())
# {}

blockchain.append('block 1')
print(blockchain.size())
# 1
print(blockchain.format())
#{'data': 'block 1', 'timestamp': 09:01:05, 'hash': 'cabdbdfa02c612a9652e5e4965db9180b25e68ffcdb4deb4b278992a3967c67f'}
blockchain.append('block 3')
blockchain.append('block 4')
print(blockchain.size())
# 3
print(blockchain.format())
# {'data': 'block 1', 'timestamp': '09:01:05', 'hash': 'cabdbdfa02c612a9652e5e4965db9180b25e68ffcdb4deb4b278992a3967c67f'}