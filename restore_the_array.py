'''
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.
'''


Let t be the max number of digits k can have.
For each position in the string we go at most t steps backward. If a number is possible which does not start with 0 and lies between 1 and k, we add that to our current count.

Time : O(length of the given string * max number of digits k can have) = O(length of the given string * 10)
Space : O(length of the given string)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        t = len(str(k))
        count = [0] * (n+1)
        count[0] = 1
        count[1] = 1
        for i in range(1, n):
            for j in range(t):
                if i-j >= 0 and 1 <= int(s[i-j:i+1]) <= k and s[i-j:i+1][0] != "0":
                    count[i+1] += count[i-j]
        return count[-1] % 1000000007
