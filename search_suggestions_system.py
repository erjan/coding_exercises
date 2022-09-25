'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
'''


class TreeNode:
    def __init__(self):
        self.children = [None]*26
        self.words = []
class Trie:
    def __init__(self):
        self.root = TreeNode()
    def _getIndex(self,ch):
        return ord(ch)-ord('a')
    def insert(self,word):
        cur_node = self.root
        for ch in word:
            index = self._getIndex(ch)
            if cur_node.children[index] is None:
                cur_node.children[index] =TreeNode()
            cur_node = cur_node.children[index]
            cur_node.words.append(word)
        return
    def search(self,word):
        cur_node = self.root
        for ch in word:
            index = self._getIndex(ch)
            if cur_node.children[index] is None:
                return False
            cur_node = cur_node.children[index]
        return cur_node.words
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for word in products:
            root.insert(word)
        res = []
        for i in range(len(searchWord)):
            tmp = root.search(searchWord[:i+1])
            if tmp:
                res.append(sorted(tmp)[:3])
            else:
                res.append([])
        return res
      
-------------------------------------------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c] 
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c] 
        return node.words
            
class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        A.sort()
        trie = Trie()
        for word in A: trie.add_word(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c 
            ans.append(trie.find_word_by_prefix(cur))
        return ans    
