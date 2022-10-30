'''
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.
'''

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        x = y = res = float('-inf')
        for a in arr:
            x, y = max(a, x + a), max(x, y + a)
            res = max(res, x, y)
        return res
      
-----------------------------------------------------------------------------------
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp1,dp2,res = float('-inf'),arr[0],arr[0]
        for i in range(1,n):
            dp1,dp2= max(dp1+ arr[i],dp2),max(dp2 + arr[i],arr[i])
            res = max(res,dp1,dp2)
        return res
      
----------------------------------------------------------------------------------------------------------
Keep two array's one will have prefix sum ending at that index from start and one will have prefix sum ending at that index from end, using kadane's algorithm. For each i these array's will denote maximum subarray ending at i-1 and maximum subarray starting at i+1 so when you add these two values it will denote maximum subarray after deleting i.

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        #maximum subarray starting from the last element i.e. backwards 
        prefix_sum_ending = [float('-inf')]*n
        #maximum subarray starting from the first element i.e forwards
        prefix_sum_starting = [float('-inf')]*n
        prefix_sum_ending[n-1] = arr[n-1]
        prefix_sum_starting[0] = arr[0]
        
        for i in range(1,n):
            prefix_sum_starting[i] = max(prefix_sum_starting[i-1]+arr[i], arr[i])
        for i in range(n-2,-1,-1):
            prefix_sum_ending[i] = max(prefix_sum_ending[i+1]+arr[i], arr[i])
           
        max_without_deletion = max(prefix_sum_starting)
        max_with_deletion = float('-inf')
        for i in range(1,n-1):
            max_with_deletion = max(max_with_deletion, prefix_sum_starting[i-1]+prefix_sum_ending[i+1])
            
        return max(max_without_deletion, max_with_deletion)
      
--------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # First build a list of max subarray sum (up to that number) with no deletion
        # which is just a max subarray sum problem
        noDeletion = [nums[0]]
        for i in range(1, len(nums)):
            noDeletion.append(nums[i] + max(0, noDeletion[i - 1]))
        
        # Then build a list of max subarray sum (up to that number) with at most one deletion
        oneDeletion = [nums[0]]
        for i in range(1, len(nums)):
            # for each number, to ensure there is at most one deletion, we could
            # 1. use the one from noDelete 
            # 2. delete this number by using noDeletion[i - 1]
            # 3. including this number with at most one delete up to last index
            oneDeletion.append(max(noDeletion[i], noDeletion[i - 1], nums[i] + oneDeletion[-1]))

        return max(oneDeletion)
