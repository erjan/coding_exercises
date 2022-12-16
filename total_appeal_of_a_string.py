'''
The appeal of a string is the number of distinct characters found in the string.

For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
Given a string s, return the total appeal of all of its substrings.

A substring is a contiguous sequence of characters within a string.
'''

--------------------------------------------------------------------------------------------------------------------------------------------------
Intuition
The given constraint has 1 <= s.length <= 10^5, indicating O(N^2) solutions would get TLE. A natural idea is to use 1-D DP.

Explanation
We use an array dp of length N, where dp[i] represents the total appeal of all of substrings ending at index i of the original string s. We also use a hashmap to record the most recent index with the current letter. Now, two conditions needs to be considered:
(1) If the current letter does not exist in the hashmap, meaning that it is a new appearance. Hence, the current letter can contribute to the appeals of all substrings ending at it, which implies dp[i] = dp[i - 1] + (i + 1);
(2) If the current letter does exist in the hashmap, meaning that it is not a new appearance. Hence, the current letter can contribute to the appeals of all substrings starting after the previous appearance and ending at it, which implies dp[i] = dp[i - 1] + (i - hashmap[s[i]]).
The final answer is sum(dp).

Complexity
Time: O(N), where N = s.length since we perform a linear scan
Space O(N), for the use of dp array (and the hashmap)

Below is my in-contest solution. Please upvote if you find this solution helpful. Thanks!

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        hashmap = {s[0]: 0}
        for i in range(1, n):
            if s[i] not in hashmap:
                dp[i] = dp[i - 1] + (i + 1)
                hashmap[s[i]] = i
            else:
                dp[i] = dp[i - 1] + (i - hashmap[s[i]])
                hashmap[s[i]] = i
        return sum(dp)
Follow up: The above solution can be further optimized to save the use of dp array given as follows, which makes the code even more clean and concise.

Complexity
Time: O(N), where N = s.length since we perform a linear scan
Space O(26) = O(1), for the use of hashmap only

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        curSum, cumSum = 1, 1
        hashmap = {s[0]: 0}
        for i in range(1, n):
            if s[i] not in hashmap:
                curSum += i + 1
            else:
                curSum += i - hashmap[s[i]]
            cumSum += curSum
            hashmap[s[i]] = i
        return cumSum
      
----------------------------------------------------------------------------------
class Solution:
    def appealSum(self, s: str) -> int:
        res, cur, prev = 0, 0, defaultdict(lambda: -1)
        for i, ch in enumerate(s):
            cur += i - prev[ch]
            prev[ch] = i
            res += cur
        return res  
