'''
You are given an array nums that consists of positive integers.

The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.

For example, the GCD of the sequence [4,6,16] is 2.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
Return the number of different GCDs among all non-empty subsequences of nums.
'''


import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_n = max(nums) + 1
        seen = set(nums)
        
        ans = 0
        for k in range(1, max_n): # iterate candidate k
            gcd = 0
            for multiple in range(k, max_n, k): # compute gcd of all array multiples of k
                if multiple in seen:
                    gcd = math.gcd(gcd, multiple)
            if gcd == k: # check the candidate 
                ans += 1
        return ans
      
------------------------------------------------------------------------------------------------------------------      

Algorithm Steps:

Iterate over the possible GCD values (from 1 to maximal value in nums)
If current gcd_candidate is indeed a GCD of values from nums - add it to the GCD options counter
Hopefully it makes sense :)
But how would we know if our gcd_candidate is indeed a GCD?
Let's iterate over all values from nums that are multiples of candidate - and calculate GCD for them iteratevly - it we reach a state that the GCD is our candidate, then it's a valid GCD value!

Please upvote if you find the explanation helful! :)

Code:

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        gcd_options         = 0
        nums_set            = set(nums)
        max_possible_gcd    = max(nums_set)
        def get_candidate_multiples_from_nums(gcd_candidate, max_possible_gcd):
            for candidate_multiple in range(gcd_candidate, max_possible_gcd+1, gcd_candidate):
                if candidate_multiple in nums_set:                    
                    yield candidate_multiple
        def is_candidate_a_gcd_of_numbers_from_num(gcd_candidate, max_possible_gcd):
            current_gcd         = 0
            for candidate_multiple in get_candidate_multiples_from_nums(gcd_candidate, max_possible_gcd):
                if not current_gcd:
                    current_gcd = candidate_multiple
                else:
                    current_gcd = gcd(candidate_multiple, current_gcd)
                if current_gcd == gcd_candidate:
                    return 1
            return 0
        for gcd_candidate in range(1, max_possible_gcd+1):
            if is_candidate_a_gcd_of_numbers_from_num(gcd_candidate, max_possible_gcd):
                gcd_options += 1                        
        return gcd_options
      
---------------------------------------------------------
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        Time Complexity: O( len(nums) + sum( log(m) (m-d)//d  for d in range(1,m+1) ) )~= O(N + mlog(m)^2)
        where m is max(nums)
        
        """

        m, nums, count = max(nums), set(nums), 0
        
        # check possible divisors one-by-one
        for d in range(1,m+1):
            g = 0 # current gcd
            for n in range(d, m+1, d): # find if d can be a gcd
                if n in nums:
                    g = gcd(g,n) # add n into sequence and update gcd
                    if g == d: # check if d is a gcd
                        count += 1
                        break # look for the next divisor candidate
        
        return count
