'''
There is an 8 x 8 chessboard containing n pieces (rooks, queens, or bishops). You are given a string array pieces of length n, where pieces[i] describes the type (rook, queen, or bishop) of the ith piece. In addition, you are given a 2D integer array positions also of length n, where positions[i] = [ri, ci] indicates that the ith piece is currently at the 1-based coordinate (ri, ci) on the chessboard.

When making a move for a piece, you choose a destination square that the piece will travel toward and stop on.

A rook can only travel horizontally or vertically from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), or (r, c-1).
A queen can only travel horizontally, vertically, or diagonally from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
A bishop can only travel diagonally from (r, c) to the direction of (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
You must make a move for every piece on the board simultaneously. A move combination consists of all the moves performed on all the given pieces. Every second, each piece will instantaneously travel one square towards their destination if they are not already at it. All pieces start traveling at the 0th second. A move combination is invalid if, at a given time, two or more pieces occupy the same square.

Return the number of valid move combinations​​​​​.

Notes:

No two pieces will start in the same square.
You may choose the square a piece is already on as its destination.
If two pieces are directly adjacent to each other, it is valid for them to move past each other and swap positions in one second.
 
 '''

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        board = [[set() for _ in range(8)] for _ in range(8)]
        n = len(pieces)
        for pos in positions:
            pos[0] -= 1
            pos[1] -= 1
        all_time = set(range(1, 8))
        def recur(i):
            if i == n:
                return 1
            ans = 0
            line = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            r, c = positions[i]
            if not board[r][c] & all_time:
                board[r][c] |= all_time
                ans += recur(i + 1)
                board[r][c].clear()
            directions = []
            if pieces[i] in ("queen", "rook"):
                directions.extend(line)
            if pieces[i] in ("queen", "bishop"):
                directions.extend(diag)                
            for dr, dc in directions:
                x, y = r + dr, c + dc
                count = 1
                while 0 <= x < 8 and 0 <= y < 8 and count not in board[x][y]:
                    board[x][y].add(count)
                    count += 1
                    rest = set(range(count, 8))
                    if not board[x][y] & rest:
                        board[x][y] |= rest
                        ans += recur(i + 1)
                        board[x][y] -= rest
                    x += dr
                    y += dc
                count -= 1
                x -= dr
                y -= dc
                while count:
                    board[x][y].remove(count)
                    count -= 1
                    x -= dr
                    y -= dc
            return ans
        return recur(0)
