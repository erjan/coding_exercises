'''
You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.
'''

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        freq = [0] * 31
        for x in nums: freq[x] += 1
        
        masks = [0] * 31
        for x in range(1, 31): 
            if x == 1: masks[x] = 0b10
            else: 
                bits = 0
                xx = x
                for k in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29): 
                    while xx % k == 0: 
                        if (bits >> k) & 1: break # repeated factors 
                        bits ^= 1 << k
                        xx //= k
                    else: continue 
                    break 
                else: masks[x] = bits
                    
        @cache
        def fn(x, m): 
            """Return number of good subsets."""
            if x == 31: return int(m > 2)
            ans = fn(x+1, m)
            if freq[x] and masks[x]: 
                if x == 1: ans *= 2**freq[x]
                elif not m & masks[x]: ans += freq[x] * fn(x+1, m | masks[x])
            return ans % 1_000_000_007
        
        return fn(1, 0)
