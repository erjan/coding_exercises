'''
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.
'''

Let's look at a few examples:

Input           Output
55627    ->     55599
55427    ->     49999
99996    ->     89999 
100         ->    99
From the above examples we can see that if a number is not monotone increasing digits, we will need to convert as many digits as posible to 9 and decrease the digit before the 9s by 1. But how to decide which digit to decrease by 1?

If we try to tranverse the digits from left to right, there are many different cases we need to consider. But if we tranverse the digits from right to left, it is very straightforward! Whenever a digit is smaller than a digit to its left, decrease its left digit by 1 and convert all the digits from here until the end to 9.

To make the digits easy to access, tranverse, and modify, I converted the number into a list of integers.

class Solution(object):
    def monotoneIncreasingDigits(self, n):
        # First, handle the single-digit cases.
        if n < 10:
            return n

		# Convert the number into a list of integers
        l = []
        for _,c in enumerate(str(n)):
            l.append(int(c))
        n = len(l)

		# Tranverse from right to left 
        for i in range(n-1,0,-1):
            if l[i] < l[i-1]:
                l[i-1] -= 1
                for i in range(i,n):
                    l[i] = 9
        
		# Convert the list back to a number
        return int("".join([str(x) for x in l]))
    
-----------------------------------------------------------------------------    
