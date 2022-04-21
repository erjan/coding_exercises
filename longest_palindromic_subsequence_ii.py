'''
A subsequence of a string s is considered a good palindromic subsequence if:

It is a subsequence of s.
It is a palindrome (has the same value if reversed).
It has an even length.
No two consecutive characters are equal, except the two middle ones.
For example, if s = "abcabcabb", then "abba" is considered a good palindromic subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive characters) are not.

Given a string s, return the length of the longest good palindromic subsequence in s.

 

Example 1:

Input: s = "bbabab"
Output: 4
Explanation: The longest good palindromic subsequence of s is "baab".
Example 2:

Input: s = "dcbccacdb"
Output: 4
Explanation: The longest good palindromic subsequence of s is "dccd".
'''

Approach:

Start with pointers i (at the start of s) and j (at the end of s) and prev_char ('@' a dummy character)
Each step you have a few choices:

If s[i] or s[j] equals prev_char then move that pointer inwards one step
because the subesquence is not allowed to have two equal consecutive characters

If s[i] equals s[j] then add 2 to the result, move both pointers inwards,
and update prev_char

If s[i] does not equal s[j] then consider moving i or moving j
return the option that produces the best result

As an exit condition, if i is ever greater than or equal to j then return zero
because we cannot use the same character twice.


def longestPalindromeSubseq(self, s: str) -> int:

	@functools.lru_cache(None)
	def helper(i, j, prev_char):
		if i >= j:
			return 0
		if s[i] == s[j] and s[i] != prev_char:
			return 2 + helper(i+1, j-1, s[i])
		return max(helper(i+1, j, prev_char), helper(i, j-1, prev_char))

	res = helper(0, len(s) - 1, '@')
	helper.cache_clear()
	return res
---------------------------------------------------------------------------

Idea

We can use DP to solve this problem. Approach from two sides to the middle and keep track of the best answer for a given range [l, r].

Interestingly DP with lru_cache gives me TLE. I had to write memo manually.


Complexity

Time complexity: O(N^2)
Space complexity: O(N^2)

Python

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def dp(l, r, prev):
            if (l, r, prev) not in memo:
                if l >= r:
                    return 0
                if s[l] == s[r] and (s[l] != prev):
                    return 2 + dp(l + 1, r - 1, s[l])
                memo[(l, r, prev)] = max(dp(l + 1, r, prev), dp(l, r - 1, prev))
            return memo[(l, r, prev)]
        
        return dp(0, len(s) - 1, '')
------------------------------------------------------------------------------------

The following is a solution with O(n^2) time complexity but not O(n^2 * |c|) where |c| is the size of lowercase character set.

class Storage:
    """
    We maintain two longest palindromic subsequences.
    The first one is of length `l_first` and with left/right-most character `c_first`.
    The second one is of length `l_second` and with left/right-most character `c_second`.
    To make our coding easier, we ensure that `l_first` >= `l_second` holds.
    
    Why should we maintain two results?
    The reason is simple:
        since we need to prevent two equal consecutive characters,
        it is intuitive to maintain two result with different left/right-most characters (i.e. `c_first` != `c_second`).
        Thus when we are doing dynamic programming for any characters,
        it is always possible for us to choose at least one of the two results to calculate the right answer.
    """
    def __init__(self, c_first, l_first, c_second, l_second):
        self.c_first = c_first
        self.l_first = l_first
        self.c_second = c_second
        self.l_second = l_second
    
    """
    When we have a new palindromic subsequence of length `l` and with left/right-most character `c`,
    we need to update our stored results:

        - If `c_first` == `c`, we can only update (`l_first`, `c_first`) to (`l`, `c`) if the latter is optimal.
        - If `c_second` == `c`, we can only update (`l_second`, `c_second`) to (`l`, `c`) if the latter is optimal.
        - Otherwise, we can choose two best ones from (`l_first`, `c_first`), (`l_second`, `c_second`) and (`l`, `c`).
    """
    def update(self, c, l):
        if self.c_first == c:
            if l > self.l_first:
                self.c_first, self.l_first = c, l
        elif self.c_second == c:
            if l > self.l_second:
                self.c_second, self.l_second = c, l
                if self.l_second > self.l_first:
                    self.c_first, self.l_first, self.c_second, self.l_second = self.c_second, self.l_second, self.c_first, self.l_first
        else:
            if l > self.l_first:
                self.c_first, self.l_first, self.c_second, self.l_second = c, l, self.c_first, self.l_first
            elif l > self.l_second:
                self.c_second, self.l_second = c, l

    """
    Return a copy of the current results.
    """
    def duplicate(self):
        return Storage(self.c_first, self.l_first, self.c_second, self.l_second)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(l: int, r: int) -> Storage:
            if l >= r:
                return Storage("", 0, "", 0)
            if s[l] == s[r]:
                # Update the result in dp(l+1, r-1) if it does not violate the consecutive character rule
                store = dp(l + 1, r - 1).duplicate()
                if s[l] != store.c_first:
                    store.update(s[l], store.l_first + 2)
                if s[l] != store.c_second:
                    store.update(s[l], store.l_second + 2)
            else:
                # Choose two best results from the four in dp(l+1, r) and dp(l, r-1)
                store = dp(l + 1, r).duplicate()
                another = dp(l, r - 1)
                store.update(another.c_first, another.l_first)
                store.update(another.c_second, another.l_second)

            return store

        answer = dp(0, len(s) - 1)
        dp.cache_clear()
        return answer.l_first
