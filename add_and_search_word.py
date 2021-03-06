'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''

#TLE SOLUTION USING LIST
class WordDictionary:

    def __init__(self):
        
        self.main = list()
        

    def addWord(self, word: str) -> None:
      
        if word not in self.main:
            print('appended ' + str(word))
            self.main.append(word)
        print()
        
        

    def search(self, word: str) -> bool:
       
        
        res = []
        same_length = list(filter(lambda x: len(x) == len(word),self.main))
        print(same_length)
        for i in range(len(same_length)):
            print()
            word_in_main = same_length[i]
            print('word ' + word_in_main)
            mismatch = False
            for j in range(len(word_in_main)):
                if word[j] != '.' and word_in_main[j] != word[j]:
                    print('mismatch found!!!!')
                    mismatch = True
            
            if mismatch== False:
                print('good word -match!')
                res.append(word)
        print(res)
        return len(res) != 0
                        

obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
param1 = obj.search('b..')



print(param1)


#solution from knowledge center

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None]*26
        self.endword = False
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self
        for c in word:
            if curr.children[ ord(c) - ord('a')] == None:
                curr.children[ ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ ord(c) - ord('a')]
        curr.endword = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch!= None and ch.search(word[i+1:]):return True
                return False
            if curr.children[ord(c) - ord('a')] == None:return False
            curr = curr.children[ord(c) - ord('a')]
        return curr != None and curr.endword
