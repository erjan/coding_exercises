'''
You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.

We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].

Return the maximum possible greatness you can achieve after permuting nums.
'''

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int: 
        nums.sort() 
        count = 0
        j = i = 0  
        while j < len(nums):
            if nums[i] < nums[j]:
                count+=1 
                i+=1
            j+=1 
        return count
        
-----------------------------------------------------------------------------
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for num in nums:
            if num>nums[ans]:
                ans+=1

        return ans
    
-----------------------------------------------------------------------------------------
import heapq 
class Solution(object):
    def maximizeGreatness(self, nums):
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        # print(nums)
        arr=[]
        ans=0

        for i in range(len(nums)):
            curr_min = heapq.heappop(nums)
            heapq.heappush(arr, curr_min)
            
            if arr and nums and -arr[0] > -nums[0]:
                ans += 1
                heapq.heappop(arr)
                
        # print(ans)
        return ans
    
---------------------------------------------------------------------------------------------------
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        res = 0
        nums.sort()
        for num in nums:
            while minHeap and minHeap[0] <= num:
                heapq.heappop(minHeap)
            if minHeap:
                heapq.heappop(minHeap)
                res += 1
            if not minHeap:
                break
        return res
        
        
