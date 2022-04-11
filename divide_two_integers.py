'''

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means 
losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only 
store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the 
quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


Example:
dividend = 100 and divisor = 7

Recursive Call #1 (dividend = 100)
7 * 2 * 2 * 2 = 56; break since 56 * 2 > 100
return 2^3 + call_2

Recursive Call #2 (dividend = 100 - 56 = 44)
7 * 2 * 2 = 28; break since 28 * 2 > 44
return 2^2 + call_3

Recursive Call #3 (dividend = 44 - 28 = 16)
7 * 2 = 14; break since 14 * 2 > 16
return 2 + call_4

Recursive Call #4 (dividend = 16 - 14 = 2)
return 0 since 2 < 7 --> dividend < divisor

Returning from the call stack we have:
result = 0 + 2 + 4 + 8 = 13

'''


def divide(self, dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    return sign * self._helper(abs(dividend), abs(divisor))
    
def _helper(self, dividend: int, divisor: int) -> int:
    if dividend < divisor:
        return 0
    exp = 0
    while dividend > (divisor << (exp+1)):
        exp += 1
    return (1 << exp) + self._helper(dividend - (divisor << exp), divisor)
  
  
  ------------------------------
  
  class Solution:
    """
        Logic:
            Since we have to avoid the usage of '/', '%', '*' operators so what we could do is,
                we could subtract the dividend by double multiplier of divisor until dividend becomes smaller than divisor.
            For example, dividend = 40, divisor = 3
                1. Can we take 3 out of 40? Yes! So, dividend => 40-3 = 37, divisor => 3*2 = 6
                2. Can we take 6 out of 37? Yes! So, dividend => 37-6 = 31, divisor => 6*2 = 12
                3. Can we take 12 out of 31? Yes! So, dividend => 31-12 = 19, divisor => 12*2 = 24
                4. Can we take 24 out of 19? No! Now we have to again follow the above approach by resetting the divisor.
                    So, dividend = 19, divisor = 3
                        And ans till now is, 1 + 2 + 4 = 7
                5. Can we take 3 out of 19? Yes! So, dividend => 19-3 = 16, divisor => 3*2 = 6
                6. Can we take 6 out of 16? Yes! So, dividend => 16-6 = 10, divisor => 6*2 = 12
                7. Can we take 12 out of 10? No! Now we have to again follow the above approach by resetting the divisor.
                    So, dividend = 10, divisor = 3
                        And ans till now is, 7 + 1 + 2 = 10
                8. Can we take 3 out of 10? Yes! So, dividend => 10-3 = 7, divisor => 3*2 = 6
                9. Can we take 6 out of 7? Yes! So, dividend => 7-6 = 1, divisor => 3*2 = 12
                6. Terminate the iterations because dividend < divisor.
                        And ans till now is, 10 + 1 + 2 = 13
    """

    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) > abs(dividend):
            return 0

        positive = (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0)

        if abs(divisor) == abs(dividend):
            return 1 if positive else -1

        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > 1:
            while dividend >= divisor:
                tempDivisor = divisor
                multiple = 1
                while dividend >= tempDivisor:
                    dividend -= tempDivisor
                    ans += multiple
                    multiple = multiple << 1
                    tempDivisor = tempDivisor << 1
        else:
            ans = dividend

        if not positive:
            ans = -ans

        ans = max(-2 ** 31, ans)
        ans = min(ans, 2 ** 31 - 1)

        return ans
      
-----------------------------

class Solution:
# @return an integer
def divide(self, dividend, divisor):
    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1
    if not positive:
        res = -res
    return min(max(-2147483648, res), 2147483647)
  
--------------------------------

for example, if we want to calc (17/2)

ret = 0;

17-2 ,ret+=1; left=15

15-4 ,ret+=2; left=11

11-8 ,ret+=4; left=3

3-2 ,ret+=1; left=1

ret=8;

class Solution:
# @return an integer
def divide(self, dividend, divisor):
    isMinus= ((dividend<0 and divisor >0) or (dividend>0 and divisor <0));
    ret=0;        
    dividend,divisor=abs(dividend),abs(divisor);
    c,sub=1,divisor;

    while(dividend >= divisor):
        if(dividend>=sub):
            dividend-=sub;
            ret+=c;
            sub=(sub<<1);
            c=(c<<1);
        else:
            sub=(sub>>1);
            c=(c>>1);
    
    if(isMinus):
        ret=-ret;
    return min(max(-2147483648,ret),2147483647);
