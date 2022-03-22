'''
A Roomba robot is currently sitting in a Cartesian plane at (0, 0). You are given a list of its moves that it will make, containing NORTH, SOUTH, WEST, and EAST.

Return whether after its moves it will end up in the coordinate (x, y).

Constraints

n ≤ 100,000 where n is length of moves
'''

class Solution:
    def solve(self, moves, x, y):

        mx = 0
        my = 0
        for m in moves:

            if m == 'NORTH':
                my+=1
            if m == 'SOUTH':
                my-=1
            if m == 'WEST':
                mx -=1
            if m == 'EAST':
                mx+=1
        
        if mx == x and my == y:
            return True
        return False

        
