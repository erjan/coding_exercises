'''
Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.
'''



class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            if i+int(str(i)[::-1])==num:
                return True
        return False
