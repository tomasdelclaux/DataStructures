class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

class _count:
    def __init__(self):
        self.count1 = 1
        self.count2 = 0
    
def union(llist_1, llist_2):
    # Your Solution Here
    visited = dict()
    largest, shortest = largest_shortest(llist_1, llist_2)
    unionList = LinkedList()
    # Traverse shortest first to reduce space
    shorthead = shortest.head
    node = shorthead
    while node:
        if visited.get(node.value, None):
            visited[node.value].count1 += 1
            unionList.append(node.value)
        else:
            visited[node.value] = _count()
            unionList.append(node.value)
        node = node.next
    # Traverse longest
    largehead = largest.head
    node = largehead
    while node:
        if visited.get(node.value, None):
            visited[node.value].count2 += 1
            if visited[node.value].count2 > visited[node.value].count1:
                unionList.append(node.value)
        else:
            unionList.append(node.value)
        node = node.next
    return unionList

def intersection(llist_1, llist_2):
    # Your Solution Here
    visited = dict()
    interList = LinkedList()
    largest, shortest = largest_shortest(llist_1, llist_2)
    # Traverse short first to reduce space in dictionary
    shorthead = shortest.head
    node = shorthead
    while node:
        if visited.get(node.value):
            visited[node.value].count1 +=1
        else:
            visited[node.value] = _count()
        node = node.next
    # Traverse long
    largehead = largest.head
    node = largehead
    while node:
        if visited.get(node.value):
            visited[node.value].count2 += 1
            if visited[node.value].count2 <= visited[node.value].count1:
                interList.append(node.value)
        node = node.next
    return interList

def largest_shortest(llist_1, llist_2):
    # return largest and shortes list in that order
    if llist_1.size() < llist_2.size():
        shortest = llist_1
        largest = llist_2
    elif llist_1.size() >= llist_2.size():
        shortest = llist_2
        largest = llist_1
    return largest, shortest

def test1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    assert union(linked_list_1,linked_list_2).__str__() == "6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> 3 -> 2 -> 35 -> 65 -> 4 -> 3 -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == "4 -> 6 -> 6 -> 21 -> "

def test2():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,"Hello", "bye"]
    element_2 = [6,32,4,9,6,1,11,21,"hello", "Hello"]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    assert union(linked_list_1,linked_list_2).__str__() == "6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> hello -> Hello -> 3 -> 2 -> 35 -> 65 -> 4 -> 3 -> bye -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == "4 -> 6 -> 6 -> Hello -> "

def test3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [None, None, None]
    element_2 = [None, None]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    assert union(linked_list_1,linked_list_2).__str__() == "None -> None -> None -> "
    assert intersection(linked_list_1,linked_list_2).__str__() == "None -> None -> "

test1()
test2()
test3()