'''
You are given four integers minLenght, maxLength, oneGroup and zeroGroup.

A binary string is good if it satisfies the following conditions:

The length of the string is in the range [minLength, maxLength].
The size of each block of consecutive 1's is a multiple of oneGroup.
For example in a binary string 00110111100 sizes of each block of consecutive ones are [2,4].
The size of each block of consecutive 0's is a multiple of zeroGroup.
For example, in a binary string 00110111100 sizes of each block of consecutive ones are [2,1,2].
Return the number of good binary strings. Since the answer may be too large, return it modulo 109 + 7.

Note that 0 is considered a multiple of all the numbers.
'''



This problem actually reduces to solving the diophantine equation z*zeroGroup + w*oneGroup = i for each i in the closed interval [minLength, maxLength].

This equation has integer solutions on if i is a multiple of gcd(zeroGroup, oneGroup). All i that are not are pruned by if i%g: continue. Results vary though. For example, if oneGroup = 12and zeroGroup = 18, approx 80% the iterations are pruned, but for oneGroup = 12andzeroGroup = 18, none are pruned.

class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        
        dp, g = [1]+[0] * maxLength, gcd(oneGroup,zeroGroup)

        for i in range(1, maxLength + 1):

            if i%g:continue             #<--- no solutions if i%g != 0

            dp[i] += ((dp[i - oneGroup ] if i >= oneGroup  else 0)+
                      (dp[i - zeroGroup] if i >= zeroGroup else 0))

            dp[i]%= 1000000007

        return sum(dp[minLength : maxLength + 1]) % 1000000007
-----------------------------------------------------------------------------
class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        dp = [0] * (maxLength + 1)
        dp[0] = 1
        MOD = 1_000_000_007
        for i in range(maxLength + 1):
            if dp[i]:
                if i + oneGroup <= maxLength:
                    dp[i + oneGroup] = (dp[i] + dp[i + oneGroup]) % MOD
                if i + zeroGroup <= maxLength:
                    dp[i + zeroGroup] = (dp[i] + dp[i + zeroGroup]) % MOD
        return sum(dp[minLength:]) % MOD
--------------------------------------------------------------------------------------------------------------------
class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        @cache
        def dp(i):
            if i > maxLength:
                return 0
            res = minLength <= i <= maxLength
            return (res + dp(i + oneGroup) + dp(i + zeroGroup)) % MOD

        MOD = 1_000_000_007
        return dp(0)
      
      
