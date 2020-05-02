#!/usr/bin/python3

# Create Doubly Linked List Class that the Cache will use

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def prepend(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.size += 1
            return      

        self.head.previous = node
        node.next = self.head
        node.previous = None
        self.head = node
        self.size += 1
        return
    
    def renew(self, node):
        if node == self.tail:
            node.previous.next = None
            newTail = node.previous
            self.tail = newTail
            node.previous = None
            node.next = self.head
            self.head.previous = node
            self.head = node 
            return
        elif node == self.head:
            return
        head = self.head
        node.previous.next = node.next
        node.next.previous = node.previous
        self.prepend(node)
        self.size -= 1
        return
    
    def dequeue(self):
        if self.size > 1:
            oldTail = self.tail
            newTail = self.tail.previous
            oldTail.previous = None
            self.tail = newTail
            self.tail.next = None
            self.size -= 1
            return oldTail
        else:
            return
    
    def __str__(self):
        return f"Head: {self.head}\nTail: {self.tail}\nSize: {self.size}"

class DoubleNode:
    def __init__(self, value, key):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        after = self.next
        before = self.previous
        if after:
            nvalue = after.value
        else:
            nvalue = None
        if before:
            pvalue = before.value
        else:
            pvalue = None
        return f"Value: {self.value}\n      Next: {nvalue}\n      Previous: {pvalue}"


# Create LRU class

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity
        self.freeSpace = capacity
        self.cache = dict()
        self.LRU = DoublyLinkedList()
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cache.get(key):
            #no renew if only one element in cache
            if self.freeSpace != self.size -1:
                self.LRU.renew(self.cache.get(key))
            return self.cache.get(key).value
        else:
            return -1

    def set(self, key, value):
        if self.size <= 0:
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.freeSpace > 0:
            self._insert(key, value)
        else:
            removedNode = self.LRU.dequeue()
            self.cache.pop(removedNode.key)
            self.freeSpace +=1
            self._insert(key,value)       
    
    def _insert(self, key, value):
        self.cache[key] = DoubleNode(value, key)
        self.freeSpace -= 1
        self.LRU.prepend(self.cache[key])
    
        
    def __str__(self):
        return f"Values in Cache {self.cache}\n Fresspace {self.freeSpace}\n LRU {self.LRU}\n"


def test1():
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1
    assert our_cache.get(2) == 2
    assert our_cache.get(9) == -1
    our_cache.set(5,5)
    our_cache.set(6, 6)
    assert our_cache.get(3) == -1

def test2():
    # Weird values
    our_cache = LRU_Cache(5)
    our_cache.set(1, "Hello World")
    our_cache.set(2, [1,2,3])
    our_cache.set(3, dict())
    our_cache.set("Hello", "Bye")
    assert our_cache.get(1) == "Hello World"
    assert our_cache.get(2) == [1,2,3]
    assert our_cache.get(9) == -1
    assert our_cache.get(3) == dict()
    assert our_cache.get("Hello") == "Bye"
    our_cache.set(5,5)
    our_cache.set(6, 6)
    assert our_cache.get(1) == -1 

def test3():
    # Large values
    our_cache = LRU_Cache(5)
    our_cache.set(1, "Hello World")
    our_cache.set(2, [1]*100)
    our_cache.set(3, None)
    # string of 4096
    our_cache.set("Novel", "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")
    assert our_cache.get(1) == "Hello World"
    assert our_cache.get(2) == [1]*100
    assert our_cache.get(8) == -1
    assert our_cache.get(3) == None
    assert our_cache.get("Novel") == "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"
    our_cache.set(8, None)
    our_cache.set(9, None)
    assert our_cache.get(1) == -1

def test4():
    #empty cache
     our_cache = LRU_Cache(5)
     assert our_cache.get(2) == -1


def test5():
    our_cache = LRU_Cache(10)
    our_cache.set(1,1)
    assert our_cache.get(1) == 1

def test6():
    our_cache = LRU_Cache(0)
    our_cache.set(1,1)
    assert our_cache.get(1) == -1

test1()
test2()
test3()
test4()
test5()
test6()