'''
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.
'''
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        start, end = 0, max(arr)
        res, mn, val = float("inf"), float("inf"), -1
        while start <= end:
            mid = (start + end)//2
            sums = 0
            for i in arr:
                sums += min(mid, i)
            val = abs(sums-target)
            if val == mn:
                res = min(res, mid)
            if val < mn:
                mn = val
                res = mid
            if sums >= target:
                end = mid-1
            else:
                start = mid+1
        return res
      
