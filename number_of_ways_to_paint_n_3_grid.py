'''
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
'''

class Solution:
    def numOfWays(self, n: int) -> int:
        '''
        https://www.***.org/ways-color-3n-board-using-4-colors/
        
        if lastline with 3 color (ABC):
            newline with 3-colors:(2 ways)
                BCA, CAB
            newline with 2-colors:(2 ways)
                BAB, BCB
        
        if lastline with 2 color (ABA):
            newline with 3-colors:(2 ways)
                BAC, CAB
            newline with 2-colors:(3 ways)
                BAB, BCB, CAC
        '''
        
        # num of single line with 3 colors, 1 * 3!
        color3 = 6
        # num of single line with 2 colors, 3 * 2
        color2 = 6
        
        for i in range(n-1):
            temp = color3 
            color3 = (2*color3 + 2*color2)
            color2 = (2*temp + 3*color2)
        
        return (color3 + color2) % (10 ** 9 + 7)
