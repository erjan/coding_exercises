'''
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the 
number of possible ways (out of the kn total ways) to roll the dice so the 
sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def helper(h, d, target):
            # if target is too small or if it is out of range
            if target <= 0 or target > (d * f):
                return 0
            if d == 1:
                return 1        # no need to check if target is within reach; already done before
            if (d, target) in h:
                return h[(d, target)]        # directly access from hash table
            res = 0
            for i in range(1, f + 1):
                res += helper(h, d - 1, target - i)       # check all possible combinations
            h[(d, target)] = res
            return h[(d, target)]
        
        h = {}
        return helper(h, d, target) % (10 ** 9 + 7)
      
-----------------------------------------------------------------------------------------------------
class Solution:
    def recur(self, n, k, target, lookup):
		# If target is not reachable then return 0
        if target <= 0 or target > n*k:
            return 0
		# If we are left with one dice and target is equal to any of the faces of dice then we have found a way so return 1
        if n == 1 and target <= k:
            return 1
        if (n, target) not in lookup:
            ways = 0
            for val in range(1, k+1):
				# Use the current dice, update the target as target - current face of dice and recur for remaining target with remaining dices
                ways += (self.recur(n-1, k, target-val, lookup))
            lookup[(n, target)] = ways
        return lookup[(n, target)] 
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.recur(n, k, target, {}) % ((10**9) + 7)
