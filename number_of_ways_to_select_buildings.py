'''
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.
'''
class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        This solution could be optimized as i have seen people figured out
        O(1) space solution, however this is what i have reached which could be helpful!
        
        We iterate from the end of the string s, store the following:
        1 - count of zeros we have next -> this will be used to count amount of "10" we can make when we are currently on index of value "1"
        
        2 - count of ones we have next -> this will be used to count amount of "01" we can make when we are currently on index of value "0"
        
        3- count of "01" we have formed -> this will be helpful in the second iteration
        4- count of "10" we have formed -> this will be helpful in the second iteration
        
        """
        n = len(s)
        dp = [[0, 0, 0, 0]] * (n + 1) # [one count, zero count, "01" count, "10" count]
        for i in range(n - 1, -1, -1):
            prev_ones, prev_zero, prev_01, prev_10 = dp[i + 1]
            #if the current value i.e s[i] has value of '1' then this means we can make prev_10 + prev_zero of "10" sequence as currently we have "1" so we can match it with any of zeros we face later
            if s[i] == "1":
                dp[i] = [prev_ones + 1, prev_zero, prev_01, prev_10 + prev_zero]
            #same comment applies here but for zeros i.e we form "01" sequence 
            else:
                dp[i] = [prev_ones, prev_zero + 1, prev_01 + prev_ones, prev_10]
        
        res = 0
        for i in range(n - 2):
            #we are currently at zero so we need "10" only so we check how many sequences of "10" we have in front of us
            if s[i] == "0":
                res += dp[i][-1]
            #we are currently at one so we need "01" only so we check how many sequences of "01" we have in front of us
            else:
                res += dp[i][-2]
        return res
      
-------------------------------------------------------------------------------------
def numberOfWays(self, s: str) -> int:
        ways = one = zero = onesAfterZero = zerosAfterOne = 0
		for i in s:
			if i == '0':
				zero += 1
				zerosAfterOne += one
				ways += onesAfterZero
			else:
				one += 1
				onesAfterZero += zero
				ways += zerosAfterOne
		return ways
  
-----------------------------------------------------------------------------------------------------
class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count('0')
        ones = len(s) - zeros
        zeroPrefix = onePrefix = res = 0
        for c in s:
            if c == '0':
                res += onePrefix * (ones - onePrefix)
                zeroPrefix += 1
            else:
                res += zeroPrefix * (zeros - zeroPrefix)
                onePrefix += 1
        
        return res
