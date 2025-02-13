'''
You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

Take the two smallest integers x and y in nums.
Remove x and y from nums.
Add min(x, y) * 2 + max(x, y) anywhere in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
'''
#my solution! myself!

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        heapq.heapify(nums)

        while len(nums)>=2 and any(n <k for n in nums):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            temp = min(x,y) *2 + max(x,y)
            heapq.heappush(nums, temp)
            res+=1
        return res

-------------------------------------------------------------------

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        res=0

        for i in range(0, len(nums)):
            x=heapq.heappop(nums)
            if x<k:
                res+=1
                y=heapq.heappop(nums)
                val= x*2+y if (x<y) else y*2+x
                heapq.heappush(nums, val)
            else:
                break

        return res
      
