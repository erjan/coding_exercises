'''
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.
'''

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        
        res = 0
        for i in range(k):
            t = -heappop(nums)
            res += t
            heappush(nums, -ceil(t / 3))
        
        return res
      
----------------------------------------------------------------------------------------
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        pq = []
        for num in nums:
            heapq.heappush(pq, (-num, num))
        while k > 0:
            max_element = heapq.heappop(pq)[1]
            score += max_element
            updated_value = max_element // 3 + (max_element % 3 != 0)
            heapq.heappush(pq, (-updated_value, updated_value))
            k -= 1
        return score
        
