'''
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.
'''

class SubrectangleQueries(object):

    def __init__(self, rectangle):
        self.rectangle = copy.deepcopy(rectangle)

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue
				
    def getValue(self, row, col):
        return self.rectangle[row][col]
      
--------------------------------------------------
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
		# make a new dictionary
        self.rec = {}
		# with enumerate we can iterate through the list rectangle, 
		# taking each row and its index
        for i, row in enumerate(rectangle):
			# we map each row to its index as it`s more space-efficent
            self.rec[i] = row
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
		# we want to put new value from row1 to row2, so we iterate through them
        for i in range(row1, row2+1):
			# we put new value only from col1 to col2, but we leave other columns as is
            self.rec[i] = self.rec[i][:col1] + [newValue]*(col2-col1+1) + self.rec[i][col2+1:]

    def getValue(self, row: int, col: int) -> int:
		# take row (of type list) from dictionary rec, take specified col from row
        return self.rec[row][col]
---------------------------------------------------------
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.ops = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.ops.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for row1, col1, row2, col2, val in reversed(self.ops):
            if row >= row1 and col >= col1 and row <= row2 and col <= col2:
                return val
        return self.rectangle[row][col]
    
