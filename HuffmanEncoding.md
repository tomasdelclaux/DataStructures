# Huffman Tree Encoding In Depth Time and Space Complexity Analysis

The main part of this problem consists of building a binary tree and then traversing the tree to obtain the codes (every left traversal is a 0 and every right traversal is a 1)
For the Huffman tree a binary was selected as the datastructure. In order to build this tree a node class was made, that contained left, right and value attributes.

For the deepest nodes in the tree, that represent the characters, it was decided to set the value to the character instead of the frequency. The reason for this, is that the
frequency is no longer needed for that node since it has already been aggregated. On the other hand, if we set to the character, when traversing the tree, it can easily be told
if the node is a character representing node, since its value will be a string and not an int, as the other nodes in the tree.

The first step in the algorithm is to produce a dictionary, where a key is assigned for each unique character in the string to be encoded and the value is the number of times this 
character appears in the data. To build this dictionary a traversal of all the characters in the string was done. This has a time complexity of O(n).

This dictionary then has to be sorted in from least repeated keys to the most. This was done using the sorted function with a time complexity of O(nlogn). The result is a list of tuples,
where the first value is the character and the second its frequency. This list will hence take a space complexity of O(2n), since for every value the frequency must also be stored.

A helper class branches, which is a list, was created in order to keep track of the created subtrees as nodes of the tree start to be created and aggregated. The algorithm consists of always 
selecting the two smallest nodes from both the sorted_frequency list of tuples and the created subtrees in the branches classes, until there is only one tree created.

In order to achieve this, two while loops are used, the first one runs until all the values in the list of tuple have been aggregated, and the second until all the subtrees have been aggregated.
Every time a node is aggregated into a tree, it is popped from either the tuples list or the branches list. Consequently, since the aggregation of two elements creates a new subtree, this is also 
added to the branches list per iteration. Since, elements are being moved from one datastructure (list of tuples to the list of subtrees) and used elements are popped, the space complexity stays 
the same as before.

The get2smallest functions in the branches classes returns the first two subtrees in the branches, as these are always going to be the smallest. If they dont exists it returns a tuple of (None, float('inf)).
By setting an upperbound limit to an element in case it does not exists, means it can be compared to other elements, simplifying the if/elif conditions, as the None case does not to be considered.

The worst case time complexity of the tree generation would happen if the all the characters have the same frequency. Thus, the first while loop would iterate over all the elements of the sorted frequencies,
aggregating two nodes each time and appending them to the branches list. Then the branches list would be iterated over in the second while loop, but this would only contain half the nodes. Thus the time complexity
for this process is O(n+n/2)

Finally, once the tree is produced it must be traversed using DFS traversal. A stack is used to keep track of the links travelled. A recursive function is used to travel to all the nodes. Every time it traverses
left a 0 is added to the stack and every time it traverses right a 1 is added to the stack. In the function and if condition is placed to catch when a node containing a character is arrived to, and then stack is
traversed to get the code for that character which is mapped to the character in a dictionary stored as an attribute of the Huffman class. The maxim number of parent nodes a node can have in a binary tree is n-2.
Hence the wosrt case space and time complexity of the stack traversal is O(n-2).

Finally, once the codes are obtained, in order to encode, the data must be tranversed and for every character its code must be found in the codes dictionary. The lookup in the dictionary takes O(1) and the traversal
of the data is O(n). The decoding process is done using the same dictionary, but the dictionary must be traversed in O(n) to see if a value in the dictionary matches the starting characters of the encoded data. If they
do, that slice is converted back and removed, and the process continues until there is no more encoded string. Since the encoded string is shortened every time the start of it is decoded, it can be assumed an average
time complexity of (On/2). Thus, for the decoding the total time complexity can be calculated as O(n/2) * O(n) = O(n^2/2).

Summary of time and space comlexities:

Enconding:

1 - Create dictionary with counts => Time: O(n)  Space: O(n)
2 - Sort dictionary into list of frequency tuple => Time: O(nlogn) Space: O(n)
3 - Create tree => Time: O(n+n/2) Space: O(n)
4 - Traverse the tree to get the trees => Time: O(n-2)~=O(n)  Space: O(n-2)
5 - Encode => Time: O(n) Space: O(n)

- Total time complexity of encoding is O(4n+nlogn+n/2)  == > O(nlogn)

Total space complexity is not the total of all the space complexities, since not all data structures are permanently stored inside the Huffman class. In fact, worst case at the same time, the stack with space complexity of O(n-2), the codes dictionary
with space complexity of O(n) and the tree which has a space complexity of O(2n-1), having a total of O(4n-2)

Decoding:

*- Using codes already produced in encoding
1- Decoding => Time: O(n^2/2) Space: Same as encoding, since same data is stored.

