'''
There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.

Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 109 + 7.

Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.

 
 '''

 def countHousePlacements(self, n):
        a, b, mod = 1, 1, 10**9 + 7
        for i in range(n):
            a, b = b, (a + b) % mod
        return b * b % mod
      
--------------------------------------------
class Solution:
    def countHousePlacements(self, n: int) -> int:
        
        
        @lru_cache(None)
        def rec(i, k):
            
            # i is the index of the house 
            # k is the state of last house, 1 if there was a house on the last index else 0
            
            if i>=n:
                return 1
            
            elif k==0:
                return rec(i+1,1) + rec(i+1,0)
            
            else:
                return rec(i+1,0)
        
        
        
        #l1 are the combinations possible in lane 1, the final answer will be the square 
		#of of l1 as for every combination of l1 there will be "l1" combinations in lane2.
        
        l1 = rec(1,0) + rec(1,1)
        
        
        mod = 10**9 +7
        return pow(l1, 2, mod) #use this when there is mod involved along with power 
