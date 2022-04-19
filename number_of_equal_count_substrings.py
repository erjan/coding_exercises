'''
You are given a 0-indexed string s consisting of only lowercase English letters, and an integer count. A substring of s is said to be an equal count substring if, for each unique letter in the substring, it appears exactly count times in the substring.

Return the number of equal count substrings in s.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "aaabcbbcc", count = 3
Output: 3
Explanation:
The substring that starts at index 0 and ends at index 2 is "aaa".
The letter 'a' in the substring appears exactly 3 times.
The substring that starts at index 3 and ends at index 8 is "bcbbcc".
The letters 'b' and 'c' in the substring appear exactly 3 times.
The substring that starts at index 0 and ends at index 8 is "aaabcbbcc".
The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
Example 2:

Input: s = "abcd", count = 2
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0.
Example 3:

Input: s = "a", count = 5
Output: 0
Explanation:
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0
'''


class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        
        # aaabbcccb
        ans=0
		# The sizes of the substring windows are limited, namely, 1*count, 2*count ..... 26*count
		# window can have 1 unique_char, 2 unique_chars...... 26 unique_chars respectively.
        for al in range(1,27):
            ans+=self.count_fix_s(s,al*count,count)
        
        return ans
            
        
    def count_fix_s(self,s,w,count):
        # standard sliding window logic with fixed window size w with left and right being left index and right index respectively..
        left=0
        d={}
        ans=0
        for right in range(len(s)):
            
            d[s[right]]=d.get(s[right],0)+1
            
            if right-left+1>w:
                d[s[left]]-=1
                if d[s[left]]==0: del d[s[left]]
                left+=1
            
            if right-left+1 == w and set(d.values())==set([count]):
                ans+=1
        return ans
      
      -------------------------------------------------------
Let the ejection condition of the sliding window be if it exceeds some number of unique characters or if the count of a character is too high.

Let uniqueChars be the number of unique characters in s, attempt this sliding window approach for all numbers 1 through uniqueChars.

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        if count > len(s):
            return 0
        
        ans = 0
        
        n = len(s)
        uniqueChars = len(set(s))
        
        for uniqueLimit in range(1,uniqueChars+1):
            slidingWindow = defaultdict(int)
            
            left = 0
            for right in range(n):
                slidingWindow[s[right]] += 1
                
                while len(slidingWindow) > uniqueLimit or slidingWindow[s[right]] > count:
                    slidingWindow[s[left]] -= 1
                    if slidingWindow[s[left]] == 0:
                        del slidingWindow[s[left]]
                    left += 1
                        
                if len(slidingWindow) == uniqueLimit and \
                    all(value == count for value in slidingWindow.values()):
                    ans +=1
                    
        return ans
      
-----------------------------------------------------------------

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:  
        def is_valid(counts, count):
            for k, v in counts.items():
                if v > 0 and v != count: return False            
            return True
        
        def window_size(right, left):
            return right - left + 1

        def counts_for_window_size(s, curr_window_size, count):
            left = 0
            counts = defaultdict(int)
            result = 0

            for right in range(len(s)):            
                counts[s[right]] += 1

                if window_size(right, left) > curr_window_size:
                    counts[s[left]] -= 1                    
                    left += 1

                if window_size(right, left) == curr_window_size:
                    if is_valid(counts, count): result += 1

            return result
        
        return sum([counts_for_window_size(s, i * count, count) for i in range(1, 27)])
      
-----------------------------------------------------------------
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        size = count
        lower = total = 0
        upper = min(26 * count, len(s))
        p = [Counter()]
        for c in s:
            p.append(p[-1] + Counter(c))
        while size <= upper:
            for i in range(lower, len(s) - size + 1):
                for k, v in p[i+size].items():
                    v -= p[i][k]
                    if v == 0:
                        continue
                    if v > count and i == lower:
                        lower += 1
                    if v != count:
                        break
                else:
                    total += 1
            size += count
        return total
I realize there's a lot going on in the above. It's a combination of a few optimization techniques I applied which eventually allowed it to pass in just under the time limit.

Development process
My solution began as a simple brute force approach where I checked every starting position and every size which was a multiple of count. This was too slow, passing only 113/124 cases:

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        size = count
        total = 0
        while size <= len(s):
            for i in range(len(s) - size + 1):
                sub = s[i:i+size]
                for v in Counter(sub).values():
                    if v != count:
                        break
                else:
                    total += 1
            size += count
        return total
I made an optimization by limiting the upper bound of size. Of course, there are only 26 characters, so the largest window can only be 26 * count. This passes 122/124 cases but then times out on the second to last:

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        size = count
        total = 0
        upper = min(26 * count, len(s))
        while size <= upper:
            for i in range(len(s) - size + 1):
                sub = s[i:i+size]
                for v in Counter(sub).values():
                    if v != count:
                        break
                else:
                    total += 1
            size += count
        return total
In desperation, I added another pathetic optimization to slightly raise the upper bound of the i variable (via "lower") whenever there were too many instances of a character, as the window size always increased so it would never have less than count of that character if it's included. This did not pass more test cases:

class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        size = count
        total = 0
        upper = min(26 * count, len(s))
        lower = 0
        while size <= upper:
            for i in range(lower, len(s) - size + 1):
                for v in Counter(s[i:i+size]).values():
                    if v > count and i == lower:
                        lower += 1
                    if v != count:
                        break
                else:
                    total += 1
            size += count
        return total
Finally, I thought "okay, so the weakest point is obviously recomputing the counter each time. What can I do to fix that?" then I thought "prefix sum!" so I wrote the script you see at the top. There was an intermediate version that subtracted the counters before the final nested loop, but this was an unnecessary 26 operations occuring before every index check and had to be eliminated before it finally passed.
      

      
      
