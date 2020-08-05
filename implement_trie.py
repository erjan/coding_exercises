#Implement a trie with insert, search, and startsWith methods.

class Trie:
    def __init__(self):
        self.endword = False
        self.children = [None]*26
        
    def insert(self,word):
        curr = self
        for c in word:
            if curr.children[ ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = Trie()
            curr = curr.children[ord(c) - ord('a')]
     
        curr.endword = True
        
    def search(self,word):
        curr =self
        for c in word:
            curr = curr.children[ord(c) - ord('a')]
            if curr == None:
                return False
        if curr.endword:
            return True
        return False
    
    def startsWith(self,prefix):
        curr = self
        for c in prefix:
            curr = curr.children[ord(c)-ord('a')]
            if curr == None:
                return False
        return True 
