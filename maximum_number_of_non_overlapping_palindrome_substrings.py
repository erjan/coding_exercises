'''
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 
 '''

This question is a combination of Palindromic Substring and Non-overlapping intervals
https://leetcode.com/problems/palindromic-substrings/
https://leetcode.com/problems/non-overlapping-intervals/

First find all palindromic substrings with length >= k in O(n*k) and store their start and end in an intervals list

Then find minumum number of intervals you need to remove to make the intervals array non overlapping in O(n) (intervals is already added in sorted order.)

def maxPalindromes(self, S: str, k: int) -> int:
    N, intervals, last, ans = len(S), [], -inf, 0
    for center in range(2 * N - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            if right + 1 - left >= k: 
                intervals.append((left, right + 1))
                break
            left -= 1
            right += 1
    for x, y in intervals:
        if x >= last:
            last = y
            ans += 1
        else:
            if y < last: last = y
    return ans
  
--------------------------------------------------------------------------------------------------------------
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            for length in range(k, k + 2):
                j = i - length
                if j < 0:
                    break
                if self.isPalindrome(s, j, i):
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[-1]
    
    
    def isPalindrome(self, s, j, i):
        left, right = j, i - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
