'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        res = []
        n = num
        up_limit = 2**31-1
        low_limit = -2**31

        for i in range(25):
            temp = 4**i
            if temp < up_limit:
                res.append(temp)

        if n in res:
            print('true')
            return True
        print('false')
        return False
