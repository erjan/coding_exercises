'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
'''

class Solution:
    def atMostK(self, nums, k):
        good_count = 0
        counter = collections.Counter()
        
        begin = 0
        for end in range(len(nums)):
            if counter[nums[end]] == 0:
                k -= 1
            counter[nums[end]] += 1
            
            while k < 0:
                counter[nums[begin]] -= 1
                if counter[nums[begin]] == 0:
                    k += 1
                
                begin += 1
            
            good_count += end - begin + 1
        
        return good_count
            
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
      
----------------------------------------------------------------------------------------

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = ii = 0 
        freq = defaultdict(int)
        queue = deque()
        for i, x in enumerate(nums): 
            freq[x] += 1
            queue.append(i)
            if len(freq) > k: 
                ii = queue[0]+1
                freq.pop(nums[queue.popleft()])
            while freq[nums[queue[0]]] > 1: freq[nums[queue.popleft()]] -= 1
            if len(freq) == k: ans += queue[0] - ii + 1
        return ans 
      
---------------------------------------------------------------------------------
