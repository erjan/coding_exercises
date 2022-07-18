'''
You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm.
'''


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        n = n//2
        newNums = [0] * n

        for i in range(n):
            if i % 2 == 0:
                newNums[i] = min(nums[2*i], nums[2*i+1])
            else:
                newNums[i] = max(nums[2*i], nums[2*i+1])

        nums = newNums
        return self.minMaxGame(nums)
      
---------------------------------------------------------------
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:                
        l=nums
        while len(l)>1:
            is_min=True     
            tmp=[]
            for i in range(0, len(l), 2):
                if is_min:
                    tmp.append(min(l[i:i+2]))
                else:
                    tmp.append(max(l[i:i+2]))
                is_min=not is_min            
            l=tmp            
        return l[0]   
