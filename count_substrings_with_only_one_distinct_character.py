'''
Given a string s, return the number of substrings that have only one distinct letter.
'''

#brute force
class Solution:
    def countLetters(self, s: str) -> int:
            count = 0
            for i in range(len(s)):

                for j in range(i, len(s)):

                    substr = s[i:j+1]
                    if len(set(substr)) == 1:
                        count += 1
            print(count)
            return count

        
        
#my own solution        
class Solution:
    def countLetters(self, s: str) -> int:
       
        res = list()
        for c, g in itertools.groupby(s):
            res.append(len(list(g)))

        total = 0

        for i in range(len(res)):

            q = res[i]
            total += q*(1+q)//2

        print(total)
        return total 
    
    
class Solution:
    def countLetters(self, S: str) -> int:
        S = ' '+ S + ' '
        total, count = 0, 1
        for i in range(1, len(S)-1):
            if S[i] != S[i-1]:
                count = 1
            else:
                count += 1 
            total += count
        return total    
    
    
    
class Solution:
    def countLetters(self, S: str) -> int:
        ans = 0
        for _, g in itertools.groupby(S):
            q = sum(1 for _ in g)
            ans += (1 + q) * (q) // 2
        return ans    
