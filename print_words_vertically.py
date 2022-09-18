'''
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
'''

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        maxiword = len(max(s, key=len))
        res = []

        for i in range(len(s)):
            s[i] = s[i].ljust(maxiword)

        res = list(zip(*s))

        for i in range(len(res)):
            res[i] = "".join(res[i])

        for i in range(len(res)):
            res[i] = res[i].rstrip()

        return res
---------------------------------------------------------------------------

class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_len = max([len(word) for word in s.split(' ')])
        words = s.split(' ')
        output = []
        for i in range(max_len) : 
            val, flag = "", True
            for word in words : 
                if i >= len(word) : 
                    val += " "
                else : 
                    if flag : 
                        space_count = len(val)
                        flag = False
                    val += word[i] 
            if val[-1] == ' ' : 
                val = ' '*space_count + val.strip()
                
            output.append(val)
        return output 
      
------------------------------------------------------------------------------------
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        output = []
        for key in range(len(max(s, key=len))):
            output.append(''.join(s[x][key] if len(s[x]) > key else ' ' for x in range(len(s))).rstrip())
        return output
      
