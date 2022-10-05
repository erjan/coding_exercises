'''
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
'''

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        How is Binary Search possible here?
        First we should understand that this is a Greedy Problem.
        
        Say we took the largest element in a column, if any of adjacent
        element is greater than the current Largest, we can just greedily go through
        the largest elements till we find a Peak Element
        
        In my Solution I am splitting column wise because in the hint it is given that width
        is more that the height.
        """
        start, end = 0, len(mat[0]) - 1
        while start <= end:
            cmid = start + (end - start) // 2
            
            # Finding the largest element in the middle Column
            ridx, curLargest = 0, float('-inf')
            for i in range(len(mat)):
                if mat[i][cmid] > curLargest:
                    curLargest = mat[i][cmid]
                    ridx= i 
            
            # Checking the adjacent element
            leftisBig = cmid > start and mat[ridx][cmid - 1] > mat[ridx][cmid]
            rightisBig = cmid < end and mat[ridx][cmid + 1] > mat[ridx][cmid]
            
            if not leftisBig and not rightisBig:
                return [ridx, cmid]
            
            if leftisBig:
                end = cmid - 1
            else:
                start = cmid + 1
                
-------------------------------------------------------------------------------

So the pseudo code for this solution is

Binary search in columns
Identify the max of each column.
a. Terminal condition: if it is larger than both left and right, return it
b. Else, if it is smaller than the left, search in the left-half columns. Otherwise, search in the right-half columns.


def findPeakGrid(self, mat):
    startCol = 0
    endCol = len(mat[0])-1
   
    while startCol <= endCol:
        midCol = (endCol+startCol)//2
        # 1. choose maxRow at current col to ensure this element larger than above and below
        maxRow = 0
        for row in range(len(mat)):
            if mat[row][midCol] >= mat[maxRow][midCol]:
                maxRow = row 
        # 2. move left or right to ensure this column is larger than at least left or right. Similar to Find a Peak Element
        low_left = midCol==0  or  mat[maxRow][midCol-1] < mat[maxRow][midCol]
        low_right = midCol == len(mat[0]) - 1 or mat[maxRow][midCol+1] < mat[maxRow][midCol]

        if low_left and low_right:      # we have found the peak element
            return [maxRow, midCol]
        elif not low_right:             # if right is larger, move to right
            startCol = midCol+1         
        else:                           # else move to left
            endCol = midCol-1
        
    return []
