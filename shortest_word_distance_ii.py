'''
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
'''


from collections import defaultdict

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        
        self.d = defaultdict(list)
        
        for i,w in enumerate(wordsDict):
            
            self.d[w] = self.d.get(w,[]) + [i]
                
                

        
    def shortest(self, word1: str, word2: str) -> int:
        i = 0
        j = 0
        l1 = self.d[word1]
        l2 = self.d[word2]
        shortest = float('inf')
        while i < len(l1) and j < len(l2):
            shortest = min(shortest, abs(l1[i]-l2[j])   )
            if l1[i] < l2[j]:
                i+=1
            else:
                j+=1
                
        return shortest

        
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


------------------------------------------------------------------------------------
class Solution:
   def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
       m=len(words)
       p1=-len(words)
       p2=len(words)
       for i in range(len(words)):
           if words[i]==word1:
               if words[i] == word2:
                   p2 = p1
               p1=i
           elif words[i]==word2:
               if words[i] == word1:
                   p1=p2
               p2=i
           m=min(m,abs(p1-p2))
       return m

------------------------------------------------------------------------

def shortestWordDistance(self, words, word1, word2):
    p1 = p2 = -1
    res = len(words)
    # first case: the same as Shortest Word Distance
    if word1 != word2:
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
            if w == word2:
                p2 = i
            if p1 > -1 and p2 > -1:
                res = min(res, abs(p1-p2))
        return res
    else:
        # pre and i record previous and current word1 respectively
        pre, i = -len(words), 0
        while i < len(words):
            while i < len(words) and words[i] != word1:
                i += 1
            if i < len(words):
                res = min(res, i-pre)
            pre = i
            i += 1
        return res
    
-------------------------------------------------------------------------------------------
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        idx1, idx2 = [], [] 
        
        for i in range(n):
            word = wordsDict[i]
            if word == word1:
                idx1.append(i)
            elif word == word2:
                idx2.append(i)

        res = float('inf')
        if word1 == word2:
            for i in range(1, len(idx1)):
                res = min(res, idx1[i] - idx1[i-1])
            return res
        res = float('inf')
        i, j = 0, 0

        while i < len(idx1) and j < len(idx2):
            res = min(res, abs(idx1[i]-idx2[j]))
            if idx1[i] > idx2[j]:
                j += 1
            else: # idx1[i] < idx2[j]
                i += 1
            
            
        return res 
    
