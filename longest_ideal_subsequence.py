'''
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
'''

'''
Explanation
dp[c] means the length of the longest ideal subsequence
ending with character c.

Iterate the character i in string s,
c can be the next character for string ending from i - k to i + k.
So that dp[i] = max(dp[i-k], dp[i-k+1] ... , dp[i+k]) + 1.

return the max(dp) as result.
'''

    def longestIdealString(self, s, k):
        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k : i + k + 1]) + 1
        return max(dp)
      
      
      
-------------------------------------------------------------------------------------------
	def longestIdealString(self, s: str, k: int) -> int:
	n = len(s)
	# Creating a list with
    # all 0's of size
    # equal to the length of string
    dp = [0] * n
     
    # Supporting list with
    # all 0's of size 26 since
    # the given string consists
    # of only lower case alphabets
    max_length = [0] * 26
 
    for i in range(n):
 
        # Converting the ascii value to
        # list indices
        curr = ord(s[i]) - ord('a')
        # Determining the lower bound
        lower = max(0, curr - k)
        # Determining the upper bound
        upper = min(25, curr + k)
        # Filling the dp array with values
        for j in range(lower, upper + 1):
 
            dp[i] = max(dp[i], max_length[j]+1)
        # Filling the max_length array with max
        # length of subsequence till now
        max_length[curr] = max(dp[i], max_length[curr])
 
    # return the max length of subsequence
    return max(dp)
