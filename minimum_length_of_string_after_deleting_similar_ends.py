'''
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
'''

class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1    # left and right pointers
        while l < r and s[l] == s[r]:
            ele = s[l]
            while s[l] == ele and l < r:
                l += 1
            if l == r:  return 0    # the entire string will be wiped out
            while s[r] == ele:
                r -= 1
        return r - l + 1
      
---------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumLength(self, s: str) -> int:
        while(len(s)>1 and s[0]==s[-1]):
            s=s.strip(s[0])
        else:
            return len(s)
          
------------------------------------------------------------------------------------------------------------------------------------------
def minimumLength(self, s: str) -> int:
	if len(s) <= 1:
		return len(s)

	while len(s) > 1 and s[0] == s[-1]:
		i = 0
		while i + 1 < len(s) and s[i] == s[i + 1]:
			i += 1

		j = len(s) - 1
		while j - 1 > 0 and s[j] == s[j - 1] and j != i:
			j -= 1

		s = s[i + 1:j]

	return len(s)
