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
    
---------------------------------------------------------------------------------------------------------
We first convert nums to a list of tuples where we store each elements minimum and maximum values. For each number n, if n is odd the minumum value is n itself and the maximum is 2*n. If n is even, the maximum value is n (we can't multiply it by 2) and the minimum value calculated based on how many times we can devided it by 2. For example if n=20 the minumum value in 5.

After this, until the minimum value in array is not reached it's maximum we mulitply it by two and check if it decreases the max deviation we update the answer (it does not necessariliy decrease the deviation because when we double the value it may become the new maximum of the array and increase the deviation.

from heapq import heapify, heappop, heappush

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = self.create_min_max_vals(nums)
        ans = float('inf')
        maximum = max(nums)[0]
        while True:
            minn = heappop(nums)
            diff = maximum - minn[0]
            if diff < ans:
                ans = diff
            if minn[0] == minn[1]:
                break
            else:
                v = minn[0]*2
                heappush(nums, (v, minn[1]))
                if v > maximum:
                    maximum = v
                
        return ans      
    
    def create_min_max_vals(self, nums):
        res = []
        for n in nums:
            if n % 2 == 1:
                res.append((n, 2*n))
            else:
                x = n
                while x % 2 == 0:
                    x = x // 2
                res.append((x, n))
        
        heapify(res)
        return res
