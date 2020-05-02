# Simple Blockchain implementation using Linked Lists -- Time and Space Complexity

Two classes are used Block and Blockchain. This last one is a linked list, where every time a new node or block is added to the linked list, it is appended and the tail and hashmap updated.
The hashmap is used to store a mapping between previous hashes and the block instance itself.

Inside the Block class, the timestamp is set to the time of class instance creation in UTC. The hash value is calculated  using the data in the block.

The add a new block to the linked list can be done in O(1) time. The traversal from the tail of the head can be done in O(n) since nodes only contain a reference to a previous hash, which is mapped
in a dictionary to the actual block. To avoid hash collisions, the timestamp and the data are used as input into the hash, since two blocks cannot be created at the same time and contain the same data.

The space complexity is O(n) where n is the number of block in the chain