-------------------------------------------------------------------------------------------

If you've already done https://leetcode.com/problems/longest-palindromic-subsequence/, then this solution is a very small change. Let's start by looking at the O(n ^ 2), O(n) space solution to LPS:

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:        
        n = len(s)
        prev = [0] * n
        
        for i in range(n - 1, -1, -1):
            curr = [0] * n
            curr[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    curr[j] = 2 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return curr[-1]
At each step of LPS, if our pointers are pointing to the same character, we look at prev[j - 1] (i.e., look "in" one step from the current LPS). The reason we set curr[i] = 1 in each loop is for the base case of i = j, which is a trivial palindrome of length 1.

Now let's move to LPS II:

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [(0, None)] * n
        for i in range(n - 1, -1, -1):
            curr = [(0, None)] * n
            for j in range(i + 1, n):
                if s[i] == s[j] != prev[j - 1][1]:
                    curr[j] = (2 + prev[j - 1][0], s[i])
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        
        return curr[-1][0]
There are only 3 changes from LPS:

We memoize a tuple of (length, last char) in the memo table
s[i] == s[j] adds an additional constraint != prev[j - 1][1] to check whether we can use the "enclosing" palindromic characters
Our palindromes have to be even length, so we remove the line that sets curr[i] = 1
One major area of question is around the else statement, which is simply

                else:
                    curr[j] = max(prev[j], curr[j - 1])
It's not immediately clear why this works. Let's look at an example using the string 'ccaabbbbcc'. In this case, we encounter the else statement above when i = 2

prev = [(0, None), (0, None), (0, None), (0, None), (0, None), (2, 'b'), (2, 'b'), (2, 'b'), (2, 'b'), (2, 'c')]
curr = [(0, None), (0, None), (0, None), (2, 'a'), (2, 'a'), (2, 'b'), (2, 'b'), (2, 'b'), (2, 'b'), (2, 'c')]
i = 2
j in range(3, 10)

Here, we favor pulling down (2, 'b') instead of pulling forward (2, 'a'). Recall from above that we need to remember when we look at prev[j], curr[j - 1] we're looking at the LPS "top down" cases T(i + 1, j) and T(i, j - 1). The reason we don't care which one we select (assuming both LPS have the same length) is that the "memory" of this DP problem is only 1. Let's assume that we did care which one we picked. That would imply that there exists some substring x: such that LPS(abxba) > LPS(abxba), which can't be true.

Just to reiterate, the key to understanding this bottom up approach is to note that the topological order of solving problems is right to left on the string.
----------------------------------------------------------------------------------------------------------

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
		"""
		dp[i][j] is a tuple of the length of the longest good palindrome substring between i and j (inclusive) and the ending char.
		if s[i]==s[j] and it is different from dp[i+1][j-1]'s ending char, then dp[i][j] = dp[i+1][j-1]+2;
		otherwise dp[i][j] is the max of dp[i+1][j], dp[i][j-1] and dp[i+1][j-1].
		"""
        n = len(s)
        dp = [[(0, '')]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i]== s[j] and dp[i+1][j-1][1] != s[i]:
                    dp[i][j] = (dp[i+1][j-1][0] + 2, s[i])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1], key=lambda x: x[0])
        return dp[0][n-1][0]
        
        

      
      
