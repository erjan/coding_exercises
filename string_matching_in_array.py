'''
Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
'''
#my solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)

        res = set()

        for i in range(len(words)):
            check = words[i]
            for j in range(i+1, len(words)):
                if check in words[j]:
                    res.add(check)

        res = list(res)
        return res
      
#better solution

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        temp = ' '.join(words)
        
        res = [ i for i in words if temp.count(i) > 1]
        print(res)
        del temp
        return res
    

       
      
      
      
