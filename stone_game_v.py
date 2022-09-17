'''
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.
'''

from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0]
        for i in range(len(stoneValue)):
            prefix += [prefix[-1] + stoneValue[i]]
        print(prefix)
        
        @lru_cache(None)
        def dfs(left=0, right=len(prefix)-1):
            if right - left == 1: return 0
            
            maxval = -1
            for i in range(left+1, right):
                leftsum = prefix[i] - prefix[left]
                rightsum = prefix[right] - prefix[i]
                
                if leftsum > rightsum:
                    maxval = max(maxval, rightsum + dfs(i, right))
                elif rightsum > leftsum:
                    maxval = max(maxval, leftsum + dfs(left, i))
                else:
                    maxval = leftsum + max(dfs(left, i), dfs(i, right))
            
            return maxval
           
        return dfs()
