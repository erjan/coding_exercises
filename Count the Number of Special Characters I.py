'''
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.
'''


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        fr = defaultdict(int)

        for ch in word:
            fr[ch]+=1
  

        res = 0

        for k,v in fr.items():
            if k.islower() and k.upper() in fr and fr[k.upper()]>0:
                res+=1
        return res

--------------
#another solution:

class Solution:
    def numberOfSpecialChars(self, word: str, ans = 0) -> int:
        
        for ch, CH in zip(ascii_lowercase, ascii_uppercase):
  
            ans+= ch in word and CH  in word

        return ans
