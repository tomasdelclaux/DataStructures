import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        data = str(self.timestamp) + str(self.data)
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __str__(self):
        return f"Timestamp: {self.timestamp}\nData: {self.data}\nHash: {self.hash}\nPrevHash: {self.previous_hash}"


class Blockchain:
    def __init__(self):
        self.tail = None
        self.hashMap = dict()

    def append(self, data):
        """ Append a node to the end of the list """
        date = datetime.utcnow()
        if self.tail is None:
            self.tail = Block(date, data, 0)
            self.hashMap[self.tail.hash] = self.tail
            return
        
        lastBlock = self.tail
        previous_hash = lastBlock.hash
        newBlock = Block(date, data, previous_hash)
        self.tail = newBlock
        self.hashMap[self.tail.hash] = self.tail

print("TEST1\n")
bitcoin = Blockchain()
bitcoin.append("Hello")
bitcoin.append("Goodbye")
bitcoin.append("see you later")

print(bitcoin.tail)
previous = bitcoin.hashMap[bitcoin.tail.previous_hash]
print(previous)
print(bitcoin.hashMap[previous.previous_hash])
print("\n")

# ouput should be: Time is going to be different, and is set to UTC

# Timestamp: 2020-04-08 21:32:34.298971
# Data: see you later
# Hash: dfa470b3a06dad85aaad98a137fb382e2637c8ce40d1f5182eb2d7d505155928
# PrevHash: e1ebd3bff59ab494bf629815c0c3df2cf009db057ab1b738f72643465968cd9a
# Timestamp: 2020-04-08 21:32:34.298965
# Data: Goodbye
# Hash: e1ebd3bff59ab494bf629815c0c3df2cf009db057ab1b738f72643465968cd9a
# PrevHash: 3f6310c78d1b56d407f2d75b425aedb0bfb7b0df48375b2faf3f4a737bfc3fab
# Timestamp: 2020-04-08 21:32:34.298839
# Data: Hello
# Hash: 3f6310c78d1b56d407f2d75b425aedb0bfb7b0df48375b2faf3f4a737bfc3fab
# PrevHash: 0

print("TEST2\n")
ether = Blockchain()
ether.append([1,2,3,4,5])
ether.append(dict())
ether.append("weird stuff")

print(ether.tail)
previous = ether.hashMap[ether.tail.previous_hash]
print(previous)
print(ether.hashMap[previous.previous_hash])
print("\n")

# ouput should be: Time is going to be different, and is set to UTC

# Timestamp: 2020-04-08 21:32:34.299016
# Data: weird stuff
# Hash: 32dd0ab57e15bd43f7c6e3c6a0b1ae5d575aa65e7968f271e1c8f942019e92aa
# PrevHash: 0c79006c958961bf0508dddf1abfca4c38dd4070516ff5b645a4acc28049beae
# Timestamp: 2020-04-08 21:32:34.299011
# Data: {}
# Hash: 0c79006c958961bf0508dddf1abfca4c38dd4070516ff5b645a4acc28049beae
# PrevHash: 20157284fa9ad07792c6e89ef8d806632433434073b70e98af2baba2862ee79c
# Timestamp: 2020-04-08 21:32:34.299004
# Data: [1, 2, 3, 4, 5]
# Hash: 20157284fa9ad07792c6e89ef8d806632433434073b70e98af2baba2862ee79c
# PrevHash: 0

print("TEST3\n")
xrp = Blockchain()
xrp.append([1,2,3,4,5])
xrp.append(None)
xrp.append("")

print(xrp.tail)
previous = xrp.hashMap[xrp.tail.previous_hash]
print(previous)
print(xrp.hashMap[previous.previous_hash])
print("\n")

# ouput should be: Time is going to be different, and is set to UTC

# Timestamp: 2020-04-08 21:32:34.299159
# Data: 
# Hash: 60952128711c81d56827dd639e06c4e224e48315dcd7f8f81cf85aafd59f2e31
# PrevHash: a88d659bd16b508d57d0e134bc944d8cd4637875592cd414b5689457fc5e1cca
# Timestamp: 2020-04-08 21:32:34.299150
# Data: None
# Hash: a88d659bd16b508d57d0e134bc944d8cd4637875592cd414b5689457fc5e1cca
# PrevHash: e93aedfad71013070ad5b863f26f81259122a4789793ad613a4cb26bd935ada6
# Timestamp: 2020-04-08 21:32:34.299138
# Data: [1, 2, 3, 4, 5]
# Hash: e93aedfad71013070ad5b863f26f81259122a4789793ad613a4cb26bd935ada6
# PrevHash: 0