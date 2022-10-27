'''
Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 for n > 2.
It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
'''

def findMinFibonacciNumbers(self, k):
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res
        
-----------------------------------------------------------------------------------------
To find the decomposition into the sum of Fibonnaci numbers we will iteratively (recursively) take the greatest Fibonnaci number that is smaller than the current reamainder and return the 1 plus the decomposition of the new remainder. 1 corresponds to the new found Fibonnaci that, and the recursion will descend just until we compute the whole solution.
Cheers.

class Solution:
    def findMinFibonacciNumbers(self, k):
        n1 = 1
        n2 = 1
        while n2 < k:
            temp = n2
            n1, n2 = n2, n1+n2
        if n2==k:
            return 1
        return self.findMinFibonacciNumbers(k-n1)+1
      
----------------------------------------------------------------------------------------------------------
        d=[0,1]
        i=1
        while d[i]<=k:
            i+=1
            d+=[d[i-1]+d[i-2]]
        s=0
        ct=0
        d.remove(d[-1])
        for i in d[::-1]:
            s+=i
            if s>k:
                s=s-i
            else:
                ct+=1
                if s==k:
                    return ct
                  
--------------------------------------------------------------------------------------
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_sq = [1, 1]
        while fib_sq[-1] + fib_sq[-2] <= k:
            fib_sq.append(fib_sq[-1]+fib_sq[-2])
        counter = 0
        for i in range(len(fib_sq)-1, -1, -1):
            if fib_sq[i] <= k:
                counter += 1
                k -= fib_sq[i]
        return counter
