'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
#my own solution - O(nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-k]
        return res
      
      
#many other follow ups possible?!



# O(k+(n-k)lgk) time, min-heap    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
            return heapq.nlargest(k, nums)[-1]

        
# max - heap - #1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = heapq.nlargest(k, nums) # run time O(n+klgn)
        return ans[-1]
