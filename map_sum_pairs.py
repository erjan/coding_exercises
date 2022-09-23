'''
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
'''


class MapSum:

    def __init__(self):
        self.d = dict()
        

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val
        

    def sum(self, prefix: str) -> int:
        res = 0
        
        for k,v in self.d.items():
            if k.startswith(prefix):
                res+=v
        return res
-------------------------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.value = 0
        
class MapSum:
    def __init__(self):
        self.t = TrieNode()
        self.m = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.m.get(key,0)
        self.m[key] = val
        node = self.t
        for char in key:
            node = node.children[char]
            node.value += delta
        
    def sum(self, prefix: str) -> int:
        node = self.t
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return 0
        return node.value
      
---------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefixCount = 0
        
        
class MapSum:  

    def __init__(self):
        self.root = TrieNode()
        self.dic = {}

    def insert(self, key: str, val: int) -> None: 
        delta = val
        if key in self.dic:     # key already existed, the original key-value pair will be overridden to the new one. And val - self.dic[key] does this thing
            delta = val - self.dic[key]
        self.dic[key] = val
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.prefixCount += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        return cur.prefixCount
      
--------------------------------------------------------------------------------------------------------------------------
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        root = self.root
        for w in key:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["-"] = val
        
    def get_siblings(self,prefix):
        root = self.root
        for w in prefix:
            if w not in root:
                return None
            root = root[w]
        return root
    
    def get_sum(self,root):
        cost = 0
        for w in root:
            if w == "-":
                cost+=root[w]
                continue
            cost+=self.get_sum(root[w])
        return cost
 
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        root = self.get_siblings(prefix)
        if root: return self.get_sum(root)
        return 0
