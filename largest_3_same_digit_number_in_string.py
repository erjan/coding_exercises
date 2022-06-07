
'''
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = num
        res = 0
        modified = False
        for i in range(len(nums)-2):

            check = (nums[i:i+3])

            unique = check.count(check[0])
            if unique == 3:
                if int(check) >= res:
                    modified = True
                    res = int(check)
        if res == 0 and modified:
            return '000'
        elif not modified:
            return ''
        return str(res)
      
---------------------------------------------------------
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = '' 
        cnt = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cnt+=1
            else:
                cnt = 1
            if cnt == 3:
                res = max(res, num[i] * 3)
                
        return res
      
--------------------------------------------------------------
    @timeit
    def largest_good_integer2(self, num: str) -> str:
        for test in [str(i)*3 for i in range(9, -1, -1)]:
            if test in num:
                return test
        return ''
