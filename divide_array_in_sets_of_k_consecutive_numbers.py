'''
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.
'''

from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d = Counter(nums)
        for x in sorted(nums):
            if x in d:
                for y in range(x, x + k):
                    if y in d:
                        d[y] -= 1
                        if d[y] == 0:
                            del d[y]
                    else:
                        return False
        return True
---------------------------------------------------------

from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums)%k != 0:
            # Quick response:
            # Reject because it is impossible to make sets
            return False
        
        if k == 1:
            # Quick response:
            # Accept with trivial solution by making set with each single element itself
            return True
        
        
        # Make number sorted in ascending order
        nums.sort()
        
        # dictionary:
        # key   : number
        # value : occurrence
        num_occ_dict = Counter( nums )
        
        
        # Make consecutive sets of size k from the smallest element
        for n in nums:
            
            occ_for_partition = num_occ_dict[n]
            
            if occ_for_partition == 0:
                continue
                
                
            for i in range(k):
                
                if num_occ_dict[n+i] < occ_for_partition:
                    # Reject:
                    # Either number (n+i) doesn't exist, or
                    # occurrence of (n+i) is not enough to make consecutive sets with k
                    return False
                
                # after making sets, update occurrence
                num_occ_dict[n+i] -= occ_for_partition
                
        return True
      
--------------------------------------------------------------------------------------------------      
