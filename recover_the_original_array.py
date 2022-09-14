'''
Alice had a 0-indexed array arr consisting of n positive integers. She chose an arbitrary positive integer k and created two new 0-indexed integer arrays lower and higher in the following manner:

lower[i] = arr[i] - k, for every index i where 0 <= i < n
higher[i] = arr[i] + k, for every index i where 0 <= i < n
Unfortunately, Alice lost all three arrays. However, she remembers the integers that were present in the arrays lower and higher, but not the array each integer belonged to. Help Alice and recover the original array.

Given an array nums consisting of 2n integers, where exactly n of the integers were present in lower and the remaining in higher, return the original array arr. In case the answer is not unique, return any valid array.

Note: The test cases are generated such that there exists at least one valid array arr.
'''

from sortedcontainers import SortedList

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        possible=[(nums[i]-nums[0])//2 for i in range(1, len(nums)) if (nums[i]-nums[0])%2==0 and nums[i]!=nums[0]]
        for i in possible:
            cur=SortedList(nums)
            memo=[]
            while len(cur)>0:
                first=cur[0]
                cur.remove(first)
                if first+i+i not in cur:
                    break
                memo.append(first+i)
                cur.remove(first+i+i)
            if len(cur)==0:
                return memo
