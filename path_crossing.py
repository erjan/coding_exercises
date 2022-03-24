'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one 
unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a 
location you have previously visited. Return false otherwise.
'''


#my own solution
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        coordinates = []
        x = 0
        y = 0
        coordinates.append([x, y])
        for p in path:

            if p == 'N':
                y += 1
            if p == 'S':
                y -= 1

            if p == 'E':
                x += 1
            if p == 'W':
                x -= 1
            if [x, y] in coordinates:
                print('same again')
                return True                
            else:
                coordinates.append([x, y])
                
        return False
