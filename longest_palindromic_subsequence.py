'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t=s[::-1]  #idea is reverse t and compare t with s
        
        dp=[[0 for _ in range(len(s)+1)] for __ in range(len(s)+1)] #create dp array
        
        for i in range(1,len(s)+1):  #start from1 to match dp size, but compare s[i-1] and t [j-1]
            for j in range(1,len(s)+1):
                if s[i-1]!=t[j-1]:  #if not equal what do we want to do ? the question is asking to
				#find the longest palindromic subsequence and char @ S !=char @T, 
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j]) #so we just take the max previous value we found before
                else:                                     #now they are equal so our palindrome can be bigger
                    dp[i][j]=1+dp[i-1][j-1]   #take previous + 1 
        return dp[-1][-1]
      
--------------------------------------------------------------------------------------------------------------------
"""

516. Longest Palindromic Subsequence


this is a subsequence rather than subarray or substring

subarray or substring -> you can use sliding window from the middle
subsequence can't start with middle, can use dp.

we can start with a left and right pointer
at index 0 and len(s) -1.
    
    c  d  c  d  c       
    0  1  2  3  4        
   -5 -4 -3 -2 -1     left = 0 right = 4
    ^.          ^     s[left] == s[right]? true  ++left --right   +2
       ^.    ^.       s[left] == s[right]? true  ++left --right   +2
         ^^           

two cases:
two chars identical - gained 2 chars. can shrink both sides towards middle
different - shrink right or left pick the max of the two paths

base cases:
is left > right? return 0 and unwind call stack
left = right? must be odd, a single palindrone is a palindrone, so return 1, unwind
call stack


memoization reduces time complexity from O(n^3) to O(n^2)
space complexity: O(n^2)

"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dfs(left, right) -> int:
            if left > right:
                return 0
            if left == right:
                return 1
            
            if s[left] == s[right]:
                # case 1: shrink left and right, recurse 
                # the longest window must be at least 2
                # characters more
                return dfs(left+1, right-1) + 2
            else:
                # case 2: the answer must be the max of either of these paths
                return max(dfs(left+1, right), dfs(left, right-1)) + 0 
                
        return dfs(0, len(s) - 1)
