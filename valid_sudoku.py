'''

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''

#my own solution - ugly
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = list()

        for i in range(len(board)):
            temp = list()
            for j in range(len(board)):
                if board[i][j] != '.':
                    temp.append(board[i][j])
            rows.append(temp)

        columns = list()

        for i in range(len(board)):
            temp = list()
            for j in range(len(board)):
                if board[j][i] != '.':
                    temp.append(board[j][i])
            columns.append(temp)

        # print(columns)

        # 3x3 sub grids

        s1 = list()
        for i in range(3):
            for j in range(3):
                if board[i][j] != '.':
                    s1.append(board[i][j])

        s2 = list()
        for i in range(3):
            for j in range(3, 6):
                if board[i][j] != '.':
                    s2.append(board[i][j])

        s3 = list()
        for i in range(3):
            for j in range(6, 9):
                if board[i][j] != '.':
                    s3.append(board[i][j])

        s4 = list()
        for i in range(3, 6):
            for j in range(3):
                if board[i][j] != '.':
                    s4.append(board[i][j])

        s5 = list()
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] != '.':
                    s5.append(board[i][j])

        s6 = list()
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] != '.':
                    s6.append(board[i][j])

        s7 = list()
        for i in range(6, 9):
            for j in range(3):
                if board[i][j] != '.':
                    s7.append(board[i][j])

        s8 = list()
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] != '.':
                    s8.append(board[i][j])

        s9 = list()
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] != '.':
                    s9.append(board[i][j])

        # checking rows:
        for r in rows:
            if len(r) != len(set(r)):
                print('row is bad', r)
                return False

        # #checking columns:
        for c in columns:
            if len(c) != len(set(c)):
                print('col is bad', c)
                return False

        # checking subgrids

        if len(s1) != len(set(s1)):
            return False

        if len(s2) != len(set(s2)):
            return False

        if len(s3) != len(set(s3)):
            return False

        if len(s4) != len(set(s4)):
            return False

        if len(s5) != len(set(s5)):
            return False

        if len(s6) != len(set(s6)):
            return False

        if len(s7) != len(set(s7)):
            return False

        if len(s8) != len(set(s8)):
            return False

        if len(s9) != len(set(s9)):
            return False
          
        del s1, s2, s3,s4,s5,s6,s7,s8,s9
        del columns, rows
        
        return True
      
      
      
#alternative solution

def isValidSudoku(self, board):
    return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

def is_row_valid(self, board):
    for row in board:
        if not self.is_unit_valid(row):
            return False
    return True

def is_col_valid(self, board):
    for col in zip(*board):
        if not self.is_unit_valid(col):
            return False
    return True
    
def is_square_valid(self, board):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
    return True
    
def is_unit_valid(self, unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)



#another


def isValidSudoku(self, board):
    seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    return len(seen) == len(set(seen))
