'''
Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which 
has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
'''

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie={}
        self.weight_marker='$'
        w=self.weight_marker
        for idx, word in enumerate(words):
            word=word + '#'
            length=len(word)
            word+=word
            
            for i in range(length):
                curr=self.trie
                curr[w]=idx 
                for c in word[i:]:
                    if c not in curr:
                        curr[c]={}
                    curr=curr[c]                    
                    curr[w]=idx  # update the weight of substring                        
            

    def f(self, prefix: str, suffix: str) -> int:
        curr=self.trie
        for c in suffix + '#' + prefix:
            if c not in curr:
                return -1
            curr=curr[c]
        
        return curr[self.weight_marker] 
