'''
You are given coordinates, a string that represents 
the coordinates of a square of the chessboard. Below is a chessboard for your reference.
'''

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        
        if coordinates[0] in 'aceg':
            if int(coordinates[1]) %2 == 0:
                return True
            else:
                return False
                    
        if coordinates[0] in 'bdfh':
            if int(coordinates[1]) %2 == 1:
                return True
            else:
                return False
