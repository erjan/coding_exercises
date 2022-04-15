'''
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase 
English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and 
returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
'''


from collections import defaultdict
class FileSystem(object):
    def __init__(self):
        self.path2value = defaultdict(int)
        self.path2value[''] = -1

    def createPath(self, path, value):
        dirs = path.split('/')
        parent = '/'.join(dirs[:-1])
        if path in self.path2value or parent not in self.path2value:
            return False
        self.path2value[path] = value
        return True

    def get(self, path):
        if path in self.path2value:
            return self.path2value[path]
        return -1
      
      
---------------------------
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        self.value = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, path, value):
        cur_node = self.root
        directories = path.split('/')[1:]
        for d in directories[:-1]:
            if d not in cur_node.children:
                return False
            cur_node = cur_node.children[d]            
        cur_node = cur_node.children[directories[-1]]
        if not cur_node.isWord:
            cur_node.isWord = True
            cur_node.value = value
            return True
        return False
            
    def search(self, path):
        cur_node = self.root
        directories = path.split('/')[1:]
        for d in directories:
            if d not in cur_node.children:
                return -1
            cur_node = cur_node.children[d]
        if cur_node.isWord:
            return cur_node.value
        return -1
    
class FileSystem:
    def __init__(self):
        self.trie = Trie()
        
    def createPath(self, path: str, value: int) -> bool:
        return self.trie.insert(path, value)

    def get(self, path: str) -> int:
        return self.trie.search(path)
      
      
-----------------------------
class TrieNode:
    def __init__(self, value=0):
        self.next = dict()
        self.value = value


class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/":  # invalid path
            return False

        folders = path.split("/")[1:]  # the first element is an empty string
        node = self.root

        for i, f in enumerate(folders):
            if f not in node.next:
                if i != len(folders) - 1:  # the parent path doesn't exist
                    return False
                # successfully create the new path
                node.next[f] = TrieNode(value)
                return True
            node = node.next[f]

        return False  # the path already exists

    def get(self, path: str) -> int:
        folders = path.split("/")[1:]
        node = self.root

        for i, f in enumerate(folders):
            if f not in node.next:  # the path doesn't exist
                return -1
            node = node.next[f]

        return node.value
