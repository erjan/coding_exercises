'''
Given a digit string s, return the number of unique substrings of s where every digit appears the same number of times.
 

Example 1:

Input: s = "1212"
Output: 5
Explanation: The substrings that meet the requirements are "1", "2", "12", "21", "1212".
Note that although the substring "12" appears twice, it is only counted once.
Example 2:

Input: s = "12321"
Output: 9
Explanation: The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".
'''


Approach #1. Brute force using Python Set
This method might TLE if more cases are added
Time: O(n**2 * m). As hint 4 says, hash cur may take O(m), if m is large this will time out.
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n, s_set = len(s), set()
        for i in range(n):
            cur, cnt = '', [0] * 10
            for j in range(i, n):
                cnt[ord(s[j]) - ord('0')] += 1
                cur += s[j]
                if len(set(cnt) - {0}) == 1:
                    s_set.add(cur)
        return len(s_set)
Approach #2. Rolling hash, Math
if max_cnt * unique == j - i + 1 is the Math trick to speed the whole thing up.
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n, s_set = len(s), set()
        PRIME, MOD = 11, int(1e9+7)                         # find a prime for hash algorithm (any prime greater than 10 for this problem)
        for i in range(n):
            cnt = [0] * 10                                  # count frequency of digit
            unique = max_cnt = s_hash = 0                   # unique: unique digit in substring, max_cnt: max frequency of digit in current substring; s_hash: string hash
            for j in range(i, n):
                digit = ord(s[j]) - ord('0')
                unique += 1 if cnt[digit] == 0 else 0       # count unique digits
                cnt[digit] += 1
                max_cnt = max(max_cnt, cnt[digit])          # update max frequency
                s_hash = (s_hash * PRIME + digit + 1) % MOD # update hash in O(1)
                if max_cnt * unique == j - i + 1:           # if max frequency * unique digits == the substring length, meaning each digits have the same frequency
                    s_set.add(s_hash)
        return len(s_set)                                   # return number of "Unique Substrings With Equal Digit Frequency"
      
      
-------------------------------------------------------------------------
Disclaimer: I didn't think of this myself, I came across this after submitting my own code. I thought it was a brilliant approach, so I decided to study it.

Runtime: 1295 ms
Memory: 14.8 MB

Original Code

class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res, uni, found, count = set(), len(set(s)), True, 1
        while count <= len(s) and found:
            found = self.equalCountSubstrings(s, count, uni, res)
            count += 1
        
        return len(res)
    
    def equalCountSubstrings(self, s: str, count: int, uni, res) -> int:
        found = False
        for i in range(1, uni + 1):
            window, dic, occ = (i) * count, {}, 0
            for j in range(len(s)):
                dic[s[j]] = dic.get(s[j], 0) + 1
                if dic[s[j]] == count:
                    occ += 1
                
                if j >= window:
                    dic[s[j-window]] = dic[s[j-window]] - 1
                    if dic[s[j-window]] == count - 1:
                        occ -= 1

                if occ == i:
                    res.add(s[j-window+1:j+1])
                    found = True
        return found
Logic:
The equalDigitFrequency() can be thought of searching for substrings where each character appears for 1 time, 2 times, 3 times, up to len(s) times.

One interesting observation is that if you cannot find a single substring where each character appears for x times, you can stop right there, since there is no way you can find any substring where each character appears for ≥(x+1) times. This control logic is implemented using the found Boolean variable.

The more interesting portion of the code is defintely equalCountSubstrings(). For the input arguments:

Variable s is the orginal string
Variable count is the number of times you want each character to appear in the substring
Variable uni stands for number of unique characters
Variable res is essentially the res collector
We can iterate through from 1 to uni (inclusive) times, where we want to find substring with 1 unique char each appearing for count times, substring with 2 unique chars each appearing for count times and so on.
Let's say we want to find substring with 2 unique chars each appearing for 3 times, so that means we are looking at a sliding window of 6. We use dic to keep track the number of times each unique char appears in this sliding window. occ represents the number of characters that appear for count (3 in this case) times in the substring. If occ == 2, means there are indeed 2 chars that appear for 3 times each in a sliding window of 6, we can therefore add the current sliding window into the res.

Finally, going back to equalDigitFrequency(), we simply return len(res).

---------------------------------------------------------------------------------------------------------------
The idea is to use a Counter() to count frequencies and another Counter() to count the frequencies of each frequency.
When there's only one different frequency, add to the set
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res=set()
        for i in range(len(s)):
            res.add(s[i])
            cur=[s[i]]
            dct=collections.Counter(s[i])
            freq=collections.Counter(dct.values())
            for j in range(i+1,len(s)):
                char=s[j]
                cur_freq=dct[char]
                cur.append(char)
                if cur_freq>0:
                    freq[cur_freq]-=1
                    if freq[cur_freq]==0: del freq[cur_freq]
                dct[char]+=1
                freq[cur_freq+1]+=1
                if len(freq)==1: res.add(''.join(cur))
        return len(res)
------------------------------------------------------------------
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        
        
        res = set()
        '''
        "1212334"
        "1101010"
        " 110000"
        "  11100"
        "   1100"
        "    110"
        "     11"
        "      1"
        '''
        
        
        def expand_from(i):
            cs = defaultdict(int)
            j = i + 1
            for c in s[i:]:
                cs[c] += 1
                if s[i:j] not in res and len(set(cs.values())) == 1:
                    res.add(s[i:j])
                j += 1
        for i in range(len(s)):
            expand_from(i)
        
        return len(res)
      
