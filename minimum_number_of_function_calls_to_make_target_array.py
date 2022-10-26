'''
You are given an integer array nums. You have an integer array arr of the same length with all values set to 0 initially. You also have the following modify function:


You want to use the modify function to covert arr to nums using the minimum number of calls.

Return the minimum number of function calls to make nums from arr.

The test cases are generated so that the answer fits in a 32-bit signed integer.
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        
        double = 0
        
        for n in nums:
            cur_double = 0
            while n != 0:
                if n%2: 
                    n -= 1
                    steps += 1
                else:
                    n //= 2
                    cur_double += 1
            double = max(double, cur_double)
            
        
        return steps + double
