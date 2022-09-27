'''
Given an array of integers arr and an integer k. Find 
the least number of unique integers after removing exactly k elements.
'''


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = Counter(arr)
        ans = len(count)
        for i in sorted(count.values()):
            k -= i
            if k < 0:
                break
            ans -= 1
        return ans
