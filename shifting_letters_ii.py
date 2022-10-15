'''
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.
'''

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = collections.Counter()
        for st, e, right in shifts:
            d[st] += 1 if right else -1         # Mark at the beginning to indicate everything after it need to be shifted
            if e+1 < n:                         # Mark (inversely) at the index after the end, to negate the unnecessary shifts
                d[e+1] += -1 if right else 1
        prefix = [0]                            # Initialize the prefix array
        ans = ''
        for i in range(n):                      # Use prefix sum style to accumulate all shifts needed, which were carried over from the previous index
            cur = prefix[-1] + d[i]
            prefix.append(cur)
            ans += string.ascii_lowercase[(ord(s[i]) - ord('a') + cur) % 26]
        return ans
      
------------------------------------------------------------------------------------------------

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            if d == 0:
                cum_shifts[st] -= 1
                cum_shifts[end+1] += 1
            else:
                cum_shifts[st] += 1
                cum_shifts[end+1] -= 1
        
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s
      
-------------------------------------------------------------------------------      
