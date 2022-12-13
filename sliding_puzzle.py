'''
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
'''

from copy import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def getS(arr):
            s = ""
            for i in arr:
                for j in i:
                    s+=str(j)
            return s
        dir = [[-1,0],[0,1],[1,0],[0,-1]]
        ans = [[1,2,3],[4,5,0]]
        q = deque()
        q.append([board,0])
        used = set()
        used.add(getS(board))
        n = len(board)
        m = len(board[0])
        while q:
            tmp,cnt = q.popleft()
            if tmp==ans:
                return cnt
            for i in range(n):
                for j in range(m):
                    if tmp[i][j]==0:
                        for r,c in dir:
                            nr,nc = i+r,j+c
                            if n>nr>=0 and m>nc>=0:
                                tmp[nr][nc],tmp[i][j] = tmp[i][j],tmp[nr][nc]
                                if getS(tmp) not in used:
                                    nw = [[j for j in i] for i in tmp]
                                    used.add(getS(nw))
                                    q.append([nw,cnt+1])
                                tmp[nr][nc],tmp[i][j] = tmp[i][j],tmp[nr][nc]        
        return -1
      
-----------------------------------------------------------------------------------
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(d) for row in board for d in row)
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index('0')))
        steps, height, width = 0, len(board), len(board[0]) 
        while dq:
            for _ in range(len(dq)):
                t, i= dq.popleft()
                if t == '123450':
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]
                        ch[i], ch[r * width + c] = ch[r * width + c], '0' # swap '0' and its neighbor.
                        s = ''.join(ch)
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))
            steps += 1              
        return -1
