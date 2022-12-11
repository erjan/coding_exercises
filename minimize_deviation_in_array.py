'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.
'''

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]%2!=0:
                nums[i]*=2
        minVal=min(nums)
        nums=[-val for val in nums]
        nums,ans=nums,float('inf')
        heapify(nums)
        while nums and abs(nums[0])%2==0:
            maxVal=abs(heappop(nums))
            ans=min(ans,abs(maxVal-minVal))
            maxVal=maxVal//2
            minVal=min(minVal,maxVal)
            heappush(nums,-maxVal)
        return min(ans,abs(min(nums))-abs(max(nums)))
            
            
--------------------------------------------------------------------------------------------------------------------------------------------
from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        S, ans = SortedList(i*2 if i & 1 else i for i in nums), 10**9
        while not S[-1] & 1:
            ans = min(ans, S[-1] - S[0])
            S.add(S.pop() // 2)
        return min(ans, S[-1] - S[0])
