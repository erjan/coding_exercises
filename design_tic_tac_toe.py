'''
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
'''

class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for i in range(n)]
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] == 0: self.board[row][col] = player
        
        for i in range(self.size):
            if self.board[row][i] != player: break
            if i == self.size-1:
                return player
        
        for i in range(self.size):
            if self.board[i][col] != player: break
            if i == self.size-1:
                return player
            
        for i in range(self.size):
            if self.board[i][i] != player: break
            if i == self.size-1:
                return player
        
        for i in range(self.size):
            if self.board[i][self.size-i-1] != player: break
            if i == self.size-1:
                return player
        
        return 0
      
------------------------
class TicTacToe:

    def __init__(self, n: int):
        self.board, self.size = [ [0] * n for _ in range(n) ], n
        
    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] != 0: return 0
        
        self.board[row][col] = player
        
        def r()-> bool:
            return sum(1 for j in range(self.size) if self.board[row][j] == player) == self.size

        def c() -> bool:
            return sum(1 for i in range(self.size) if self.board[i][col] == player) == self.size

        def d() -> bool:
            return sum(1 for i in range(self.size) if self.board[i][i] == player) == self.size

        def ad() -> bool:
            return sum(1 for i in range(self.size - 1, -1, -1) if self.board[i][self.size - i - 1] == player) == self.size
        
        return player if (r() or c() or d() or ad()) else 0
      
      ---------------------------------------
      class TicTacToe(object):
      def __init__(self, n):
        count = collections.Counter()
        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move
