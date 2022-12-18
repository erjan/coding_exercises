'''
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.

Two sequences are considered different if at least one element differs from each other.
'''

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def func(idx, prevNum, prevNumFreq):
            if idx == n:
                return 1
            
            ans = 0
            for i in range(1, 7):
                if i == prevNum:
                    if prevNumFreq < rollMax[i - 1]:
                        ans += func(idx + 1, i, prevNumFreq + 1)
                        
                else:
                    ans += func(idx + 1, i, 1)
            
            return ans % MOD
        
        return func(0, 0, 0)
