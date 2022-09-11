'''
Given a string s and an integer k, return the length of 
the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
'''


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = collections.Counter(s)
        st = 0
        maxst = 0
        for i, c in enumerate(s):
            if cnt[c] < k:
                maxst = max(maxst, self.longestSubstring(s[st:i], k))
                st = i + 1
        return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))
      
-------------------------------------------------------------------------------------
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        if k > len(s):
            
            # k is too large, larger than the length of s
            # Quick response for invalid k
            return 0
        
        
        # just for the convenience of self-recursion
        f = self.longestSubstring
        
        ## dictionary
        # key: unique character
        # value: occurrence
        char_occ_dict = collections.Counter(s)
        
        # Scan each unique character and check occurrence
        for character, occurrence in char_occ_dict.items():
            
            if occurrence < k:
                
                # If occurrence of current character is less than k,
                # find possible longest substring without current character in recursion
                
                return max( f(sub_string, k) for sub_string in s.split(character) )
        
        # -------------------------------
        
        # If occurrences of all characters are larger than or equal to k
        # the length of s is the answer exactly
        
        return len(s)
