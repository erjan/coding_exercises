'''
Given an integer array nums, return the number of non-empty subarrays with 
the leftmost element of the subarray not larger than other elements in the subarray.

A subarray is a contiguous part of an array.

 '''


Inspired by https://leetcode.com/problems/number-of-valid-subarrays/discuss/318895/Python-O(n)-stack

Main idea:

Brute force that iterates through i and j in Python is too slow. Use stack.

We know that the number of subarrays that start at ind, and end somewhere before i is just i - ind.

As you store those elements, you append elements, and sometimes replace elements. Whenever you replace elements, the number of subarrays that start with that element can be given by i (The element that replaces) - ind (The element that's being replaced). Note that when you do the element popping, use a while loop to pop out everything that's bigger than it, rather than just popping one element.

When you are don with the stack, for every element in the stack, the number of subarrays that start from that element is its index to the end of nums, because the everything is valid given that the stack is monotonely increasing.

 class Solution(object):
 def validSubarrays(self, nums):
 	"""
 :type nums: List[int]
 :rtype: int
 """        
 count = 0
 stack = []
 for i,v in enumerate(nums):
     while stack and v < nums[stack[-1]]:
         ind = stack.pop(-1)
         count += i - ind
     stack.append(i)
 for i in stack:
     count += len(nums) - i
         
     
  return count
 
 
 -------------------------------------------
 class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            ans += (stack[-1] if stack else len(nums)) - i
            stack.append(i)
        return ans
        
        
--------------------------------------------------------
class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        stack = []
        nextSmaller = [n] * n
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                nextSmaller[stack.pop()] = i
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans += nextSmaller[i] - i
        return ans
