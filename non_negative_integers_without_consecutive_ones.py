'''
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.
'''


class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1, 2]
        for _ in range(30): fib.append(fib[-2] + fib[-1])
        
        ans = prev = 0
        for i in range(31, -1, -1): 
            if n & (1<<i): 
                ans += fib[i]
                if prev: return ans
                else: prev = 1
            else: prev = 0
        return ans + 1
      
----------------------------------------------------------------------
class Solution:
    def findIntegers(self, num: int) -> int:
        def is_valid(number):
            while number:
                if number&3==3:
                    return False
                number>>=1
            return True
        memo = {0:1}
        def nco(n, memo=memo):
            if n in memo:
                return memo[n]
                    #append(0) #append(01)
            res = nco(n>>1)+nco(n>>2)
            test = ((n>>2)<<2)+1
            if is_valid(test) and test>n:
                res-=1
            memo[n] = res
            return res
        return nco(num)
