'''
Given an array of integers cost and an integer target, return the maximum integer you can paint under the following rules:

The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
The total cost used must be equal to target.
The integer does not have 0 digits.
Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return "0".
'''

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
        @cache
        def fn(x): 
            """Return max integer given target x."""
            if x == 0: return 0
            if x < 0: return -inf 
            return max(fn(x - c) * 10 + i + 1 for i, c in enumerate(cost))
        
        return str(max(0, fn(target)))
