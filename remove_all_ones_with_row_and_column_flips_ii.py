'''
You are given a 0-indexed m x n binary matrix grid.

In one operation, you can choose any i and j that meet the following conditions:

0 <= i < m
0 <= j < n
grid[i][j] == 1
and change the values of all cells in row i and column j to zero.

Return the minimum number of operations needed to remove all 1's from grid.
'''


A lot of global variables which may be a bit improper, but this should help anyone confused get the gist on how to solve it ...

class Solution(object):
    def removeOnes(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.ans = float('inf')
        self.flips = 0
        seen = set()
        def helper():
            flag = False
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 1 and ('r', x) not in seen and ('c', y) not in seen :
                        flag = True
                        seen.add(('r', x))
                        seen.add(('c', y))
                        self.flips+=1
                        helper()
                        self.flips-=1
                        seen.remove(('r', x))
                        seen.remove(('c', y))
                        
            if not flag:
                self.ans=min(self.ans, self.flips)
        
        helper()
        return self.ans
      
----------------------------------------------------------------------------------------------------------
How should we bitmask a Matrix?
mapping each i, j position to 1-D array. The following picture shows the 1-D index of each 2-D position.
image

bitmasking the Matirx by the 1-D array index
image

indexes = [0, 2, 5, 6]
bitmask = (1<<0) + (1<<2) + (1<<5) + (1<<6) = 101

Operaion as bitmask
Each operation is like doing an AND operation of a covering matrix to the original one

image

We can gerenate the bitmask of all the covering matrices (operations) on each positions beforehand, it takes only O(N * M * max(N,M)). We just start with the bitmask of a full matrix with all 1 and then substract the bit number of each position with same row or column. Note that we need to add the bit of initial position back since we substract it twice.

        covers = [[0 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                n = mask - 1
                for ii in range(N):
                    n -= (1 << (ii*M + j))
                for jj in range(M):
                    n -= (1 << (i*M + jj))
                n += (1 << (i*M + j))
                covers[i][j] = n
DP Solution
k = bitmask of some state
State Definition: DP[k] means the minimum operations we need to take to transform it into DP[0]
Transition of State: DP[k] = min(DP[k & covers[i][j]] + 1 for all i, j with grid[i][j] == 1)
Initial State: DP[0] = 0
So the answer will be DP[bitmask of initial state]

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        mask = 1<<(N*M)
        
        covers = [[0 for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                n = mask - 1
                for ii in range(N):
                    n -= (1 << (ii*M + j))
                for jj in range(M):
                    n -= (1 << (i*M + jj))
                n += (1 << (i*M + j))
                covers[i][j] = n

        target = sum([(1 << (i*M+j)) * grid[i][j] for i in range(N) for j in range(M)])
        if target == 0:
            return 0
                
        DP = [inf for _ in range(mask)]
        DP[0] = 0
        for k in range(1, mask):
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == 1:
                        DP[k] = min(DP[k], DP[k & covers[i][j]] + 1)
            if k == target:
                return DP[k]
Time Complexity
O(NM*2^(NM))

------------------------------------------------------------------------------------------------
Explanation
Try all possible permutations of ones, where ones is a list of (i, j) when grid[i][j] == 1
It's just a question about implementation, since brute force will make it work. I guess the blocker is:
Finding a way to generate permutation of ones
If you don't know itertools.permutations, you can also use backtracking to write one simulate the same process
Figuring out the upper bound of the length of each permutation (a little bit Math)
If there is a 3*5 matrix with 1 at each cell, then the minimum operation is 3. (i.e. You can walk over each row to remove 1s)
If there is a 3*5 matrix with only 1 at (0, 0), then the minimum is obvious 1, which is the total count number of 1s
thus, we are getting ans = min(m, n, one_cnt). See below code.
Time: O(10^5) ~= O(122850) = O(2730 * 3 * 15)
Space: O(1), since max number of elements is 15.
Implementation
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = [(i, j) for i in range(m) for j in range(n) if grid[i][j]] # get indices for all ones, time: O(15)
        one_cnt = len(ones)                    
        ans = min(m, n, one_cnt)                                          # the answer will be bounded by the minimum between these 3
        for indices in itertools.permutations(ones, r=ans):               # Permutation: Pick 3 out of 15, time: O(2730) for 3*5 matrix
            cur, tmp = 0, set()
            for x, y in indices:                                          # Brute force, iterate permuted indices, time: O(3)
                for i, j in ones:                                         # iterate over `ones`: O(15)
                    if i == x or j == y:
                        tmp.add((i, j))
                cur += 1                                                  # count current step
                if len(tmp) == one_cnt: break
            ans = min(ans, cur)                                           # update minimum step
            if ans == 1: return 1                                         # optimization, the best solution for non-all-zero matrix 
        return ans

      
