'''
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
'''

class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        def helper(screen, clipboard):
            if (screen, clipboard) in cache: return cache[(screen, clipboard)]
            if screen == n: return 0
            if screen > n: return float("Inf")
            
            copy_paste = helper(screen+screen, screen) + 2
            paste = float("Inf")
            if clipboard:
                paste = helper(screen + clipboard, clipboard) + 1

            cache[(screen, clipboard)] = min(copy_paste, paste)    
            return cache[(screen, clipboard)]
        
        return helper(1, 0)
      
--------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minSteps(self, n: int) -> int:
        """
        Find the pattern here, before seeing the solution
        1. A > 0
        2. AA > 2
        3. AAA > 3
        4. AAAA > 4
        5. AAAAA > 5
        
        6. AAAAAA > 5 
        
        7. AAAAAA > 7
        
        9. AAAAAAAAA > 6
        
        ........
        
        15. AAAAAAAAAAAAAAA > 8
        
        What do you see?
        
        Can you find the relation here?
        1. even number can be achieved by copy-pasting minSteps(n // 2)
        2. Odd numbers don't follow this pattern
            1. For minimum steps some odd numbers need to copy-paste 'A' upto n.
            2. For minimum steps some odd numbers look for its divisor.
        
        if you can see this pattern, then you have covered all the logic needed for this problem
        1. even number
        2. Prime number
        3. Odd number (with divisors)
        """
        memo = [0] * (n + 1)
        
        def return_divisors(n):
            """
            find all the divisors of a number
            """
            divisors = set()
            i = 2
            while i * i <= n:
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                i += 1
            return divisors
        
        def recurse(n):
            """
            recurse top - down fashion with memorization
            """
            if n <= 1:
                return 0
            
            if memo[n]:
                return memo[n]
            
            else:
                # even number can be achieved by copy and paste (2 operations) of its n / 2 steps
                if n % 2 == 0:
                    memo[n] = self.minSteps(n // 2) + 2
                
                # odd numbers can be a combination of prime and non-prime numbers
                else:
                    divisors = return_divisors(n)
                    if divisors:
                        memo[n] = min(self.minSteps(i) + (n // i) for i in divisors)
                    
                    # if there is no divisors, then it is a prime number
                    # can only be achieved by coping 'A' one time and paste n - 1 time
                    else:
                        memo[n] = n
  
            return memo[n]
        
        return recurse(n)
    
