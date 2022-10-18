'''
You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where 
a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically
larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.
'''



every time before we move the pointer, we compare the remaining string of word1 and word2, pick the first letter from the larger sring

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ''
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1:] > word2[p2:]:
                res += word1[p1]
                p1 += 1
            else:
                res += word2[p2]
                p2 += 1
        
        res += word1[p1:] + word2[p2:]

        
        return res
      
-------------------------------------------------------------------------------------------
class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        ans=[]
        m,n=len(w1),len(w2)
        i=j=0
        while i<m or j<n:
            if w1[i:]>w2[j:]:
                ans.append(w1[i])
                i+=1
            else:
                ans.append(w2[j])
                j+=1
        return ''.join(ans)
      
