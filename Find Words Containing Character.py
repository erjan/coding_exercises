You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
-----------------------------------------------------------------------------------------

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for ind,word in enumerate(words):
            if x  in word:
                res.append(ind)

        return res
---------------------------------------------------------------------------------------------------

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if w.find(x)!=-1]
        
        
