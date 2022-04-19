'''
Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ## RC ##
        ## APPROACH : SLIDING WINDOW ##
        ## Similar to Leetcode : 424. Longest Repeating Character Replacement ##
        ## Similar to Leetcode : 904. Fruit Into Basket ##
        ## SAME CODE : 340. Longest Substring with At Most K Distinct Characters ##
		
        ## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(N) ##
        
        lookup = collections.defaultdict(int)
        n, k = len(s), 2
        start = end = max_len = 0 
        while(end < n ):
            lookup[ s[end] ] += 1
            end += 1
            while( len(lookup) > k ):
                lookup[ s[start] ] -= 1
                if( lookup[ s[start] ] == 0 ):
                    del lookup[ s[start] ]
                start += 1
            max_len = max( max_len, end - start )        
        return max_len
      
------------------------------------------------------

Time: O(N)
Space: O(1) - at most the hash will hold 3 elements.
Algorithm: Maintain a sliding window which will increase until a third distinct character is detected. At this point decrement the counter for the left end and delete it from the hash if it is empty. Left will keep moving up as long as the hash holds 3 distinct characters. At the end of the loop the window will have its max seen value.

def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        counter = collections.defaultdict(int)
        left, res = 0, 0
        for right in range(len(s)):
            counter[s[right]] += 1
            if len(counter) > 2:
                counter[s[left]] -= 1
                if not counter[s[left]]:
                    counter.pop(s[left])
                left += 1
        return right - left + 1
Other solution which may be easier to understand as left is brought in keeping the size of the hash always at 2, but this is not necessary as shown above.

def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        counter = collections.defaultdict(int)
        left = 0
        res = 0
        counter[s[left]] = 1
        for right in range(1, len(s)):
            if s[right] in counter or len(counter) < 2:
                counter[s[right]] += 1
            else:
                while len(counter) == 2:
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        counter.pop(s[left])
                    left += 1
                counter[s[right]] += 1
            res = max(res, right - left + 1)
            
        return res
-------------------------------------------------------------------

# approach:
# keep a map/dictionary to keep count of different type of characters
# if I add a character and it's count is 1 that means I have added a new char right?
# so I increase the count by 1
# now, I have a limit on count(distinct chars) as k or 2 in this example
# so I will see if my window has count less than or equal to the 2, if yes, then I will
# find the size of that window.
# otherwise, I will shrink my window
# If I remove a char and if its count becomes 0 that means, I have removed a distinct char right?
# so I will decrease my count by 1

def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    ln = len(s)
    if ln == 0:
        return 0
    
    # to hold chars from the s so that I know that I have only two distinct characters
    dct = {}
    j = 0
    maxWindow = 0
    count = 0
    for i in range(ln):
        dct[s[i]] = dct.get(s[i], 0) + 1
        
        if dct[s[i]] == 1:
            count += 1
        
        while count > 2:
            dct[s[j]] -= 1
            if dct[s[j]] == 0:
                count -= 1
            j += 1
        
        maxWindow = max(maxWindow, i - j + 1)

    return maxWindow
	
	
	similar question, when K is a param, exact ditto code, just use K instead of 2
	https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/discuss/389922/easy-peasy-pythoncomments-approach-sliding-window-two-pointers-solution
    
    --------------------------------------------------------
    
    class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        left, right = 0, 0
        N, memo = len(s), {}
        maxLen = 0
        
        if N < 3: return N
        
        while(right < N):
            
            memo[s[right]] = right
            right += 1
            
            if len(memo) == 3:
                delIndex = min(memo.values())
                left = delIndex + 1
                del memo[s[delIndex]]
            
            maxLen = max(maxLen, right-left)
            
        return maxLen
------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {} # key: character, value: index
        left = 0
        res = 0
        for right,c in enumerate(s):
            if c not in d:
                d[c] = 1
            else: 
                d[c] = d[c] + 1

            if len(d) <= 2:
                res = max(res, right - left + 1)
            else:
                d[s[left]] = d[s[left]] - 1
                if (d[s[left]] == 0):
                    del d[s[left]]
                left += 1
        return res
      
      
