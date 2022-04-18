'''
Given a single-digit integer d and two integers low and high, return 
the number of times that d occurs as a digit in all integers in the inclusive range [low, right].
'''

class Solution(object):
    def digitsCount(self, d, low, high):

        def check(n):
            res, a, b = 0, 1, 1
        
            while n > 0:
                if d == 0:
                    if n%10 == d:res += ((n + (10-d-1))//10 -1) * a + b
                    else: res += ((n + (10-d-1))//10 -1) * a
                else:
                    if n%10 == d:res += ((n + (10-d-0))//10 -1) * a + b
                    else: res += ((n + (10-d-1))//10 -0) * a
                b += n%10*a
                a *= 10
                n //= 10
            
            return res if d == 0 else res+1
    
        left = check(low-1)
                    
        right = check(high)
        return right - left
        
--------------------------------------------------------------------------
    def digitsCount(self, d, low, high):
        def count(N):
            if N == 0: return 0
            if d == 0 and N <= 10: return 0
            res = 0
            if N % 10 > d: res += 1
            if N / 10 > 0: res += str(N / 10).count(str(d)) * (N % 10)
            res += N / 10 if d else N / 10 - 1
            res += count(N / 10) * 10
            return res
        return count(high + 1) - count(low)
        
------------------------------------------------------------
Rather than counting the occurence of d from each number, we count the the occurent of d on each digit from 1 to the number.

Think about the form of the number abcTxyz and the current digit T, and we want to count the occurence of d on that position.
1. If T>d, then from 000 to abc, each corresponds to 1000 counts
2. If T==d, then from 000 to abc, each corresponds to 1000 counts except the last one, and xyz correponds to a count of abcT000 to abcTxyz, which is xyz+1 counts.
3. If T<d, then only from 000 to abc(excluded), each corresponds to 1000 counts.

Pay attention to d=0, for that case, we cannot start from 000, so we need to subtract them.

    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        def getCounts(num):
            res, step, n = 0, 1, 0
            while num>0:
                t = num%10 # the current digit
                num = num//10 # the num in front of the digit
                if t>d:# 
                    res+=(1+num-(d==0))*step
                elif t==d:# 
                    res+=(num-(d==0))*step+n+1
                else:
                    res+=(num-(d==0))*step
                n += t*step# update the number after the current digit
                step = 10*step# update the weight
            return res
        
        return getCounts(high)-getCounts(low-1)
        
------------------------------------------------------------------------------
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def calculate(num):
            num_eq = str(num).count(str(d))
            res = 0
            acc0 = 0
            acc1 = 1
            while num:
                num, di = divmod(num, 10)
                num_eq -= di == d
                res += di * num_eq * acc1 + di * acc0
                # to remove count of numbers with leading 0s
                if d == 0:
                    res -= acc1
                if di > d:
                    res += acc1
                acc0 = 10 * acc0 + acc1
                acc1 *= 10
            return res

        return calculate(high + 1) - calculate(low)
        
-------------------------------------------------------------------------------
if d != 0, and checking the number of times that 'd' occurs at position 'i':
Not considering all the edge cases here for clear explanation
str(number)[:i] +1: this is the number of times that 'd' appears at position 'i'.

10**(N-i-1) (N is len(str(number)): this is the duration of 'd' at position 'i'. For example 9999, 1 at second position from left will last 100 occurrences once it appears.

class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        
        def check(number):
            string = str(number)
            
            N = len(string)
            ans = 0
            for i in range(N):
                newstr = string[:i] + str(d) + ('9' * (N-i-1))
                freqs, extra = 1, 0
                if i != 0:
                    freqs = int(string[:i]) + 1
                if d == 0: freqs -= 1
                if int(newstr) > number:
                    # Handle edge case
                    freqs -= 1
                    newstr = string[:i] + str(d) + ('0' * (N-i-1))
                    if int(newstr) == number:
                        extra = 1
                    elif int(newstr) < number:
                        newstr = string[i+1:].lstrip('0')
                        extra = int(newstr) + 1
                # Freqs is determined by positions before digit i, after duration is
                # the digit number after i
                ans += freqs * (10**(N-i-1)) + extra
            return ans
        
        left = check(low-1)
                    
        right = check(high)
        return right - left
