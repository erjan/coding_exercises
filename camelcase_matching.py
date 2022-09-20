'''
Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. You may insert each character at any position and you may not insert any characters.
'''


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def match(p, q):
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == q[j]: i += 1
                elif q[j].isupper(): return False
            return i == len(p)
        
        return [True if match(pattern, s) else False for s in queries]
      
-------------------------------------------------------------------------------      


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, pattern):
        current = self.root
        p_index = 0
        follow_pattern = True
        for letter in word:
            if p_index < len(pattern) and letter == pattern[p_index]:
                p_index += 1
            elif p_index < len(pattern) and letter.isupper() and letter != pattern[p_index]:
                # Case for "ForceFeedBack" and "FB" as pattern
                follow_pattern = False
            elif p_index == len(pattern) and letter.isupper():
                # Case for "FooBarTest" and "FB" as pattern
                follow_pattern = False
            current = current.children[letter]
        current.word = word

        return follow_pattern and p_index == len(pattern)

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        tree = Trie()
        return [tree.insert(word, pattern) for word in queries]
