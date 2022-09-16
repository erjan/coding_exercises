'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 
'''

def longestWord(self, words: List[str]) -> str:
    #sort the words, then keep in the set and check for nextWord[:-1] in the set
    words.sort()
    st, res = set(), "" #res == result
    st.add("")
    for word in words:
        if word[:-1] in st:
            if len(word) > len(res):
                res = word
            st.add(word)
    
    return res
  
--------------------------------------------------------

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None  # Record the built word for the current node
        self.length = 0  # Record the continue length of the build word

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_length = -1  # the max length of the word in the entire words list
        self.word = None  # the resulting word
    
    def insert(self, word):
        current = self.root
        word_length = 1
        for letter in word:
            if current.word:
                word_length += 1
            else:
                # Reset length if one character is skipped
                word_length = 1
            current = current.children[letter]
        current.word = word
        current.length = word_length if word_length == len(word) else 1
        
        if current.length > self.max_length:
            self.max_length = current.length
            self.word = word
        elif current.length == self.max_length:
            self.word = min(word, self.word)
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        tree = Trie()
        [tree.insert(word) for word in sorted(words)]  # Have to sort to make sure the word is built in order
        
        return tree.word
      
------------------------------------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.val = ''           # to define the value of end node as word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        cur.val = word     # definging the end value as whole word
    
    def bfs(self):         # as I am starting from the root itself, so bfs have only argument self for referring the root
        q = [self.root]
        res = ''
        while q:
            cur = q.pop(0)
            for child in cur.children.values():     # traversing all the nodes of cur not keys
                if child.endOfWord:                 # ONLY go to the node which is of length 1 and end of a word also
                    q.append(child)
                    if len(child.val) > len(res):   # for greater length as for lexicografical I have already sorted words 
                        res = child.val
        return res
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()        # sort in lexicografical order
        trie = Trie()       # making object of the Trie Class
        for word in words:  # adding all words to trie structre
            trie.addWord(word)
        
        return trie.bfs()   # calling the bfs function 
  
