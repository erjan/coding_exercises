'''
You are given an array of integers nums. Perform the following steps:

Find any two adjacent numbers in nums that are non-coprime.
If no such numbers are found, stop the process.
Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
Repeat this process as long as you keep finding two adjacent non-coprime numbers.
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.
'''

----------------------------------------------------------------------------------------------------------------------------------

Explanation
For each number a in input array A,
check if it is coprime with the last number b in res.
If it's not coprime, then we can merge them by calculate a * b / gcd(a, b).
and check we can continue to do this process.

Until it's coprime with the last element in res,
we append a at the end of res.

We do this for all elements a in A, and return the final result.

    def replaceNonCoprimes(self, A):
        res = []
        for a in A:
            while True:
                x = math.gcd(res[-1] if res else 1, a)
                if x == 1: break # co-prime
                a *= res.pop() // x
            res.append(a)
            
----------------------------------------------------------------------------------
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            while res and gcd(res[-1], num) > 1:
                num = lcm(res[-1], num)
                res.pop()
            res.append(num)
        return res
        return res
