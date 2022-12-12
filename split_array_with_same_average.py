'''
You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.
'''


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        sz, sm = len(nums), sum(nums)
        nums.sort()

        @cache
        def dfs(size: int, _sum: int, start: int) -> bool:
            nonlocal nums, sz
            if size == 0:
                return _sum == 0
            for idx in range(start, sz):
                if _sum < nums[idx] * size:
                    return False
                if dfs(size - 1, _sum - nums[idx], idx + 1):
                    return True

        for idx in range(1, (sz // 2) + 1):
            if (idx * sm) % sz == 0 and dfs(idx, (idx * sm) // sz, 0):
                return True
        return False
      
---------------------------------------------------------------------------------------------
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort()
        DP=[set() for _ in range(len(A)//2+1)]    #DP[i] stores the all available sum with i items in a bracket
        all_sum=sum(A)
        DP[0]=set([0])
        for item in A:                  #iterate over items in the list
            for count in range(len(DP)-2,-1,-1):          # iterate backwards w.r.t. the bracket size
                if len(DP[count])>0:                             # if DP[i] is not empty, then update DP[i+1] by adding the current item into all sums in DP[i]
                    for a in DP[count]:
                        DP[count+1].add(a+item)
        for size in range(1,len(DP)):
            if all_sum*size/len(A) in DP[size]:
                return True
        return False
      
------------------------------------------------------------------------

      
