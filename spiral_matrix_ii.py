'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''


class Solution:
    def generateMatrix(self, n):
        matrix = []
        if not n: return matrix

        # construct a matrix of zeros
        for row in range(n):
            rowArray = []
            for col in range(n):
                rowArray.append(0)
            matrix.append(rowArray)

        # layer by layer strategy
        num = 1
        top = 0 # top layer: top row index
        right = n - 1 # right layer: right col index
        down = n - 1 # bottom layer: bottom row index
        left = 0 # left layer: left col index
		 
		 # while layers closing inward but not overlapping. if overlap = reached end of spiral matrix
        while left <= right and top <= down: 
            # top row
            for i in range(left, right+1): # from left to right. right + 1 to reach the last position in a row
                matrix[top][i] = num # to fill top row, fix the top row index and increment the col position
                num += 1 # update num
            top += 1 # after traversing top row, move top row index inward(downward) by one unit

            # right col
            for i in range(top, down+1): # from top to bottom. bottom + 1 to reach the last positin in a col
                matrix[i][right] = num # to fill the right col, fix the right col index and increment the row position
                num += 1 # update num
            right -= 1 # after traversing right col, move right col index inward(towards the left) by one unit

            # bottom row
            for i in range(right, left-1, -1): # from left to right, in reverse order. left-1 to reach the leftmost position in a row
                matrix[down][i] = num
                num += 1 # update num
            down -= 1 # after traversing bottom row, move bottom row index inward(upward) by one unit

            # left col
            for i in range(down, top-1, -1): # from bottom to top, in reverse order. top-1 to reach the topmost position in a col
                matrix[i][left] = num # to fill the left col, fix the left col index and increment the row position
                num += 1
            left += 1 # after traversing left col, move left col index inward(towards the right) by one unit

            # repeat until top-bottom or left-right indices collide (ie. have completed all layers)
        return matrix
