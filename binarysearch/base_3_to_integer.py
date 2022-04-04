'''

Given a string s representing a number in
base 3 (consisting only of 0, 1, or 2), return its decimal integer equivalent. This should be 
implemented directly without using a built-in function.
'''



class Solution:
    def solve(self, s):

        deg = 0

        res = 0

        for i in range(len(s)-1,-1,-1):

            res += int(s[i]) * 3**deg
            deg+=1
        return res
        

