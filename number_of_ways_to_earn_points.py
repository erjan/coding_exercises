'''
There is a test that has n types of questions. You are given an integer target and a 0-indexed 2D integer array
types where types[i] = [counti, marksi] indicates that there are counti questions of the ith type, and 
each one of them is worth marksi points.

Return the number of ways you can earn exactly target points in the exam. Since the answer may be too large, return it modulo 109 + 7.

Note that questions of the same type are indistinguishable.

For example, if there are 3 questions of the same type, then solving the 1st and 2nd questions is the
same as solving the 1st and 3rd questions, or the 2nd and 3rd questions.
'''



class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = 10**9 + 7
        dp = [0]*(target + 1)
        dp[0] = 1

        for count, mark in types:
            # Repeat in reverse order to avoid duplication 
            for i in range(target, -1, -1):
                for j in range(1, count + 1):
                    if i - mark*j >= 0:
                        dp[i] += dp[i - mark*j]
                        dp[i] %= mod
        
        return dp[target]
      
--------------------------------------------------------------------------------------------
Basic DP problem, it's easier than 3rd problem...

we can define dp as:
dp[i][j]: the number of ways you can earn exactly j points in the exam considering types[:i]

and the state transfer fn is straightforward.

since we choose types[i] based on previous choice only, it means each state only depends on previous state. dp[i] only depends on dp[i-1]
if current points is j, then previous points should be j-cnt*mark
[count, mark] = types[i]
dp[i][j] += dp[i-1][j-cnt*mark] where cnt from 0 to count
Base Case

choose nothing to make 0 points is also ONE valid way
dp[0][0] = 1

Complexity
Time complexity:
O(n∗target∗count)O(n*target*count)O(n∗target∗count)

Space complexity:
O(n∗target)O(n*target)O(n∗target)

Code
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = int(1e9+7)

        n = len(types)

        # dp[i][j]: the number of ways you can earn exactly j points in the exam considering types[:i]
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        types = [[-1, -1]] + types
        for i in range(1, n+1):
            count, mark = types[i][0], types[i][1]
            for j in range(target+1):
                for cnt in range(count+1):
                    dp[i][j] += dp[i-1][j-cnt*mark] if j-cnt*mark>=0 else 0
                    dp[i][j] %= MOD

        return dp[n][target] % MOD
