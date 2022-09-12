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
---------------------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, val= 0):
        self.val = val
        self.next = None
        self.pre = None
        self.arr = set()


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.pre = self.tail, self.head
        self.d = {}
        
    def move_forward(self, node, key):
        if node.val+1 != node.next.val:
            newNode = Node(node.val+1)
            newNode.pre, newNode.next = node, node.next
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.next
        newNode.arr.add(key)
        return newNode
    
    def pre(self, node, key):
        if node.val-1 != node.pre.val:
            newNode = Node(node.val-1)
            newNode.pre, newNode.next = node.pre, node
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.pre
        newNode.arr.add(key)
        return newNode

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.d:
            node = self.head
        else:
            node = self.d[key]
            node.arr.discard(key)
            
        self.d[key] = self.move_forward(node, key)
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key in self.d:
            node = self.d[key]
            node.arr.discard(key)
            if node.val != 1:
                self.d[key] = self.pre(node, key)
            else:
                del self.d[key]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        node = self.tail.pre
        while node and len(node.arr) == 0:
            node = node.pre
        
        if not node:
            return ""
        
        val = node.arr.pop()
        node.arr.add(val)
        return val
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        node = self.head.next
        while node and len(node.arr) == 0:
            node = node.next
        if not node:
            return ""
        
        val = node.arr.pop()
        node.arr.add(val)
        return val
----------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, val):
        self.next = None
        self.pre = None
        self.val = val
        self.data = set()


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.pre = self.tail, self.head
        self.memo = {}
        
    def add(self, node, key):
        if node.val+1 != node.next.val:
            newNode = Node(node.val+1)
            newNode.pre, newNode.next = node, node.next
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.next
        
        newNode.data.add(key)
        return newNode
    
    def add_prev(self, node, key):
        if node.val-1 != node.pre.val:
            newNode = Node(node.val-1)
            newNode.pre, newNode.next = node.pre, node
            newNode.pre.next = newNode.next.pre = newNode
        else:
            newNode = node.pre
        newNode.data.add(key)
        return newNode
        
    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.memo:
            self.memo[key] = self.add(self.head, key)
        else:
            node = self.memo[key]
            self.memo[key] = self.add(node, key)
            node.data.remove(key)
            if not node.data:
                node.pre.next, node.next.pre = node.next, node.pre
                node.next = node.pre = None

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key in self.memo:
            node = self.memo[key]
            node.data.remove(key)
            del self.memo[key]
            if node.val > 1:
                self.memo[key] = self.add_prev(node, key)
            if not node.data:
                node.pre.next, node.next.pre = node.next, node.pre
                node.next = node.pre = None
                

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.tail.pre.data:
            return ""
        num = self.tail.pre.data.pop()
        self.tail.pre.data.add(num)
        return num

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.head.next.data:
            return ""
        num = self.head.next.data.pop()
        self.head.next.data.add(num)
        return num
