'''
Given an array of strings words, find the longest string in words such that every prefix of it is also in words.

For example, let words = ["a", "app", "ap"]. The string "app" has prefixes "ap" and "a", all of which are in words.
Return the string described above. If there is more than one string with the same length, return the lexicographically smallest one, and if no string exists, return "".

 

Example 1:

Input: words = ["k","ki","kir","kira", "kiran"]
Output: "kiran"
Explanation: "kiran" has prefixes "kira", "kir", "ki", and "k", and all of them appear in words.
Example 2:

Input: words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: Both "apple" and "apply" have all their prefixes in words.
However, "apple" is lexicographically smaller, so we return that.
Example 3:

Input: words = ["abc", "bc", "ab", "qwe"]
Output: ""
'''


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.string = ''

class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = Node()
        self.ans = ''
        for word in words:
            self.insert(word)
        for word in words:
            self.find(word)
        return self.ans
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.string = word
    
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            if not node.string:
                return
        if len(word) > len(self.ans):
            self.ans = word
        elif len(word) == len(self.ans) and word < self.ans:
            self.ans = word
-------------------------------------------------------------------------------

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
    
    def addWord(self, word):
        root = self
        for ch in word:
            root = root.children.setdefault(ch, TrieNode())
        root.end = True
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        for word in words:
            self.root.addWord(word)
        res = ""
        for word in words:
            if self.allPrefixExist(word, self.root):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(word, res)
        return res
        
    def allPrefixExist(self, word, node):        
        for ch in word:
            node = node.children[ch]
            if not node.end:
                return False
        return True
-----------------------------------------------------------

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key=lambda x:(len(x), x))
        good = set([""])
        result = ""
        
        for word in words:
            pre = word[:-1]
            if pre in good:
                good.add(word)
                if len(word) > len(result):
                    result = word
        
        return result
------------------------------------------------------------------


Solution sketch
Two steps: (1) Implement a trie (2) Travese the trie and find the longest path where all the nodes are valid words.

step 1 is leet code 208. So moving forward we are assuming that is a given. I simply copied my solution for lc 208, so the whole answer is pretty long.
step 2 is a bit tricky. I used an implementation involving backtracking:

2.1 It is worth noting that, the teminating conditioning is not exactly that we are in the bottom of tree. We could stop anywhere, or more specifically, the first ocurrence where the word is not in the give words set. So we go deeper whenever the current path + next char is in the word list, otherwise we stop and record the current path and backtrack.
2.2 After this, we get a set of possible answers, we then sort them based on (1) length of that word and (2) alphabetical order.
Code

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def startsWith(self, prefix):
        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return True

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node.is_word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = []

        def traverse(node, path):
            nonlocal result
            if not node.children:
                result.append(''.join(path))
                return None

            for next_value in node.children:
                if ''.join(path) + next_value in words:
                    path.append(next_value)
                    traverse(node.children[next_value], path)
                    path.pop()
                else:
                    result.append(''.join(path))

        traverse(trie.root, path=[])
        if result:
            result.sort(key=lambda x: (-len(x), x))
            return result[0]
        return ''

-------------------------------------------------------------

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        max_len = 0
        seen = set()
        
        for word in words:
            if len(word) == 1 or word[:len(word)-1] in seen:
                if len(word) > max_len:
                    max_len = len(word)
                    ans = word
                seen.add(word)
        return ans
--------------------------------------

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)        
        longest = ""
        for w in words:
            for i in range(len(w)):
                if w[:i+1] not in words:
                    break
            else:
                if len(w) > len(longest) or len(w) == len(longest) and w < longest:
                    longest = w
                    
        return longest
      
      
      
      
            
