'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie.
 
 
 '''
 
 
 
 
 A slightly modification based on basic Trie implementation.

cnt_start_with: count all words has the same prefix
cnt: count only the exact word
Implementation
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.cnt = 0
        self.cnt_start_with = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]    
            node.cnt_start_with += 1    
        node.cnt += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.cnt    
            
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.cnt_start_with
        

    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
            node.cnt_start_with -= 1
        node.cnt -= 1
        
------------------------------------------------------------------------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.charCount = 0
        self.wordCount = 0
        self.child = {}
        

class Trie:

    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.child:
                root.child[ch] = Node(ch)
            root = root.child[ch]
            root.charCount += 1
        root.wordCount += 1
        
        
    def countWordsEqualTo(self, word: str) -> int:
        root = self.root
        for ch in word:
            if ch not in root.child:
                return 0
            root = root.child[ch]
        return root.wordCount
        
        
        

    def countWordsStartingWith(self, prefix: str) -> int:
        root = self.root
        for ch in prefix:
            if ch not in root.child:
                return 0
            root = root.child[ch]
        return root.charCount
        

    def erase(self, word: str) -> None:
        root = self.root
        for ch in word:
            root = root.child[ch]
            root.charCount -= 1
        root.wordCount -= 1
--------------------------------------------------------------

class TrieNode:
		def __init__(self):
				self.wordCounter = 0
				self.prefixCounter = 0
				self.children = {}


class Trie:

		def __init__(self):
				self.root = TrieNode()

		def insert(self, word: str) -> None:
				current = self.root
				current.prefixCounter += 1

				for c in word:
						if c in current.children:
								current = current.children[c]
								current.prefixCounter += 1
						else:
								current.children[c] = TrieNode()
								current = current.children[c]
								current.prefixCounter += 1

				current.wordCounter += 1

		def countWordsEqualTo(self, word: str) -> int:
				current = self.root
				for c in word:
						if c not in current.children:
								return 0
						else:
								current = current.children[c]

				return current.wordCounter


		def countWordsStartingWith(self, prefix: str) -> int:
				current = self.root
				for c in prefix:
						if c not in current.children:
								return 0
						else:
								current = current.children[c]

				return current.prefixCounter


		def erase(self, word: str) -> None:
				current = self.root
				current.prefixCounter -= 1
				for c in word:
						if c not in current.children:
								return
						else:
								current = current.children[c]
								if current.prefixCounter > 0:
										current.prefixCounter -= 1

				if current.wordCounter > 0:
						current.wordCounter -= 1
------------------------------------------------------------------

class Trie:

    def __init__(self):
        self.ds ={}

    def insert(self, word: str) -> None: #O(N), where N is length of word
        letters = list(word)
        t=self.ds
        for letter in letters:
            if letter not in t:
                t[letter] = {}
            t = t[letter]
        if "end" not in t:
            t["end"] = 0
        t["end"] += 1
        
            

    def countWordsEqualTo(self, word: str) -> int: #O(N), where N is length of word
        letters = list(word)
        t=self.ds
        for letter in letters:
            if letter not in t:
                return 0
            t = t[letter]
        if "end" in t:
            return t["end"]
        else:
            return 0
        

    def countWordsStartingWith(self, prefix: str) -> int: #O(N), where N is length of word
        letters = list(prefix)
        t=self.ds
        for letter in letters:
            if letter not in t:
                return 0
            t = t[letter]
        s = [t]
        c=0
        while s:
            st = s.pop()
            for k,v in st.items():
                if k=="end":
                    c+=st["end"]
                else:
                    s.append(v)
        return c
            
    def erase(self, word: str) -> None: #O(N) where N is length of word
        letters = list(word)
        t=self.ds
        for letter in letters:
            if letter not in t:
                return False
            t = t[letter]
        t["end"] -= 1
        
---------------------------------------------------------


After seeing the answers given here and not feeling satisfied, I came up with this solution. Hope by the time you read this, there are more efficient and modular solutions than what I have given here.

Points to note:

I used word_count to keep track of the number of occurences of the word
count keeps track of the occurences of the letters in the word
The reason we require 2 variables is because, when we erase from the Trie, assuming we do not have word_count there is no way to know if we deleted a word or just letters occuring in a word.
Lets say we have 2 words app and apple. When we erase app, the count variable will not be 0
How can we set the is_word variable to False then?
Hence we require a word_count which helps us keep track of words getting erased and when the count reaches 0, sets the is_word variable to False.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0
        self.word_count = 0

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1
        node.is_word = True
        node.word_count += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.word_count if node.is_word else 0
        

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count
        

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.children[c]
            node.count -= 1
        node.word_count -= 1
        if node.word_count == 0:
            node.is_word = False
           
        
            
        
