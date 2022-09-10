'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        
        longest = 0
        
        for n in nums:
            #check if its the start of sequence
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                longest = max(longest, length)
        return longest
-------------------------------------------------------------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        cur_consecutive = 1
        heapq.heapify(nums)
        prev = heapq.heappop(nums)
        while nums:
            cur = heapq.heappop(nums)
            diff = cur - prev
            if diff == 1:
                cur_consecutive += 1
                ans = max(ans, cur_consecutive)
            elif diff > 1:
                cur_consecutive = 1
            prev = cur
        return ans
------------------------------------------------------------------------------------
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        
        heapq.heapify(nums)
        
        res = 1
        
        cur_consec = 1
        
        prev = heapq.heappop(nums)
        
        while nums:
            
            cur = heapq.heappop(nums)
            
            diff = cur - prev
            if diff == 1:
                cur_consec +=1
                res = max(res, cur_consec)
            
            elif diff > 1:
                cur_consec = 1
            
            prev = cur
        
        return res
            
