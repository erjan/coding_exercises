'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
		res = []
        for c in product('abc', repeat=n):
            flag = True
            for i in range(1, len(c)):
			    # Check if c[i] is not equal c[i-1] as mentioned in the problem
                if c[i] == c[i-1]:
                    flag = False
            if flag:
                res.append(''.join(f for f in c))
				
		# Check for boundary conditions
        if k > len(res):
            return ""
        else:
            return res[k-1]
