
'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True     
        return dp[-1]
      
----------------------------------------------------------------------

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		# instantiate an empty trie 
        trie = Trie()
        # Iterate over words in dictionary and build trie one word at a time
        for word in wordDict:   #------ O(W) where W = len(words)
            trie.add(word)  #--------------- O(K) where K = len(word)
        print(trie.root.children)
        # Words have been added. Find if s is made up of words in the trie
        return trie.find(s)  # ---- Overall time : O(W*K) OR O(S*S[i+1:]) Whichever is worst

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_done = False

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.memo = {}

    def add(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Node(char)
            root = root.children[char]  
        root.is_done = True    

    def find(self, s):
        root = self.root
        for i, char in enumerate(s):
            if char not in root.children:   # [1] 
                return False
            
            if root.children[char].is_done: # [2]
			                                          

                if s[i+1:] not in self.memo:                  #
                    self.memo[s[i+1:]] = self.find(s[i+1:]) 

                if self.memo[s[i+1:]]:                        
                    return True                                                                                                                  

            root = root.children[char]         
        
        return root.is_done
                            
    
   
