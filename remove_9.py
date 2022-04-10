'''

Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...

Now, you will have a new integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...].

Given an integer n, return the nth (1-indexed) integer in the new sequence.

'''

def newInteger(self, n):
    ans = ''
    while n:
        ans = str(n%9) + ans
        n /= 9
    return int(ans)
  
  
  --------------------
  class Solution:
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        out = []
        
        while n > 0:
            out.append(str(n % 9))
            n //= 9
            
        out.reverse()
        return int(''.join(out))
