'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
'''


Explanation
Two pointer to same direction, fast pointer check new character, slow pointer shorten substr
Use a little math (n-j) to count possible valid substrings
Check comments for more detail
Implementation
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = 0                        # counter for letter a/b/c
        ans, i, n = 0, 0, len(s)             # i: slow pointer
        for j, letter in enumerate(s):       # j: fast pointer
            if letter == 'a': a += 1         # increment a/b/c accordingly
            elif letter == 'b': b += 1
            else: c += 1
            while a > 0 and b > 0 and c > 0: # if all of a/b/c are contained, move slow pointer
                ans += n-j                   # count possible substr, if a substr ends at j, then there are n-j substrs to the right that are containing all a/b/c
                if s[i] == 'a': a -= 1       # decrement counter accordingly
                elif s[i] == 'b': b -= 1
                else: c -= 1
                i += 1                       # move slow pointer
        return ans    
      
----------------------------------------------------------------------------------------------------
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count, left = 0, 0
        map = {x:0 for x in "abc"}
        
        for right in range(0,len(s)):
            map[s[right]] += 1
            
            while map["a"] and map["b"] and map["c"]:
                map[s[left]] -= 1
                left += 1
            
            count += left
            
        return count
