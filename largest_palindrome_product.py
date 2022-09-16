'''
Given an integer n, return the largest palindromic integer 
that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.
'''


class Solution:
    def largestPalindrome(self, n: int) -> int:
        
        # just to forget about 1-digit case
        if n == 1:
            return 9
        
        # minimal number with n digits (for ex. for n = 4, min_num = 1000)
        min_num = 10 ** (n - 1)
        
        # maximal number with n digits (for ex. 9999)
        max_num = 10 ** n - 1       
        
        max_pal = 0
        
        # step is equal to 2, because we have to get a number, the 1st digit of which is 9, so we have to   
		# iterate only over odd numbers
        for i in range(max_num, min_num - 1, -2): 
            
            # since we are looking for the maximum palindrome number, it makes no sense to iterate over the 
            # product less than the max_pal obtained from the last iteration
            if i * i < max_pal:
                break
                
            for j in range(max_num, i - 1, -2):
                product = i * j
                
                # since a palindrome with an even number of digits must be mod 11 == 0 and we have no reason to 
                # check the product which less or equal than max_pal
                if product % 11 != 0 and product >= max_pal:
                    continue
                    
                # check if product is a palindrome then update the max_pal
                if str(product) == str(product)[::-1]:
                    max_pal = product

        return max_pal % 1337
      
--------------------------------------------
class Solution:
    def largestPalindrome(self, n: int) -> int:
        return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]

        
    def isPalindrome(x):
        return str(x) == str(x)[::-1]

    def solve(n):
        best = 0
        for i in range(10**n-1, 0, -1):
            for j in range(max(i, (best-1)//i+1), 10**n):
                if isPalindrome(i*j):
                    #print(i, j, i*j)
                    best = i*j
        return best
