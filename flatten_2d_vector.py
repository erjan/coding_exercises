'''

Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:

Vector2D(int[][] vec) initializes the object with the 2D vector vec.
next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
hasNext() returns true if there are still some elements in the vector, and false otherwise.
'''

def __init__(self, v: List[List[int]]):
    self.v = v
    self.col = 0
    self.row = 0

def next(self) -> int:
    self.hasNext()
    val = self.v[self.row][self.col]
    self.col += 1
    return val

def hasNext(self) -> bool:
    while self.row < len(self.v):
        if self.col < len(self.v[self.row]):
            return True
        self.row += 1
        self.col = 0
    
    return False
