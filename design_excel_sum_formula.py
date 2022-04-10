'''
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
'''


class Excel:

    def __init__(self, height: int, width: str):
        self.mat = [[0]*(self.Ato0(width) + 1) for _ in range(height)]
    
    def Ato0(self, c):
        return ord(c) - ord("A")

    def set(self, row: int, column: str, val: int) -> None:
        self.mat[row - 1][self.Ato0(column)] = val
    
    def get(self, row: int, column: str) -> int:
        r, c = row -1, self.Ato0(column)
        if type(self.mat[r][c]) is int:
            return self.mat[r][c]
        return self.sum(row, column, self.mat[r][c])
        
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        acum = 0
        for sub in numbers:
            if ":" not in sub:
                w = sub[0]
                h = sub[1:]
                acum += self.get(int(h), w)
            else:
                tl, br = sub.split(":")
                w1, h1 = self.Ato0(tl[0]), int(tl[1:]) - 1
                w2, h2 = self.Ato0(br[0]), int(br[1:]) - 1
                for i in range(h1, h2+1):
                    for j in range(w1, w2+1):
                        acum += self.get(i + 1, chr(j + 65))
        self.mat[row - 1][self.Ato0(column)] = numbers
        return acum
