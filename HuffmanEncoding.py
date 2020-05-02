import sys

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        # The deepest nodes of the Huffman tree are going to be characters instead of numbers, since they represent the
        # different characters in the string to be compressed
        if type(self.left) is str:
            left = self.left
        elif self.left:
            left = self.left.value
        else:
            left = None
        if type(self.right) is str:
            right = self.right
        elif self.right:
            right = self.right.value
        else:
            right = None
        return (f"""
                value: {self.value}
                left: {left}
                right: {right}
                """)

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def set_left_child(self, node):
        self.left = node
    
    def set_right_child(self, node):
        self.right = node
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None


class Tree:
    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root


# Let's define a stack to help keep track of the tree nodes. Used for pre-order traversal
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"


#Helper class to keep track of the created sub trees and also method to return smallest nodes,
# or uppber bound in case they dont exist
class Branches:
    def __init__(self):
        self.branches = list()
    
    def get2smallest(self):
        # Return tuple of index, value to be able to compare to elements in sorted_freq
        if len(self.branches) >1:
            small_1, small_2 = (0, self.branches[0].value), (1, self.branches[1].value)
        elif len(self.branches) ==1:
            small_1, small_2 = (0, self.branches[0].value), (None, float('inf'))
        else:
            small_1, small_2 = (None, float('inf')), (None, float('inf'))
        return small_1, small_2


def freq(data):
    frequency=dict()
    for character in data:
        if frequency.get(character):
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency


class Huffman:
    def __init__(self):
        self.codes = None
        self.tree = None

    def _get_Huffman(self, data):
        sorted_freq = sorted(freq(data).items(), key=lambda value: value[1])
        created = Branches()

        #in case there is only a single character in the string then map to 1
        if len(sorted_freq) == 1:
            code = dict()
            code[sorted_freq[0][0]] = "1"
            self.codes = code
            return

        while len(sorted_freq) > 0:
            node1 = sorted_freq[0]
            if len(sorted_freq) > 1:
                node2 = sorted_freq[1]
            else:
                node2 = (None, float('inf'))
            elem1, elem2 = created.get2smallest()

            if node2[1] < elem1[1]:
                root = Node(node1[1] + node2[1])
                root.set_left_child(node1[0])
                root.set_right_child(node2[0])
                sorted_freq = sorted_freq[2:]
            elif node1[1] <= elem1[1] and node1[1] < elem2[1]:
                root = Node(node1[1] + elem1[1])
                root.set_left_child(created.branches[0])
                root.set_right_child(node1[0])
                sorted_freq = sorted_freq[1:]
                created.branches.pop(0)
            else:
                root = Node(elem1[1] + elem2[1])
                root.set_left_child(created.branches[0])
                root.set_right_child(created.branches[1])
                created.branches.pop(0)
                created.branches.pop(0)

            created.branches.append(root)

        while len(created.branches) > 1:
            root = Node(created.branches[0].value + created.branches[1].value)
            root.set_left_child(created.branches[0])
            root.set_right_child(created.branches[1])
            created.branches.pop(0)
            created.branches.pop(0)
            created.branches.append(root)

        self.tree = Tree(created.branches[0])
        self.codes = self._get_codes()

    # define in-order traversal function. Stack is used to keep track on the path travelled.
    # When a node with a string is reached, the stack is traversed to get the code.
    def _get_codes(self):
        path = Stack()
        root = self.tree.get_root()
        codes = dict()
        
        if self.codes:
            return
        
        def traverse(node, direction=None):
            if direction == "0":
                path.push("0")
            elif direction == "1":
                path.push("1")
            if node:
                if type(node) is str:
                    codes[node] = self._get_path(path)
                    path.pop()
                else:
                #visit
                    #traverse left
                    traverse(node.get_left_child(), "0")
                    #traverse right
                    traverse(node.get_right_child(), "1")
                    if node != root:
                        path.pop()
        traverse(root)
        return codes

    def _get_path(self, stack):
        path = ""
        i = 0
        while i < len(stack.list):
            value = stack.list[i]
            path += value
            i +=1
        return path

def huffman_encoding(data):
    if data == "":
        return "0", None
    HuffmanTree = Huffman()
    HuffmanTree._get_Huffman(data)
    codes = HuffmanTree.codes
    encoded = ""
    for char in data:
        encoded += codes[char]
    return encoded, HuffmanTree

def huffman_decoding(data,tree):
    if data == "" or tree == None:
        return ""
    codes = tree.codes
    decoded = ""
    i = len(data)
    while len(data) > 0 and i >0:
        i -= 1
        for k,v in codes.items():
            if data.startswith(v):
                decoded += k
                data = data[len(v):]
    return decoded

if __name__ == "__main__":
    print("Test Case 1: The bird is the word")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test Case 2: All those moments will be lost in time like tears in rain")
    another_great_sentence = "All those moments will be lost in time like tears in rain"

    print ("The size of the data is: {}\n".format(sys.getsizeof(another_great_sentence)))
    print ("The content of the data is: {}\n".format(another_great_sentence))

    encoded_data, tree = huffman_encoding(another_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test Case 3: 2+2 = 4 or does it?")
    weird_sentence = "2+2 = 4 or does it?"

    print ("The size of the data is: {}\n".format(sys.getsizeof(weird_sentence)))
    print ("The content of the data is: {}\n".format(weird_sentence))

    encoded_data, tree = huffman_encoding(weird_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test Case 4: empty string")
    weird_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(weird_sentence)))
    print ("The content of the data is: {}\n".format(weird_sentence))

    encoded_data, tree = huffman_encoding(weird_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test Case 5: 1 character")
    weird_sentence = "aaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(weird_sentence)))
    print ("The content of the data is: {}\n".format(weird_sentence))

    encoded_data, tree = huffman_encoding(weird_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test Case 6: Long string")
    weird_sentence = "Once upon a time there was a spaceship that ruled the world etc, lorem ipsum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(weird_sentence)))
    print ("The content of the data is: {}\n".format(weird_sentence))

    encoded_data, tree = huffman_encoding(weird_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))