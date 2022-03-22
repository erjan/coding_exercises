'''
You have n coins and you want to build a staircase with these coins. The staircase 
consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
            total = 0
            row = 0
            for i in range(1, n+1):
                total += i
                if total >= n:
                    row = i
                    break
            print(total)
            if total != n:
                row = row-1
            print(row)
            return row

          
#another solution          
def arrangeCoins(self, n: int) -> int:
    return int((-1 + (1 + 8*n) ** 0.5) // 2)          
