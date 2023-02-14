'''
You are given a binary string s, and two integers num1 and num2. num1 and num2 are coprime numbers.

A ratio substring is a substring of s where the ratio between the number of 0's and the number of 1's in the substring is exactly num1 : num2.

For example, if num1 = 2 and num2 = 3, then "01011" and "1110000111" are ratio substrings, while "11000" is not.
Return the number of non-empty ratio substrings of s.

Note that:

A substring is a contiguous sequence of characters within a string.
Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.
'''



Intuition
Here, I use prefix sum to indicate what has been seen so far. If 0 is seen, I increase 
prefix by num2; if 1 is seen, I decrease prefix by num1. As a result, the number of prefix that 
has been seen in the past indicate how many subarrays with proper ratio ending at current index.


class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        ans = prefix = 0 
        freq = Counter({0 : 1})
        for ch in s:
            if ch == '0': prefix += num2
            else: prefix -= num1
            ans += freq[prefix]
            freq[prefix] += 1
        return ans 
