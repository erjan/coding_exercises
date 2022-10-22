'''
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.


'''

Basic idea:
Use BFS to find one shortest path for each character one time, and then connect all paths.

Stand at index (x, y) first, initially it's (0, 0)
Then did BFS to find targeted character, record the shortest path
update x, y
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde","fghij","klmno","pqrst","uvwxy","z0000"] # fill "0" in blank
        res = []
        x0, y0 = 0, 0
        for s in target: #each time, find shorest path for one char
                x, y, path = self.bfs(board, x0, y0, s)
                x0, y0 = x, y # update intial index
                res.append(path)
        return "".join(res)
                
        
    # Input: initial index (indx, idy), one char (goal this time)
    # Output: index and path for the goal char
    def bfs(self, board, idx, idy, goal):
        m, n = len(board), len(board[0])
        queue = collections.deque([(idx, idy,"")])
        visited = set() # array will TLE
        dirt = {'U':(-1, 0),"D":(1,0),"L":(0, -1),"R":(0, 1)}
        while queue:
                a, b, path = queue.popleft()
                visited.add(path)
                if board[a][b] == goal:
                        return (a, b, path+"!") #return path and index
                for sign in dirt:
                        i, j = a + dirt[sign][0], b + dirt[sign][1]
                        if 0<=i<m and 0<=j<n and board[i][j]!="0" and path+sign not in visited:
                                queue.append((i, j, path+sign))
        return -1
      
----------------------------------------------------------------------------------------------------

