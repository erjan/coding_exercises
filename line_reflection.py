'''
Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

Note that there can be repeated points.

'''

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        max_point = float('-inf')
        min_point = float('inf')
        
        x_positions = dict()
        
        for x in points:
            if x[0] in x_positions:
                x_positions[x[0]].add(x[1])
            else:
                x_positions[x[0]] = {x[1]}
            
            if x[0] > max_point:
                max_point = x[0]
            if x[0] < min_point:
                min_point = x[0]
        
        mid = (max_point + min_point) / 2
        
        for x in x_positions:
            if x == mid:
                continue
            if 2*mid-x not in x_positions:
                return False
            if x_positions[x] != x_positions[2*mid-x]:
                return False
                
        return True
