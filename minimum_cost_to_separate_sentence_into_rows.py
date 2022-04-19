'''
You are given a string sentence containing words separated by spaces, and an integer k. Your task is to separate sentence into rows where the number of characters in each row is at most k. You may assume that sentence does not begin or end with a space, and the words in sentence are separated by a single space.

You can split sentence into rows by inserting line breaks between words in sentence. A word cannot be split between two rows. Each word must be used exactly once, and the word order cannot be rearranged. Adjacent words in a row should be separated by a single space, and rows should not begin or end with spaces.

The cost of a row with length n is (k - n)2, and the total cost is the sum of the costs for all rows except the last one.

For example if sentence = "i love leetcode" and k = 12:
Separating sentence into "i", "love", and "leetcode" has a cost of (12 - 1)2 + (12 - 4)2 = 185.
Separating sentence into "i love", and "leetcode" has a cost of (12 - 6)2 = 36.
Separating sentence into "i", and "love leetcode" is not possible because the length of "love leetcode" is greater than k.
Return the minimum possible total cost of separating sentence into rows.
'''


Explanation
dp[i+1]: Minimum cost to separate up to the ith word
dp[i+1] = min(dp[i+1], dp[j] + (k - cur) ** 2) for j in range(i-1, -1, -1)
cur: length of current row to including the ith word
Make sure cur <= k, otherwise, break the loop
Note that we do NOT want to count the cost of last row
We will use a dp_row to record the number of row needed to cover ith word with cost is minimized
See more explanation below
Implementation
class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        if len(sentence) <= k: return 0                   # optimization
        words = sentence.split(' ')                       # split sentence to words
        words_len = [len(word) for word in words]         # get length for each word, will be used later
        cur, n = 0, len(words)
        dp = [0] * (n+1)                                  # dp[i+1]: minimum cost to include word[i], dp[0] works as a padding to handle edge cases
        dp_row = [0] * (n+1)                              # dp_row[i+1]: number of row needed to include word[i] when cost is minimized
        for i in range(n):
            cur = words_len[i]                            # length of current row
            dp[i+1] = dp[i] + (k - cur) ** 2              # initialize cost
            dp_row[i+1] = dp_row[i] + 1                   # initialize number of row needed
            for j in range(i-1, -1, -1):                  # use each previous row to find out the minimum cost
                cur += words_len[j] + 1                   # increment length of current row (word length + space (1))
                if cur > k: break                         # break when length is over `k`
                if dp[j] + (k - cur) ** 2 < dp[i+1]:      # if a smaller cost is found
                    dp[i+1] = min(dp[i+1],                #     update cost
                                  dp[j] + (k - cur) ** 2)
                    dp_row[i+1] = dp_row[j] + 1           #     update number of rows needed
        for i in range(n-1, -1, -1):                      # return cost of including last word in the second last row (last row doesn't count)
            if dp_row[i] != dp_row[i+1]:                  # By description: "total cost is the sum of the costs for all rows except the last one."
                return dp[i]
        return 0
Thanks to @WayWardCC , I realized that my solution can be clearer without using dp_row.
This is because, cost only increase when a new row is started, and decrese if it's in the same row.

class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        if len(sentence) <= k: return 0                   
        words = sentence.split(' ')                       
        words_len = [len(word) for word in words]         
        cur, n = 0, len(words)
        dp = [0] * (n+1)                                  
        for i in range(n):
            cur = words_len[i]                            
            dp[i+1] = dp[i] + (k - cur) ** 2              
            for j in range(i-1, -1, -1):                  
                cur += words_len[j] + 1                   
                if cur > k: break                         
                if dp[j] + (k - cur) ** 2 < dp[i+1]:      
                    dp[i+1] = min(dp[i+1],                
                                  dp[j] + (k - cur) ** 2)
        for i in range(n-1, -1, -1):                      
            if dp[i+1] >= dp[i]:
                return dp[i]
        return 0
        
--------------------------------------------------------------
Python 3

class Solution:
    def minimumCost(self, s: str, k: int) -> int:
        @cache
        def dfs(i: int) -> int:
            return 0 if i + k >= len(s) else (
                min([(k + i - j) * (k + i - j) + dfs(j + 1) for j in range(i, i + k + 1) if s[j] == ' '])
            )
        return dfs(0)
        
