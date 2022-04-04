
'''

Given a list of unsorted integers nums, and an integer k, return the kth (0-indexed) smallest element in the list.

This should be done in \mathcal{O}(n)O(n) time on average.

'''


import heapq

class Solution:
    def solve(self, nums, k):
        
        heapq.heapify(nums)
        res = heapq.nsmallest(k+1,nums)
        return (res[-1])
      
#another      
class Solution:
    def solve(self, nums, k):
        hp = []
        heapq.heapify(hp)
        for num in nums:
            heapq.heappush(hp, num)

        while k >= 0:
            num = heapq.heappop(hp)
            k -= 1
        return num      
      
      
#another - quick select algo

import random


class Solution:
    def solve(self, nums, k):
        def solve(oi, oj, k):
            # Solve for k-th largest on nums[oi..oj]
            if oi >= oj:
                return nums[oi]

            # Move random 'pivot' element to j-th position
            p = random.randint(oi, oj)
            nums[oj], nums[p] = nums[p], nums[oj]

            # Lomuto's partition scheme - partition by pivot nums[j]
            i = oi
            for j in range(oi, oj):
                if nums[j] < nums[oj]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[oj] = nums[oj], nums[i]

            # nums[oi..i] is before nums[i+1..oj]
            if k <= i - oi:
                return solve(oi, i, k)
            return solve(i + 1, oj, k - (i - oi + 1))

        return solve(0, len(nums) - 1, k)
