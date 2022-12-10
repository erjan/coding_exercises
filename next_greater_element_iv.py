'''
You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.

The second greater integer of nums[i] is nums[j] such that:

j > i
nums[j] > nums[i]
There exists exactly one index k such that nums[k] > nums[i] and i < k < j.
If there is no such nums[j], the second greater integer is considered to be -1.

For example, in the array [1, 2, 4, 3], the second greater integer of 1 is 4, 2 is 3, and that of 3 and 4 is -1.
Return an integer array answer, where answer[i] is the second greater integer of nums[i].
'''


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s, ss = [], []
        for i, x in enumerate(nums): 
            while ss and nums[ss[-1]] < x: ans[ss.pop()] = x
            buff = []
            while s and nums[s[-1]] < x: buff.append(s.pop())
            while buff: ss.append(buff.pop())
            s.append(i)
        return ans 
      
----------------------------------------------------------------------------------
