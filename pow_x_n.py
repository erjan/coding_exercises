#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

#just copied solution

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n == 1: return x
        if n < 0: return self.myPow(1/x, -n)
        result = self.myPow(x, n//2)
        result *= result
        if n%2 == 1: result *= x
        return result
