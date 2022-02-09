'''
Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?
'''

class Solution:
    def solve(self, num):
        num = str(num)

        l = len(num)
        mid = 0
        if l %2 != 0:
            mid = l//2
            print('mid %d ' % mid)

            f = num[:mid]
            s = num[(mid+1):]
            print(f)
            print(s)
            
            return f[::-1] == s
        else:

            mid = l//2 
            f = num[:(mid)]
            s = num[mid:]
            print(f)
            print(s)
            return f[::-1] == s
