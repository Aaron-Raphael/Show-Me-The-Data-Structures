# Problem 3

## Time complexity
        Encoding : 
            O(n) loop through each character once in the input
            O(nlogn)generating the code for unique characters
            O(n^2) replacing the charachters in the string

        Decoding :
            O(nlogn) generating decode
            O(n^2) the data is looped decoded and replaced with the match through the length of data

## Space Complexity:
        Encoding
            O(n*log(n)) from the tree 
        Decoding 
            O(n) where n is the length of the string