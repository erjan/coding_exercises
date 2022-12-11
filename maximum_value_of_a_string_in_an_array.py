'''
The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
'''
#my own solution

class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        res = float('-inf')
        for w in strs:

            if w.isdigit():
                res = max(res, int(w,10))
            else:
                res = max(res, len(w))
        return res
      
----------------------------------------------------------------------------------
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs:
            if s.isnumeric():
                ans = max(ans,int(s))
            else:
                ans = max(ans,len(s))
        return ans
                
