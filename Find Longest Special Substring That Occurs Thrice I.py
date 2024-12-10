'''
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.
'''

class Solution:
    def maximumLength(self, s: str) -> int:
        

        def is_special(x):
            return len(set(x)) == 1
        

        n = len(s)
        res = -1
        for i in range(1,n+1):
            q = {}

            for j in range(n-i+1):
                substr = s[j:i+j]

                if is_special(substr):
                    q[substr] = q.get(substr,0)+1
                    if q[substr]>=3:
                        res = max(res,i)
        return res
