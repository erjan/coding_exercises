'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
'''

class Node:
    def __init__(self, elements=[]):
        self.left = None
        self.right = None
        self.elements = set(elements)

    def addBetween(self, node1, node2):
        self.left = node1
        self.right = node2

        node1.right = self
        node2.left = self
    
    def deleteNode(self):
        left, right = self.left, self.right
        left.right = right
        right.left = left
            
			
class AllOne:
    def __init__(self):
        self.keyToNum = {}
        self.numToNode = {}
        
        self.head, self.tail = Node(), Node()
        self.head.right = self.tail
        self.tail.left = self.head
        
    def inc(self, key: str) -> None:
        keyToNum = self.keyToNum
        numToNode = self.numToNode

        if key not in keyToNum:
            keyToNum[key] = 1
            if 1 in numToNode:
                numToNode[1].elements.add(key)
            else:
                newNode = Node([key])
                numToNode[1] = newNode
                newNode.addBetween(self.head, self.head.right)                
        else:
            oldNum = keyToNum[key]
            oldNode = numToNode[oldNum]
            
            newNum = oldNum + 1
            keyToNum[key] = newNum

            if newNum in numToNode:
                numToNode[newNum].elements.add(key)
            else:
                newNode = Node([key])
                numToNode[newNum] = newNode
                newNode.addBetween(oldNode, oldNode.right)
            
            oldNode.elements.discard(key)
            if not oldNode.elements:
                oldNode.deleteNode()
                del numToNode[oldNum]

    def dec(self, key: str) -> None:
        keyToNum = self.keyToNum
        numToNode = self.numToNode
        
        if key not in keyToNum:
            return
        
        oldNum = keyToNum[key]
        oldNode = numToNode[oldNum]
        
        if oldNum == 1:
            del keyToNum[key]
        else:
            newNum = oldNum - 1
            keyToNum[key] = newNum
			
            if newNum in numToNode:
                newNode = numToNode[newNum]
                newNode.elements.add(key)
            else:
                newNode = Node([key])
                numToNode[newNum] = newNode
                oldLeft = oldNode.left
                newNode.addBetween(oldLeft, oldNode)
                
        oldNode.elements.discard(key)
        if not oldNode.elements:
            oldNode.deleteNode()
            del numToNode[oldNum]

    def getMaxKey(self) -> str:
        if self.tail.left == self.head:
            return ''
        else:
            for e in self.tail.left.elements:
                return e

    def getMinKey(self) -> str:
        if self.head.right == self.tail:
            return ''
        else:
            for e in self.head.right.elements:
                return e
              
-----------------------------------------------------------------------------------------------------
class Block(object):
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None

    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    def insert_after(self, new_block):
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block


class AllOne(object):
    def __init__(self):
        self.begin = Block()  # sentinel
        self.end = Block()  # sentinel
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {}  # key to block

    def inc(self, key):
        if not key in self.mapping:  # find current block and remove key
            current_block = self.begin
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        if current_block.val + 1 != current_block.after.val:  # insert new block
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.after

        new_block.keys.add(key)  # update new_block
        self.mapping[key] = new_block  # ... and mapping of key to new_block

        if not current_block.keys and current_block.val != 0:  # delete current block if not seninel
            current_block.remove()

    def dec(self, key):
        if not key in self.mapping:
            return

        current_block = self.mapping[key]
        del self.mapping[key]  # could use self.mapping.pop(key)
        current_block.keys.remove(key)

        if current_block.val != 1:
            if current_block.val - 1 != current_block.before.val:  # insert new block
                new_block = Block(current_block.val - 1)
                current_block.before.insert_after(new_block)
            else:
                new_block = current_block.before
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not current_block.keys:  # delete current block
            current_block.remove()

    def getMaxKey(self):
        if self.end.before.val == 0:
            return ""
        key = self.end.before.keys.pop()  # pop and add back to get arbitrary (but not random) element
        self.end.before.keys.add(key)
        return key

    def getMinKey(self):
        if self.begin.after.val == 0:
            return ""
        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key
