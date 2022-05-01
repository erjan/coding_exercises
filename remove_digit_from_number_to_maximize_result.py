'''
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing 
exactly one occurrence of digit from number such that the 
value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number
'''


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        nums = number
        res = list()
        maxnum = float('-inf')
        for i in range(len(nums)):
            if nums[i] == digit:
                temp = (nums[0:(i)] + nums[(i+1):])
                temp = int(temp)
                if temp > maxnum:
                    maxnum = temp
        #print(maxnum)
        return str(maxnum)
