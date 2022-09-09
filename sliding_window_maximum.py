'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        
        l = r = 0
        q = collections.deque()
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r+1) >=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
