
'''

Given an integer n, return whether its prime factors only include 2, 3 or 5.
'''

class Solution:
    def solve(self, n):
        num = n
        if num == 0: return False
        while num % 5 == 0: num /= 5
        while num % 3 == 0: num /= 3
        while num % 2 == 0: num /= 2
        return num == 1


        
        
        
