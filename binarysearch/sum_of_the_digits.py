'''
Given a positive integer num, return the sum of its digits.

Bonus: Can you do it without using strings?
'''

class Solution:
    def solve(self, num):


        total = 0

        while num:

            total += num%10
            num = num//10
        
        print(total)
        return total
        
