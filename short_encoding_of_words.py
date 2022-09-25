'''
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
'''



class Solution:
    def minimumLengthEncoding(self, W: List[str]) -> int:
        wset = set(W)
        for word in W:
            if word in wset:
                for i in range(1,len(word)):
                    wset.discard(word[i:])
        return len("#".join(list(wset))) + 1
      
----------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getTrieNode()
    
    def getTrieNode(self):
        return TrieNode()
    
    def insert(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = self.getTrieNode()
            root = root.children[ch]
        root.endOfWord = True
    
    def isNotPrefix(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                return True
            root = root.children[ch]
        return len(root.children) == 0
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        words = set(words)
        
        for word in words:
            trie.insert(word[::-1])
                
        encodingLen = 0
        for word in words:
            encodingLen += len(word)+1 if trie.isNotPrefix(word[::-1]) else 0
        
        return encodingLen
