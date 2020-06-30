'''
3. Huffman Coding

Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding scheme is also lossless meaning that when compressing the data to make it smaller that there is no loss of information. The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman codes can be of any length and does not require a prefix, therefore this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode code for this algorithm. At the basic core it is comprised of building a Huffman tree, encoding the data and lastly decoding the data.

Here is one type of pseudocode for this coding schema:

- Take string and determine the relevant frequencies of the characters
- Builds and sort a list of tuples from lowest to highest frequencies.
- Build the Huffman Tree by assigning a binary code to each letter using shorter codes for the more frequent letters. This is the heart of the Huffman algorithm.
- Trim the Huffman Tree (Remove the frequencies from the previously built tree)
- Encode the text into its compressed form
- Decode the text from its compressed form
'''

import sys

class Node(object):
    def __init__(self, count, ch = None):
        self.child_0 = None
        self.child_1 = None
        self.count = count 
        self.ch = ch

    def __str__(self):
        return "(char: {}, count: {})".format(self.ch, self.count)


def huffman_encoding(data):

    # count frequencies
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char,0) +1
    
    if len(frequency)<2:
        if data == "":
            return "0", Node(1,"")
        else:
            return encode(data, huffman_code(Node(1,data[0]))), Node(1,data[0])

    # make nodes with counts and associated chars
    nodes = {}
    for char in frequency:
        nodes[char] = Node(frequency[char], char)

    # generate Tree
    priority = 1
    node_0 = None
    node_1 = None
    parent_node = None
    while len(nodes)>1:
        change_priority = True
        min_priority = None
        for char in nodes:            
            if nodes[char].count == priority:
                if not node_0:
                    node_0 = nodes[char]
                elif not node_1: 
                    node_1 = nodes[char]
            elif not min_priority or nodes[char].count< min_priority:
                min_priority = nodes[char].count
            
            if node_0 and node_1:
                parent_node = Node(node_0.count + node_1.count,
                                   node_0.ch + node_1.ch)
                parent_node.child_0 = node_0
                parent_node.child_1 = node_1
                nodes[parent_node.ch] = parent_node
                nodes.pop(node_0.ch)
                nodes.pop(node_1.ch)
                node_0 = None
                node_1 = None
                change_priority = False
                break

        if change_priority:
            priority = min_priority
    tree = parent_node

    # generate encoding
    encoding = huffman_code(tree)

    encoded_data = encode(data, encoding)

    return encoded_data, tree

def huffman_code(node , code = ""):
    encoding = {}
    if node:
        if not (node.child_0 or node.child_1):
            if code == "": # case of only one letter
                encoding.update({node.ch: "0"})
            else:
                encoding.update({node.ch: code})
        encoding.update(huffman_code(node.child_0, code + "0"))
        encoding.update(huffman_code(node.child_1, code + "1"))
    return encoding

def encode(data , encoding):
    encoded_data = data
    for char in encoding:
        encoded_data = encoded_data.replace(char, encoding[char])
    return encoded_data
    

def huffman_decode(node , code = ""):
    encoding = {}
    if node:
        if not (node.child_0 or node.child_1):
            if code == "": # case of only one letter
                encoding.update({"0": node.ch})
            else:
                encoding.update({code: node.ch})
        encoding.update(huffman_decode(node.child_0, code + "0"))
        encoding.update(huffman_decode(node.child_1, code + "1"))
    return encoding

def huffman_decoding(data, tree):
    
    encoding = huffman_decode(tree)
    decoded_message = ""
    code = ""
    for c in data:
        code += c
        if code in encoding:
            decoded_message += encoding[code]
            code = ""
    
    return decoded_message


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