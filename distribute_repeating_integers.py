'''
You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:

The ith customer gets exactly quantity[i] integers,
The integers the ith customer gets are all equal, and
Every customer is satisfied.
Return true if it is possible to distribute nums according to the above conditions.
'''


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = {}
        for x in nums: freq[x] = 1 + freq.get(x, 0)
        
        vals = sorted(freq.values(), reverse=True)
        quantity.sort(reverse=True) # pruning - large values first  
        
        def fn(i): 
            """Return True if possible to distribute quantity[i:] to remaining."""
            if i == len(quantity): return True 
            seen = set()
            for k in range(len(vals)): 
                if vals[k] >= quantity[i] and vals[k] not in seen: 
                    seen.add(vals[k]) # pruning - unqiue values 
                    vals[k] -= quantity[i]
                    if fn(i+1): return True 
                    vals[k] += quantity[i] # backtracking
                    
        return fn(0)
