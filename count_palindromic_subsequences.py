'''
Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.

Note:

A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 
 '''

----------------------------------------------------------------------------------------------------
Intuition

Since 5 is an odd length each palindromic subsequences must have a single middle element ('3' in the case of "10301"). Each palindromic subsequences must also have an ordered pair prior to a middle element with a mirrored ordered pair after ("10", "01" in the case of "10301"). The idea of this solution is to count the number of ordered pairs that mirror before and after each middle index (index ∈ [2, len(S) - 2)).

Algorithm

If the length of the input string S is less than 5 no strings can be built of length 5 (return 0).
Get the number of ordered pairs before and after each index.
Count the number of matching pairs before and after each index. There are only 10 possible digits to loop through for each pair addition resulting in a global linear runtime.
Return the value calculated modulo 10^9 + 7.
Code

class Solution:
    def countPalindromes(self, S: str) -> int:
        #Ignore string less than 5 characters (cannot have a 5 length substring)
        if len(S) < 5:
            return 0
        
        #Returns the running pair counts for each index
        def get_pairs(s):
            seen_cnt = {str(num):0 for num in range(10)}
            seen_cnt[s[0]] = 1 #We have seen the first character since we start the loop at 1
            pair_cnts = defaultdict(int)
            res = [None] #Filler empty dict (index = 0 / end index)
            
            #Getting running pairs
            for idx in range(1, len(s) - 1):
                res.append(pair_cnts.copy()) #Append running pair counts
                for num in seen_cnt.keys():
                    pair_cnts[(num, s[idx])] += seen_cnt[num]
                seen_cnt[s[idx]] += 1
                
            #Filler empty dict (index = 0 / end index)
            res.append(None)
            
            return res
        
        res = 0
        #Getting post and pre pair counts
        pre, post = get_pairs(S), get_pairs(S[::-1])[::-1]
        
        #Check all possible middle characters -> S[2, len(S) - 2)
        for idx in range(2, len(S) - 2):
            for key, val in pre[idx].items():
                if key in post[idx]:
                    res += post[idx][key] * val #Total pairs per key
                    res %= 1000000007
                    
        return res        
        
-------------------------------------------------------------------------------------------------------------------------

Intuition
If a size 5 palindromic subsequence is given, we can check how many of it appears in s in O(N) via DP. In total, there are 100 (not 1000) relevant subsequences to check.



class Solution:
    def countPalindromes(self, s: str) -> int:
        ans = 0 
        for x in range(10): 
            for y in range(10): 
                pattern = f"{x}{y}|{y}{x}" 
                dp = [0]*6
                dp[-1] = 1 
                for i in range(len(s)): 
                    for j in range(5): 
                        if s[i] == pattern[j] or j == 2: dp[j] += dp[j+1]
                ans = (ans + dp[0]) % 1_000_000_007
        return ans 
