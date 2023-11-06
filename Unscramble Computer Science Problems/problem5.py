import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return f"Block data: {self.data} \nTimestamp: {self.timestamp} \nHash: {self.hash}"

class BlockChain:

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        if self.tail is None:
            self.tail = Block(datetime.now(), data, previous_hash=None)
        else:
            self.tail = Block(datetime.now(), data, previous_hash=self.tail)
        self.size += 1

    def search(self, data):
        if self.tail:
            curr_block = self.tail
            while curr_block:
                if curr_block.data == data:
                    return curr_block
                curr_block = curr_block.previous_hash 
        return None
    

    def get_size(self):
        return self.size

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

blockchain = BlockChain()

blockchain.append('A')
blockchain.append('B')
blockchain.append('C')

## Test Case 1
print(blockchain.get_size())  # 3

## Test Case 2
print(blockchain.search('B')) # prints block data

## Test Case 3
print(blockchain.search('A')) # prints block data

## Test Case 4
print(blockchain.search('C')) # prints block data

## Test Case 5
print(blockchain.search('D')) # prints None

## Test Case 6
blockchain.append('')
print(blockchain.search('')) # prints block data

## Test Case 7
blockchain = BlockChain()
print(blockchain.search('A')) # prints None