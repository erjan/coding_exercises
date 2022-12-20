'''
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.
'''


def numWays(self, steps: int, arrLen: int) -> int:
    if steps is None or steps < 0 or not arrLen:
        return 0
    arrLen = min(arrLen, steps + 1)
    f = [[0] * arrLen for _ in range(steps + 1)]
    f[0][0] = 1
    for i in range(1, steps + 1):
        for j in range(arrLen):
            f[i][j] += f[i - 1][j]
            if j > 0:
                f[i][j] += f[i - 1][j - 1]
            if j < arrLen - 1:
                f[i][j] += f[i - 1][j + 1]
    return f[steps][0] % (10 ** 9 + 7)
  
---------------------------------------------------------------------------------------------------------
def numWays(self, steps, arrLen):
    # write your code here
    arrLen = min(arrLen, steps + 1) 
    f = [1]+[0]*(arrLen-1) # f[0] = 1
    
    for i in range(1, steps+1):
        old = 0 
        for j in range(arrLen):
            old_left = old
            old = f[j]
            if j > 0:
                f[j] += old_left      
            if j < arrLen - 1:
                f[j] += f[j+1]   
    return f[0] % (10 ** 9 + 7)
