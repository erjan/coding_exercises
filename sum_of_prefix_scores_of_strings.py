'''
You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        for word in words:
            node = self.root
            for l in word:
                if not l in node.children:
                    node.children[l] = TrieNode()
                node = node.children[l]
                node.count+=1
        res = []
        for word in words:
            node = self.root
            count = 0
            for i, l in enumerate(word):
                node = node.children[l]
                count+= node.count
                if node.count == 1:
                    count+= len(word) - (i+1)
                    break
            res.append(count)
        return res
      
------------------------------------------------------------------------------------------------
class Node:

    def __init__(self, label=None):

        self.label = label  
        self.count = 0
        self.children = {}

class Trie:

    def __init__(self):

        self.root = Node()

    def insert(self, word):

        trie = self.root

        for c in word:

            if c not in trie.children:

                trie.children[c] = Node(c)

            trie.children[c].count += 1
            trie = trie.children[c]

    def get_word_scores(self, word):

        trie = self.root
        count = 0

        for c in word:

            count += trie.children[c].count
            trie = trie.children[c]
            
        return(count)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()

        for word in words:

            trie.insert(word)

        word_scores = []

        for word in words:

            word_scores.append(trie.get_word_scores(word))

        return(word_scores)
      
---------------------------------------------------------------------------------------------------------      
