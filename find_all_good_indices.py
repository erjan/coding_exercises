'''
You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

The k elements that are just before the index i are in non-increasing order.
The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.
'''


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 2 * k:
            return []

        pref = [0] * len(nums)
        suff = [0] * len(nums)
        count = 0
		
		# descending order
        for i in range(len(nums)):
            pref[i] = count
            if i != 0 and nums[i] <= nums[i - 1]:
                count += 1
            else:
                count = 1

        count = 0
		# ascending order
        for j in range(len(nums) - 1, -1, -1):
            suff[j] = count
            if j != len(nums) - 1 and nums[j] <= nums[j + 1]:
                count += 1
            else:
                count = 1

        ans = []

        for i in range(len(suff)):
            if pref[i] >= k and suff[i] >= k:
                ans.append(i)

        return ans
        
-------------------------------------------------------------------------------------------------
def goodIndices(self, nums, k):

    n = len(nums)
    if k*2+1 > n : return []
    else :
        ans = [] 
        nonde = [0 for _ in range(n)]
        nonin = [0 for _ in range(n)]
        cur = nums[0]
        nonde[0] = 1 
        for i in range(1,n-k) :
            if cur >= nums[i] :
                nonde[i] = nonde[i-1]+1
    
            else :
                nonde[i] = 1 
            cur = nums[i]
                
        cur = nums[n-1]
        nonin[n-1] = 1 
        for i in range(n-2,k,-1) :
            if cur >= nums[i] :
                nonin[i] = nonin[i+1]+1
            else :
                nonin[i] = 1 
            cur = nums[i]
        
   
        
        for i in range(k,n-k) :
            
            if nonde[i-1] >= k and nonin[i+1] >= k : 
                ans += [i]
        return ans
