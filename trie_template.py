class TrieNode():
 def __init__(self):
    self.child = defaultdict(TrieNode)

class Trie():
def __init__(self):
    self.root = TrieNode()
    self.list = []

	def add(self, word):
    node = self.root
    for ch in word:
        node = node.child[ch]
    self.list.append((node, len(word)+1))


 class Solution(object):
 def main(self, words):
    trie  = Trie()
    for word in set(words):
        trie.add(word[::-1])
    ans = 0
    
