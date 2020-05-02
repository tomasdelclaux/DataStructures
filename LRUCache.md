# Time and Space Complexity of the LRU Cache

There are two datastructures being used in the LRU cache:

    1- Dictionary to store the values and be able to get them in O(1). This is because every time a value is inserted in the cache it is stored under a key. Hence that value can be retrieved using the key in O(1)

    2- DoublyLinked List. This datastructure is used to keep track of the least_recently used node in the cache, in case it needs to be removed. A queue cannot be used since it is a FIFO structure, and because
        everytime a value is retrieved the position of that value in the queue would have to change so that it is the last one. In order to have this behaviour a double linked list is used, since all nodes
        contain references to next and previous. Then, these nodes can be stored in the dictionary under a key, and then if the DoublyLinkedList needs re-ordering the previous and next node to the one retrieved
        can be updated in O(1) and the node retrieved can be prepended to the head. This now means, that if a node needs to be removed from the cache, it can be dequeued from the tail of the doubly linked list
        since the tail will always be the least recently used node. This is done with the dequeue method. The renew method on the other hand, is ran after getting a value, in order to remove that element from the linked list
        and attach at the head.
    
    All the operations have a O(1) time complexity, but because every value must be stored in a dictionary and doublylinked list the space complexity is O(2n) where n is the size of the cache.
