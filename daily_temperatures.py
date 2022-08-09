'''
Given an array of integers temperatures 
represents the daily temperatures, return an 
array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 
 '''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums= temperatures
        stack = list()
        res = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            cur = nums[i]

            while stack and cur >= stack[-1][1]:
                stack.pop()
            if stack and cur < stack[-1][1]:
                dist = stack[-1][0] - i
                res[i] = dist
            stack.append([i, nums[i]])

        print(res)
        return res
