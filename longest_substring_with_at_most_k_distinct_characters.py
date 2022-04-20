'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
'''

class Solution(object):
    
    """
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
-----------------------------------------------------------------------------------
class Solution:
    
    def lengthOfLongestSubstringKDistinct(self, string: str, numDistinctCharacters: int) -> int:
        
        # create a counter that will store the frequency of characters
        freq = Counter()
        
        # create a variable to store the index of the left side of the window
        window_start = 0
        
        # create a variable to return that will hold the length of the longest valid substring seen
        longest_valid_substring_seen = 0
        
        # iterate through the entire string, "window_end" represents the "right side" of the window
        for window_end, char in enumerate(string):
            
            # load up the frequency counter until constraint violation
            freq[char] += 1
            
            # shrink the window if violates the constraint of more than the number of distinct characters
            # the length of the freq counter represents the number of distinct characters
            while len(freq) > numDistinctCharacters:
                
                # get the left char of the window (the char that window_start points to)
                left_char = string[window_start]
                
                # and decrement it in the counter
                freq[left_char] -= 1
                
                # IMPORTANT: we check the length of the frequency counter (which is equivalent to number of distinct chars)
                # we must delete chars that have a zero count, because we no longer have a distinct char in window
                if freq[left_char] == 0:
                    del freq[left_char]
                
                # shrink window here
                window_start += 1
            
            # valid window at this point, get the size of the window
            # and compare it to the longest valid substring seen so far
            # update longest_valid_substring_seen if we found a new longest valid substring
            window_size = window_end - window_start+1
            longest_valid_substring_seen = max(longest_valid_substring_seen, window_size)
        
        return longest_valid_substring_seen
----------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0:
            return 0
        
        max_len = 0
        l = 0
        count = defaultdict(int)
        
        for r in range(len(s)):
            count[s[r]] += 1 
            while l < r and len(count) > k:
                if count[s[l]] == 1:
                    del count[s[l]]
                else:
                    count[s[l]] -= 1
                l += 1       
            max_len = max(max_len,r - l + 1)
                     
        return max_len
The idea for this solution is that instead of keeping track of the location of the last appearance of a character in the window, we instead just count occuraces of characters in the window.

When we have more than k characters in the window, we move left, decrease the character count, and drop values from the dictionary when their count is zero, i.e. when the character is no longer in the window.

The time complexity then becomes O(n) since we do not need to find the minimum element in the dictionary.

Thank you for reading my first LeetCode post!
---------------------------------------------------------------------------------

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        longest =0
        currentDict = {}
        if k ==0:
            return 0
        
        for right, rightval in enumerate(s):
            leftval= s[left]
            
            if rightval not in currentDict:
                currentDict[rightval] = 1
            else:
                currentDict[rightval] += 1
            
            currentlength = right-left +1
            if len(currentDict) <=k:
                longest = max(longest,currentlength)
            else:
                currentDict[leftval] -=1
                if currentDict[leftval] ==0 :
                    del currentDict[leftval]
                left +=1
        return longest
-----------------------------------------------------------------

You can use Python3's OrderedDict class from collections to act as a lru_cache.
The idea here is that when you encounter a letter that is not in the cache, and over the threshold, you simply evict the least-recently used item. Using the last index that item was seen, just update where you want your "window" to start and calculated the longest substring again.

import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """ Sliding window with a orderedDict acting as lru_cache """
        # Catch edge case
        if k == 0:
            return 0
        # use ordered dict here to act as cache
        unique_chars = collections.OrderedDict()
        # keep track of the longest_length we found
        longest_length = 0
        # once we evict a letter, we update the start index of the next letter
        start_index = 0
        for index, c in enumerate(s):
            # we want to know when to evict, this is when we are at capacity k
            # AND the current letter is not already in our cache
            if len(unique_chars) >= k and c not in unique_chars:
                # at capacity, have to evict
                last_item = unique_chars.popitem(last=False) # pop the least recently used item
                last_index = last_item[1] # get that item's index
                start_index = last_index+1 # set the start_index as the next letter to the right
            unique_chars[c] = index # update our cache with the last index we saw this letter at
            unique_chars.move_to_end(c, last=True) # Move it to the end of the list so it's most recent
            longest_length = max(longest_length, index-start_index+1) # calculate longest again
        return longest_length
------------------------------------------------------------------------------------

def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
        if k >= len(s):
            return len(s)
        if k == 0:
            return 0
        
        dic = {}
        
        count = 0
        l = 0
        r = 0
        s = list(s)
        maxCount = 0
        
        # O(n) time
        while r < len(s):
            # If character not in dic then we add it and increment a count
            if s[r] not in dic:
                dic[s[r]] = 1
                count += 1
            else:
                dic[s[r]] += 1
                
            # We reached the max distinct characters, update maxCount
            if count <= k:
                maxCount = max(maxCount, r-l+1)

            # If count is greater than k then we have to shrink the window
            else:
				# check if l is in the dic, if so we have to decrement it
				# and if it is now decremented to 0, we remove that from the dic
				# and reduce count by 1
                if s[l] in dic:
                    dic[s[l]] -= 1
                    if dic[s[l]] == 0:
                        del dic[s[l]]
                        count -= 1
                l += 1
            r += 1

        return maxCount
      
      
      
      

      
      
