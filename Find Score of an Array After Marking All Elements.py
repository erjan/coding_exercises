'''
You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.
'''


class Solution:
    def findScore(self, nums: List[int]) -> int: 
        heap = [(nums[i],i) for i in range(len(nums))] 
        marked = {} 
        score = 0
        heapq.heapify(heap) 
        for i in range(len(nums)):
            mini,ind = heapq.heappop(heap) 
            if ind not in marked:
                score += mini 
                marked[ind] = 1 
                marked[ind-1] = marked[ind+1] = 1 
        return score
        
-----------------------------------------------------------------
class Solution:
    def findScore(self, nums: List[int]) -> int:

        n, score, seen = len(nums), 0, set()

        queue = sorted(enumerate(nums), key = lambda x: (x[1],x[0]))

        for idx, num in queue:
            if idx in seen: continue

            score+= num
            
            seen.add(idx)
            if idx > 0  : seen.add(idx-1)
            if idx < n-1: seen.add(idx+1) 
            
        return score
---------------------------------------------------------------------
#wrong solution

class Solution:
    def findScore(self, nums: List[int]) -> int:

        score = 0

        
        heapify(nums)


        while nums:

            smallest = heappop(nums)
            ind = nums.index(smallest)
            score += smallest
            if ind>0 and ind< len(nums):
                nums.remove(nums[ind-1])
                nums.remove(nums[ind+1])
            elif ind==0:
                nums.remove(nums[ind+1])
            elif ind == len(nums)-1:
                nums.remove(nums[ind-1])
        return score







        
