'''
You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.
'''

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ii = val = 0 
        ans = inf
        loc = [] # location of 1s
        for i, x in enumerate(nums): 
            if x: 
                loc.append(i)
                m = (ii + len(loc) - 1)//2 # median 
                val += loc[-1] - loc[m] - (len(loc)-ii)//2 # adding right 
                if len(loc) - ii > k: 
                    m = (ii + len(loc))//2 # updated median 
                    val -= loc[m] - loc[ii] - (len(loc)-ii)//2 # removing left 
                    ii += 1
                if len(loc)-ii == k: ans = min(ans, val) # len(ones) - ii effective length
        return ans 
      
-----------------------------------------------------------------------------------------------
