'''
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
 
 '''

There is only four situation that Tic-Tac-Toe is invalid:

two players are not taking turns making move
"O" player makes move before "X" player
"X" player wins but "O" player continues to make move
"O" player wins but "X" player continues to make move
class Solution(object):
    def validTicTacToe(self, board):
        def win(s): # return True if the player who use s wins
            if board[0][0]==s and board[0][1]==s and board[0][2]==s: return True
            if board[1][0]==s and board[1][1]==s and board[1][2]==s: return True
            if board[2][0]==s and board[2][1]==s and board[2][2]==s: return True
            if board[0][0]==s and board[1][0]==s and board[2][0]==s: return True
            if board[0][1]==s and board[1][1]==s and board[2][1]==s: return True
            if board[0][2]==s and board[1][2]==s and board[2][2]==s: return True
            if board[0][0]==s and board[1][1]==s and board[2][2]==s: return True
            if board[0][2]==s and board[1][1]==s and board[2][0]==s: return True
            return False
        
        xNo, oNo=0, 0
        for row in board:
            xNo+=row.count('X')
            oNo+=row.count('O')
        if oNo>xNo or xNo-oNo>=2: # "X" not making move first or not taking turns making move
            return False
        if xNo>=3:
            if xNo==oNo and win('X'): # put another "O" after "X" player winning
                return False
            if xNo!=oNo and win('O'): # put another "X" after "O" player winning
                return False
        return True
-----------------------------------------------------------------------------------------------------
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # count the number of x and o
        xCount = oCount = 0
        
        # Easy state representation of valid win lines
        # Indexes: 0,1,2 represent rows. 3,4,5 represent columns. 6,7 represent diagonals (6 - \, 7 - /)
        arr = [0]*8

        # Check over the whole board
        for i, row in enumerate(board):
            for j, ch in enumerate(row):

                # Check for X
                # steps: 
                # 1. increment xCount 
                # 2. add 1 to the row
                # 3. add 1 to the column
                # 4. add 1 to the diagonals if coordinates lie on diagonals
                if ch == 'X': 
                    xCount += 1
                    
                    arr[i] += 1
                    arr[j+3] += 1
                    
                    # check left to right diagonal (\)
                    if i == j: arr[6] += 1
                    # check right to left diagonal (/)
                    if i == 2-j: arr[7] += 1

                # Check for O
                # steps: 
                # 1. increment oCount 
                # 2. subtract 1 from the row
                # 3. subtract 1 from the column
                # 4. subtract 1 from the diagonals if coordinates lie on diagonals
                if ch == 'O': 
                    oCount += 1
                    
                    arr[i] -= 1
                    arr[j+3] -= 1
                    
                    # check left to right diagonal (\)
                    if i == j: arr[6] -= 1
                    # check right to left diagonal (/)
                    if i == 2-j: arr[7] -= 1
                        
        # win conditions:
        # if 3 exists in array: X wins
        # if -3 exists: O wins
        # For more visualization, try drawing this
        xWin, oWin = 3 in arr, -3 in arr
        
        # Case 1: both are shown as winning (invalid state as X wins before O) eg: ["XXX","   ","OOO"]
        if xWin and oWin: return False

        # Case 2: X wins that indicates that the difference in count should be 1. As X plays before O
        if xWin and xCount - oCount != 1 : return False
        
        # Case 3: O wins that indicates that the difference in count should be 0. As X plays before O
        if oWin and xCount - oCount != 0 : return False
        
        # Case 4: both of them have to play alternate moves, hence difference can only be 1 or 0
        if xCount - oCount not in (0,1): return False
        
        # If all cases pass, board is valid
        return True
--------------------------------------------------------------------------------
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def wins(c: str) -> bool:
            cols = map(lambda x:''.join(x), zip(*board))
            diags = map(lambda x:''.join(x),
                        ((board[i][i] for i in range(3)),
                         (board[i][-i-1] for i in range(3))))
            return any(row == c * 3 for row in itertools.chain.from_iterable((board, cols, diags)))
        
        Xwins = wins('X')
        Owins = wins('O')
        
        if Xwins and Owins:
            return False
        
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)
        
        if not Xwins and not Owins:
            return countX == countO or countX == countO + 1
        if Xwins:
            return countX == countO + 1
        return countX == countO
      
