
'''
Given an array of integers nums and an integer limit, return the 
size of the longest non-empty subarray such that the absolute 
difference between any two elements of this subarray is less than or equal to limit.
'''

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQueue = deque()
        maxQueue = deque()
        
        ans = 0
        l = 0
        for r in range(len(nums)):
            # removing max elements on the left
            while maxQueue and nums[maxQueue[-1]] < nums[r]:
                maxQueue.pop()
                
            maxQueue.append(r)
            
            # removing min elements on the left
            while minQueue and nums[minQueue[-1]] > nums[r]:
                minQueue.pop()
                
            minQueue.append(r)
            
            maxEl = nums[maxQueue[0]]
            minEl = nums[minQueue[0]]
            
            if abs(maxEl - minEl) <= limit:
                ans = max(ans, r-l+1)
            else:
                # shrink window
                if l == maxQueue[0]:
                    maxQueue.popleft()
                if l == minQueue[0]:
                    minQueue.popleft()
                    
                l += 1
        return ans 
