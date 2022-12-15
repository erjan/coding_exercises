'''
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.
'''

class Solution:
    def calculateSum(self, nums, cost, target):
        res = 0
        for n, c in zip(nums, cost):
            res += abs(n - target) * c
        return res
    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        s, e = min(nums), max(nums)
        
        while s < e:
            mid = (s + e) // 2
            leftSum, rightSum = self.calculateSum(nums, cost, mid), self.calculateSum(nums, cost, mid + 1)
            if leftSum < rightSum:
                e = mid
            else:
                s = mid + 1
        
        return self.calculateSum(nums, cost, s)
      
------------------------------------------------------------------------------------------------------------------------
Observation
Think of the cost array as the weight of the corresponding num in the nums array. For example when nums = [1, 3, 5, 2] and cost = [2, 3, 1, 14], suppose we want to increase 1 in nums to 2, we know that the cost for this operation is 2. However, this is equivalent as if there are two 1’s in nums and we increase both of them to 2. Therefore, the minimum total cost such that all the elements of the array nums become equal is equivalent to the minimum total cost such that all the elements of the array
nums = [1, 1, 3, 3, 3, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
become equal, with the cost of doing one operation on each element being 1. As such, the answer to this question is the total cost for moving all elements to the (unweighted) median in the new (collapsed) array. See also LC 462. Minimum Moves to Equal Array Elements II and LC 296. Best Meeting Point for practice of unweighted median problems.

Implementation
We find the weighted median of nums by sorting the (num, weight) pair of the original arrays. We then use the weighted median (target) to calculate the minimum total cost such that all the elements of the array nums becomes equal, which is the answer to this question.

Complexity
Time Complexity: O(NlogN)
Space Complexity: O(N), for the use of arr

Solution

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in arr)
