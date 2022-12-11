'''
You are given a string s consisting of only lowercase English letters. In one operation, you can:

Delete the entire string s, or
Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

Return the maximum number of operations needed to delete all of s.
'''

    def deleteString(self, s: str) -> int:
        n = len(s)
        if n == 1: return 1
		if (len(set(s)) == 1): return n
        
        @cache
        def dp(i):
            if i == n - 1: return 1
            res = 0
            l = (n - i) // 2
            temp = ""
            for j in range(1, l + 1):
                temp += s[i + j - 1]
                if temp == s[i+j:i+2*j]:
                    res = max(res, dp(i+j))
            return res + 1        
        
        return dp(0)
