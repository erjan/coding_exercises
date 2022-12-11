'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
'''

from functools import lru_cache, cmp_to_key
import bisect

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return [nums[0][0], nums[0][0]]

        def compare(a, b):
            return len(a) - len(b)

        for i in range(len(nums)):
            nums[i] = sorted(list(set(nums[i])))

        nums = sorted(nums, key = cmp_to_key(compare))

        @lru_cache
        def searchRange(index, a, b):
            if index >= len(nums):
                return a, b
            
            index1 = bisect.bisect_left(nums[index], a)
            index2 = bisect.bisect_left(nums[index], b)

            if index1 < index2:
                # At least one number in current list is already included, continue
                return searchRange(index + 1, a, b)
            
            if index1 == 0:
                # First number only is included
                b = nums[index][index1]
                return searchRange(index + 1, a, b)
            
            if index1 == len(nums[index]):
                # Only last number is included
                a = nums[index][index1 - 1]
                return searchRange(index + 1, a, b)
            
            if nums[index][index1] == a or nums[index][index1] == b:
                # The same number from the range is present
                return searchRange(index + 1, a, b)

            # Trying to increase range to left number or to right number
            c = nums[index][index1 - 1]
            left = searchRange(index + 1, c, b)

            d = nums[index][index1]
            right = searchRange(index + 1, a, d)

            # Returning the smallest of two results
            if left[1] - left[0] < right[1] - right[0]:
                return left
            else:
                return right
        
        a, b = float('-inf'), float('inf')

        for n in nums[0]:
            # First range is consist of one number [n, n]
            c, d = searchRange(1, n, n)
            if d - c < b - a:
                a, b = c, d

        return [a, b]

--------------------------------------------------------------------------------------------------
from sortedcontainers import SortedList
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def compareRanges(range1, range2) -> bool:
            return (range1[1] - range1[0] < range2[1] - range2[0]) or ((range1[1] - range1[0]) == (range2[1] - range2[0]) and range1[0] < range2[0])
        
        PQ = SortedList([(lis[0], ind, 0) for ind, lis in enumerate(nums)])

        bestRange = [PQ[0][0], PQ[-1][0]]

        while len(PQ) > 0:
            
            newRange = [PQ[0][0], PQ[-1][0]]
            print("bestRange:", bestRange)
            print("newRange: ", newRange)
            print()
            if compareRanges(newRange, bestRange):
                bestRange = newRange
            
            _, numsIndex, listIndex = PQ.pop(0)
            
            if listIndex + 1 < len(nums[numsIndex]):
                PQ.add((nums[numsIndex][listIndex + 1], numsIndex, listIndex + 1))
            else:
                return bestRange
        
        return bestRange

      
      
