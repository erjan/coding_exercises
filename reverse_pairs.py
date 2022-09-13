'''
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
'''

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0

        def merge(left, right):
            nonlocal cnt
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    i += 1
                else:
                    cnt += len(left)-i
                    j += 1

            return sorted(left+right)


        def mergeSort(A):
            if len(A) <= 1:
                return A
            return merge(mergeSort(A[:(len(A) + 1) // 2]), mergeSort(A[(len(A) + 1) // 2:]))

        mergeSort(nums)
        return cnt
-------------------------------------------------------------------------------------------------------
class FenwickTree:
    def __init__(self, n: int) -> None:
        self.BIT = [0] * (n+1)
        
    def sum(self, x: int) -> int:
        rv = 0
        while x > 0:
            rv += self.BIT[x]
            x -= x&-x
        return rv
    
    def add(self, x: int, delta: int) -> None:
        while x < len(self.BIT):
            self.BIT[x] += delta
            x += x&-x
            
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        doubleNums = [n * 2 for n in nums]
        m = {n: i+1 for i, n in enumerate(sorted(set(nums + doubleNums)))}
        numsRanks = [m[n] for n in nums]
        doubleNumsRanks = [m[n] for n in doubleNums]
        ft = FenwickTree(len(nums * 2))
        rv = 0
        for i in range(len(nums)-1, -1, -1):
            rv += ft.sum(numsRanks[i]-1)
            ft.add(doubleNumsRanks[i], 1)
        return rv
