import sys
from collections import Counter
import heapq as hq


class Node:
    def __init__(self, char, freq, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, next_node): 
        return self.freq < next_node.freq 


class HuffmanTree:
    def __init__(self, data):
        if not data:
            self.root = None
            self.code_table = {}
        else:
            self.root, self.code_table = self.__huffman_code(data)

    # Function to build the huffman tree using a min heap, returns the tree root and code table
    def __huffman_code(self,data):
        char_count = Counter(data)
        nodes = []

        for x in char_count:
            hq.heappush(nodes,Node(char=x,freq=char_count[x]))

        if len(nodes) == 1:
            hq.heappush(nodes, Node(char=None, freq=0))

        while len(nodes) > 1:
            left = hq.heappop(nodes)
            right = hq.heappop(nodes)
            new_node = Node(freq = left.freq + right.freq, 
                            char = None, 
                            left = left, 
                            right = right
                            )
            hq.heappush(nodes, new_node)

        root = nodes[0]
        code_table = {}
        self.__build_code_table(root, "", code_table)
        return root, code_table

    # Traverse the huffman tree building the code table to convert letters to binary values
    def __build_code_table(self, node, current_code, table):
        if node is None:
            return
        if node.char is not None:
            table[node.char] = current_code
            return
        self.__build_code_table(node.left, current_code + "0", table)
        self.__build_code_table(node.right, current_code + "1", table)


    # Builds Binary string using the code table
    def encode(self, data):
        return ''.join([self.code_table[char] for char in data])


    # Converts binary string back into letters traversing the tree
    # Digit 0 indicates left traversal and digit 1 indicates right traversal
    # Once reaching a leaf node add the letter to the string, return to root.
    def decode(self, data):
        if not self.code_table:
            return ''

        cur_node = self.root
        decoded = ""
        for bit in data:
            if bit == '0':
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            if cur_node.char:
                decoded += cur_node.char
                cur_node = self.root
        return decoded
        

def huffman_encoding(data):
    if not data:
        return '', HuffmanTree('')
    tree = HuffmanTree(data)
    return tree.encode(data), tree


def huffman_decoding(data,tree):
    return tree.decode(data)


    

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1: Empty String
test_case_1 = ""
encoded_data, tree = huffman_encoding(test_case_1)
decoded_data = huffman_decoding(encoded_data, tree)
assert test_case_1 == decoded_data
print(f"Test Case 1 - Original: {test_case_1} | Encoded: {encoded_data} | Decoded: {decoded_data}")

# Test Case 2: String with Single Repeated Character
test_case_2 = "aaaaaaa"
encoded_data, tree = huffman_encoding(test_case_2)
decoded_data = huffman_decoding(encoded_data, tree)
assert test_case_2 == decoded_data
print(f"Test Case 2 - Original: {test_case_2} | Encoded: {encoded_data} | Decoded: {decoded_data}")

# Test Case 3: Conceptual Large String
test_case_3 = "The quick brown fox jumps over the lazy dog" * 100  # repeating for demonstration
encoded_data, tree = huffman_encoding(test_case_3)
decoded_data = huffman_decoding(encoded_data, tree)
assert test_case_3 == decoded_data
print(f"Test Case 3 - Original (first 50 chars): {test_case_3[:50]}... | Encoded (first 50 bits): {encoded_data[:50]}... | Decoded (first 50 chars): {decoded_data[:50]}...")