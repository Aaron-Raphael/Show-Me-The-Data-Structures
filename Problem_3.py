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