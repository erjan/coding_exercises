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
