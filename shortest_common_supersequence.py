'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n,m = len(str1),len(str2)
        dp = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        i,j = n,m
        ans = ""
        while(i>0 and j>0):
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i -= 1
                j -= 1
            else:
                if(dp[i-1][j] > dp[i][j-1]):
                    ans += str1[i-1]
                    i -= 1
                else:
                    ans += str2[j-1]
                    j -= 1
        while(i>0):
            ans += str1[i-1]
            i -= 1
        while(j>0):
            ans += str2[j-1]
            j -= 1
        return ans[::-1]
            
------------------------------------------------------------------------------

Initially DP M x N, gave memory limit exceeded, so reduced the number of rows to only 2, as we only need dp[i-1] row only to compute values in dp[i] row.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ## APPROACH : DP ##
        ## REDUCED TO 2 ROWS ##
        str1 = " "+str1
        str2 = " "+str2
        dp = [ ["" for _ in str1] for _ in range(2) ]
        
        for j in range(1,len(str1)):
            dp[0][j] = str1[1:j+1]
        
        for i in range(1,len(str2)):
            dp[1][0] = str2[1:i+1]                  # base case for leftmost column
            for j in range(1,len(str1)):
                if str2[i] == str1[j]:
                    dp[1][j] = dp[0][j-1] + str1[j]
                else:
                    dp[1][j] = min( dp[0][j] + str2[i], dp[1][j-1] + str1[j], key = len )
            dp[0] = dp[1][:]
            dp[1] = [""] * len(str1)
        return dp[0][-1]
        
        ## MEMORY LIMIT EXCEEDED, IF I STORE ALL STRINGS IN MATRIX ##
        ## EXAMPLE : S1 = "abac", S2= "cab" ##
        # [
        #     ['', 'a', 'ab', 'aba', 'abac'], 
        #     ['c', 'ac', 'abc', 'abac', 'abac'], 
        #     ['ca', 'ca', 'cab', 'abca', 'abaca'], 
        #     ['cab', 'cab', 'cab', 'caba', 'cabac']
        # ]
        
        str1 = " "+str1
        str2 = " "+str2
        dp = [ ["" for _ in str1] for _ in str2 ]
        
        dp[0][0] = ""
        
        for j in range(1,len(str1)):
            dp[0][j] = str1[1:j+1]
        
        for i in range(1,len(str2)):
            dp[i][0] = str2[1:i+1]
        
        for i in range(1,len(str2)):
            for j in range(1,len(str1)):
                if str2[i] == str1[j]:
                    dp[i][j] = dp[i-1][j-1] + str1[j]
                else:
                    dp[i][j] = min( dp[i-1][j] + str2[i], dp[i][j-1] + str1[j], key = len )
        # print(dp)     
        return dp[-1][-1]
