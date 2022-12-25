'''
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
'''


we have to find length of largest window/substring where we have

occurences of 'a' in window/substring <= (total occurences of 'a' in s) - k
occurences of 'b' in window/substring <= (total occurences of 'b' in s) - k
occurences of 'c' in window/substring <= (total occurences of 'c' in s) - k
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ra = s.count('a') - k
        rb = s.count('b') - k
        rc = s.count('c') - k
        
		# if any of them is less than 0, it means there are less than k occurences of a character.
        if any(i < 0 for i in [ra, rb, rc]):
            return -1
        
        hm = defaultdict(int)
        l = j = res = 0
        
        for i in s:
            hm[i] += 1
            l += 1
            
            while hm['a'] > ra or hm['b'] > rb or hm['c'] > rc:
                hm[s[j]] -= 1
                l -= 1
                j += 1
            
            res = max(res, l)
        
        return len(s) - res
    
------------------------------------------------------------------------------------------------------------------    
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1

        cnts = {c: 0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            cnts[c] += 1
            while cnts[c] > limits[c]:
                cnts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return len(s) - ans
