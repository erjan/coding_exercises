'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''


The prerequisite for this problem is Longest Common Subsequence. Please check and solve that problem first before you solve this. Once you have mastered LCS, this problem is easy.

eg: Input strings: s1="sea", s2="eat"

LCS for above inputs is "ea"
So the number of characters that needs to be deleted from both the strings can be calculated as :

Required number of deletions = length of s1 + length of s2 - 2 * length of LCS

The LCS can be solved using DP both the methods. I have provided the solutions using two approaches:

✔️Solution I - Memoization - Top Down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        @cache
        def lcs(i, j): # find longest common subsequence
            if i==m or j==n:
                return 0            
            return 1 + lcs(i+1, j+1) if word1[i]==word2[j] else  max(lcs(i+1, j), lcs(i,j+1))                               
        # subtract the lcs length from both the strings 
        # the difference is the number of characters that has to deleted
        return m + n - 2*lcs(0,0)
Time - O(m * n) - to explore all paths
Space - O(m * n) - for cache and recursive call stack

✔️Solution I I - Tabulation - Bottom Up
class Solution:       
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)>len(word2):
            word2,word1=word1,word2        
        
        m,n=len(word1),len(word2)
        prev=[0] * (m+1)
        
        for i in range(n-1, -1, -1):
            curr=[0] * (m+1)
            for j in range(m-1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j]=1 + prev[j+1]
                else:
                    curr[j]=max(curr[j+1], prev[j])
            prev=curr
        return m + n - 2*prev[0]
      
-----------------------------------------------------------------------------------------------------------------------
first we buid a map which width: len(word1)+1 , height : len(word2)+1, where the index zero col and row means empty string

now we consider one thing: How many delete operation we neee to match the empty string to the compared string?

the answer will be the length of string!

so we fill in the value into the map in the first two forloop.
now the map look like: (take the "sea" "eat" as example)
"" "e" "a" "t"
" " [0, 1, 2, 3],
"s"[1, 0, 0, 0],
"e"[2, 0, 0, 0],
"a"[3, 0, 0, 0]

then we deal with the other value:
there are two possibility:
(1) the next char is not same::(like the map[1][1])
then how to match "s" and "e": we can do delete in "s" and do delete in "e" but we want to reduce the operation,
we already have the number of oprerations for " " to match "e" , we can just add 1 deletion to make "s" become " ".
we already have the number of oprerations for "s " to match "" , we can just add 1 deletion to make "e" become " ".
so we can generalize the formula:

DP[i][j] = min(DP[i][j-1]+1, DP[i-1][j]+1)
now map look like:
"" "e" "a" "t"
" " [0, 1, 2, 3],
"s"[1, 2, 0, 0],
"e"[2, 0, 0, 0],
"a"[3, 0, 0, 0]
(2) the next char is same:(like the table[1][2]):
we can just get the before result to fill in, since they are same so we don't need extra operation.

DP[i][j] = DP[i-1][j-1]
table look like:
"" "e" "a" "t"
" " [0, 1, 2, 3],
"s"[1, 2, 0, 0],
"e"[2, 1, 0, 0],
"a"[3, 0, 0, 0]

return the final value

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        DP = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        for i in range(1,len(word2)+1):
            DP[0][i]=i
        for j in range(1,len(word1)+1):
            DP[j][0]= j
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]== word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i][j-1]+1, DP[i-1][j]+1)
        # print(DP)
        return DP[i][j]
