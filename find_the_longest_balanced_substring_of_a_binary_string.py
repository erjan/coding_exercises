
'''
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number 
of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.
'''



class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res, temp = 0, "01"
        while len(temp) <= len(s):
            if temp in s: 
                res = len(temp)
            temp = '0' + temp + '1'
        return res
        
------------------------------------------------------------------------------------------------
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        it = 0
        while it < len(s):
            oCnt ,zCnt = 0 , 0
            while it < len(s) and s[it] == "0"  :
                zCnt += 1
                it += 1
            while it < len(s) and s[it] == "1":
                oCnt += 1
                it += 1
            res = max(res,2*min(oCnt,zCnt))
        return res
