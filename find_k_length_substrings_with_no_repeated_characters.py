'''
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
'''

Idea
Common sliding window problem. We need the count of duplicates for a specific window. If the count of a letter is 2, then we add the letter to more_than_one. We remove the head of the window and if removing the count of the letter is one again, we remove it from more_than_one. res is incremented when more_than_one is empty and the length of the str is k.

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        count = defaultdict(int)
        N = len(s)
        res = j = 0
        more_than_one = set()
        
        for i in range(N):
            count[s[i]] += 1
            if count[s[i]] == 2:
                more_than_one.add(s[i])
                
            if i-j==k:
                count[s[j]] -= 1
                if count[s[j]] == 1:
                    more_than_one.remove(s[j])
                j += 1
				
            res += i-j+1==k and not more_than_one
        return res
------------------------------------------------------------------------------------------------------

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
		"""
        Two Pointers with HashSet
        Complexities:
            Time: O(N), N - number of chars
            Space: O(N), N - number of chars
        """
		
		# Base Case to check if string len is lower than K
		if len(S) < K:
            return 0
    
        left = ans = 0
        seen = set()
        
        for right, char in enumerate(S):
			# Start to remove from the left side of the window while we have duplicated char
            while char in seen:
                seen.remove(S[left])
                left += 1
                
            seen.add(char)
			# Only Add to Answer If we have window len of chars more or equal than K
            if right - left + 1 >= K:
                ans += 1
                
        return ans
-----------------------------------------------------------------------------------------

Time Complexity: O(n)
Space Complexity: O(1)

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count, i = 0, 0      
        while (i+k) <= len(s):
            if len(set(s[i:i+k])) == k:
                count += 1
            i += 1
        return count
      
      
-------------------------------------------------------------------------------------------------------
 from collections import defaultdict
        window_chars = defaultdict(int)
        if k > len(s):
            return 0
        for i in range(k):
            window_chars[s[i]]+=1
        def check_window(start, end):
            for i in range(start, end):
                if window_chars[s[i]] > 1:
                    return False
            return True
        
        
        ans = 0
        for i in range(k, len(s)):
            if check_window(i-k, i):
                ans+=1
            window_chars[s[i]]+=1
            window_chars[s[i-k]]-=1
        return ans + 1 if check_window(len(s) - k, len(s)) else ans 
--------------------------------------------------

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        res = 0
        count = Counter(s[:k])
        for i in range(k, len(s)):
            
            if len(count) == k:
                res += 1
            count[s[i]] += 1
            count[s[i - k]] -= 1
            if count[s[i - k]] == 0:
                del count[s[i - k]]
        if len(count) == k: res += 1
        return res
      
      
      
      
