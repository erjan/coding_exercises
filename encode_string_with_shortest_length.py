'''
Given a string s, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. k should be a positive integer.

If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.

 

Example 1:

Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
Example 2:

Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
Example 3:

Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
'''


For any s, you can either

Do not encode it
Or encode it to one string if possible
Or, split it into two, encode the two substring to their shortest possible length, and combine them
Pick up the shortest result from 1~3.
During this process, you should remember the best encoding result for all substrings so that it can be reused.

For #2, you can use LeetCode 459: Repeated Substring Pattern to find out whether the "s" is repeated or not, and how many times it is repeated:
"i=(s+s).find(s,1)"
"i" is the length of repeating pattern. If i>=len(s), then s is not repeated.

import functools
class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        i=(s+s).find(s,1)
        encoded=str(len(s)//i)+'['+self.encode(s[:i])+']' if i<len(s) else s
        splitEncoded=[self.encode(s[:i])+self.encode(s[i:]) for i in range(1,len(s))]
        return min(splitEncoded+[encoded],key=len)
      
      
------------------------------------------------------------------------------------------
Either don't encode s at all, or encode it as one part k[...] or encode it as multiple parts (in which case we can somewhere split it into two subproblems). Whatever is shortest. Uses @rsrs3's nice trick of searching s in s + s.

def encode(self, s, memo={}):
    if s not in memo:
        n = len(s)
        i = (s + s).find(s, 1)
        one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
        multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in xrange(1, n)]
        memo[s] = min([s, one] + multi, key=len)
    return memo[s]
  
  
----------------------------------------------------------
There's a DP inside a DP happening here :)
I could have replaced the string parameter with start and end indices, but didn't care to.

def encode(self, s: str) -> str:

	@lru_cache(None)
	def mincode(s):
		'''find the shortest representation of the string and return it'''
		if len(s) < 5: return s
		dp = [0]

		for i in range(1, len(s)):
			j = dp[i-1]
			while j > 0 and s[i] != s[j]: j = dp[j-1]
			if s[i] == s[j]: j += 1
			dp += [j]

		smallest = s
		for prefix_len in range(len(s), 0, -1):
			repeat_len = prefix_len - dp[prefix_len-1]
			if repeat_len < prefix_len and prefix_len % repeat_len == 0: # we have a repeat
				prefix_compressed = mincode(s[:repeat_len])
				left_compressed = f'{prefix_len // repeat_len}[{prefix_compressed}]'
			else:
				left_compressed = s[:prefix_len]

			right_compressed = mincode(s[prefix_len:])
			if len(left_compressed) + len(right_compressed) < len(smallest):
				smallest = left_compressed + right_compressed

		return smallest

	return mincode(s)

---------------------------------------------------------
class Solution:
    def encode(self, s: str) -> str:
        memo = dict()
        def collapse(i, j):
            temp = s[i:j+1]
            pos = (temp + temp).find(temp, 1)
            if pos >= len(temp):
                return temp
            return f'{len(temp)//pos}[{dfs(i, i+pos-1)}]'
        def dfs(i, j):
            if i == j:
                return s[i]
            if (i, j) not in memo:
                res = min([dfs(i,k) + dfs(k+1,j) for k in range(i, j)], key=lambda x: len(x))
                temp = collapse(i, j)
                memo[i, j] = min(res, temp, key=lambda x: len(x))
            return memo[i, j]
        return dfs(0, len(s)-1)
--------------------------------------------
class Solution:
    @functools.lru_cache(None)
    def encode(self, s: str) -> str:
        if len(s) <= 4:
            return s
        n = len(s)
        for seg in range(n, 1,-1):
            if n % seg == 0:
                if s == s[:n // seg] * seg:
                    return str(seg) + '[' + self.encode(s[:n // seg]) + ']'
        ret = s
        for i in range(1,n):
            new = self.encode(s[:i]) + self.encode(s[i:])
            if len(new) < len(ret):
                ret = new
        return ret
----------------------------------------------------------
We want minimum length of encoding for string s
let say it has lenght of n.
Our function dp(i,j) will return minimum length of encoding for s[i:j+1].
if lenght is less than 5, then we can return same string for minimum length of encoding for s[i:j+1].
if it is not, then firstly we try to take minimum of split of string and take minimum length of encoding for s[i:j+1].
ln = length of s[i:j+1] = j+1-i
for k in range(i, j):
if len(dp(i, k)) + len(dp(k+1, j)) < len(ret):
ret = dp(i, k) + dp(k+1, j)
then we check if the string can be broken down to repeated string and if we can achieve minimum length dp string by this.

from functools import lru_cache as l
class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        
        @l(None)
        def dp(i, j):
            # if i > j:
            #     return ""
            ret = s[i:j+1]
            if j + 1 - i < 5:
                return s[i:j+1]
            ln = j+1-i
            for k in range(i, j):
                if len(dp(i, k)) + len(dp(k+1, j)) < len(ret):
                    ret = dp(i, k) + dp(k+1, j)
            
            for k in range(1, ln):
                if ln%k == 0:
                    if s[i:i+k]*(ln//k) == s[i:j+1]:
                        if len(ret) > 2+len(str(ln//k))+len(dp(i, i+k-1)):
                            ret = str(ln//k)+"["+dp(i,i+k-1)+"]"
            # print(ret, s[i:j+1])
            return ret
        
        return dp(0, n-1)
      
      
