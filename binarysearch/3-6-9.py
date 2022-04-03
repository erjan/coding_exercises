'''

Given an integer n, return a list with each number from 1 to n, except if it's a multiple of 3 or has a 3, 6, or 9 in the number, it should be the string "clap".

Note: return the number as a string.

'''

#my own solution

class Solution:
    def solve(self, n):
        res = list()
        for i in range(1,n+1):

            num_i = int(i)
            str_i = str(i)

            if num_i %3 == 0 or '3' in str_i or '6' in str_i or '9' in str_i:
                res.append('clap')
            else:
                res.append(str_i)
        return res
        
        
        
#another using map()

class Solution:
    def clap(self, i):
        if i % 3 == 0:
            return "clap"
        i = str(i)
        if "3" in i or "6" in i or "9" in i:
            return "clap"
        return i

    def solve(self, n):
        return list(map(self.clap, range(1, n + 1)))
