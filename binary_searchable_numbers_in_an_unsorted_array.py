'''
Consider a function that implements an algorithm similar to Binary Search. The function has two input parameters: sequence is a sequence of integers, and target is an integer value. The purpose of the function is to find if the target exists in the sequence.

The pseudocode of the function is as follows:

func(sequence, target)
  while sequence is not empty
    randomly choose an element from sequence as the pivot
    if pivot = target, return true
    else if pivot < target, remove pivot and all elements to its left from the sequence
    else, remove pivot and all elements to its right from the sequence
  end while
  return false
When the sequence is sorted, the function works correctly for all values. When the sequence is not sorted, the function does not work for all values, but may still work for some values.

Given an integer array nums, representing the sequence, that contains unique numbers and may or may not be sorted, return the number of values that are guaranteed to be found using the function, for every possible pivot selection.

 
 '''


Explanation
The intuition is to find in what situation this function will work
If you know Quick Sort, you will soon realize this problem is the same idea as find a pivot in Quick Sort. Check this Wikipedia - Quick Sort to know more about it.
A pivot in Quick Sort guarantees that
Every number on the left side of it are less than it
Every number on the right side of it are greater than it
And thus the pivot number is at the index, which is same as the index when the sequence is sorted
For example, nums = [8, 5, 13, 26, 14]
After sorting, nums = [5, 8, 13, 14, 26]
In this case, 13 is a pivot and it will work for the function given by this question
Because, 5, 8 on its left is less than 13, and 14, 26 on its right is greater than 13. 13 is at the sorted index
To find pivot described as above, we simply need to do a prefix-maximum and a suffix-minimum number by using prefix array. For each index i, make sure that
Prefix-maximum is less than nums[i]
Suffix-minimum is greater than nums[i]
Count & return the total count of these pivots
NOTE: Quick Sort is not absolutely necessary, but it does help you come up with the idea since it's somewhat familiar to you if you had experience with it.

Implementation
class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        prefix = [False] * n                  # Create prefix array and initialize them as False
        cur_max, cur_min = nums[0], nums[-1]  # Initialize prefix_max & suffix_min
        for i in range(n):                    # Update prefix from left to right
            prefix[i] = cur_max <= nums[i] 
            cur_max = max(cur_max, nums[i])
        for i in range(n-1, -1, -1):          # Update suffix and count from right to left
            prefix[i] &= cur_min >= nums[i]   # Use `&` operation (`and` is also fine) to make sure 2 condition hold at the same time
            ans += prefix[i]                  # +1 when `prefix[i]` is True, otherwise +0 (no change)
            cur_min = min(cur_min, nums[i])    
        return ans
      
--------------------------------------------------------------------------------------------------------------
The way I thought about this was to think about how binary search works. We know that the underlying property that makes binary search work is that for the pivot:

all items to the left must be less than the pivot
all items to the right must be more than the pivot
Therefore, we look at each item in the list and ask

Are all items to the left of this target less than it?
Are all items to the right of this target more than it?
If the answer to both questions is yes then we would successfully find the target, no matter what random pivot we used. Think about that from a binary search perspective.
If we have
[1,2,0,7,8] and our target was 7.

picking 1 as our pivot would discard the 1. 1 < 7 so we discard it and items to the left.
picking 2 as our pivot would discard the 1 and 2. 2 < 7 so we discard it and items to the left.
picking 0 as our pivot would discard the 1, 2 and 0. 0 < 7 so we discard it and items to the left.
picking 7 as our pivot gives us the answer immediately
picking 8 as our pivot would discard the 8. 8 > 7 so we discard it and items to the right.
Any choice of pivot for target 7 works because all items left of 7 are less than it and all items right of 7 are more than it.

[1,2,0,7,8] and our target was 0.

picking 1 as our pivot would discard the 1 and everything to the right. 1 > 0 so we discard it and items to the right. This wipes our target out so it would not be found if 1 was the pivot.
The reason this is broken when the pivot is 0 and target is 1 is because 1 is more than 0 bit its on the left instead of the right.

Kinowing ths the obvious solution is to build two arrays, one which stores the maximum value to the left of each position and one which stores the minimum value to the right of each position.

For example
[1,2,0,7,8]
max_lefts = [-inf,1,2,2,7]
min_rights = [0,0,7,8,inf]

Then we compare against each. If max_lefts[i] < nums[i] < min_rights[i] then the item would be found regardless of which pivot was chosen.

The solution below improves on this slightly by only storing a single array (min_rights) as the max_lefts can be done by storing a single value of the max_right as we traverse nums from left to right.

class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        min_rights = [math.inf]
        for n in reversed(nums):
            min_rights.append(min(min_rights[-1], n))
        # Don't want to compare the first value against itself, 
		# we want to compare against the second value, so remove the first.
        min_rights.pop()
        max_left = -math.inf
        result = 0
        for n in nums:
            max_right = min_rights.pop()
            if max_left < n < max_right:
                result += 1
            max_left = max(max_left, n)
        return result 
      
---------------------------------------------------------------------------------
class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        suffix = [inf]
        for x in reversed(nums): suffix.append(min(suffix[-1], x))
        suffix = suffix[::-1]
        
        ans = 0
        prefix = -inf 
        for i, x in enumerate(nums): 
            prefix = max(prefix, x)
            if prefix == x == suffix[i]: ans += 1
        return ans 
      
-----------------------------------------------------------------------------------------------
The key idea is to find minimums for each element starting from the right side and maximums for each element starting from the left side. If an element is equal to maximum and minimum, it will be found.

class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        maximums = [nums[0]] # from the left
        minimums = [0] * len(nums) # from the right
        min_n = nums[-1]
        result = 0
        
        for n in nums[1::]:
            maximums.append(max(maximums[-1], n))
            
        for idx in range(len(nums)-1, -1, -1):
            min_n = min(min_n, nums[idx])
            minimums[idx] = min_n
            
            if nums[idx] == maximums[idx] and nums[idx] == minimums[idx]:
                result += 1
        
        return result
Complexity Analysis:

Time complexity : O(n)
Space complexity : O(n)
      
      
