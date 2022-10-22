'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


Approach:

Sort the points array in increasing order based on ending x index.
Initialize res=1 which means always consider first balloon
Initialize a variable shoot which indicates the current fixed point to shoot the arrow. Initialize it to ending index of first balloon.
Loop through all the indexes. If starting index of balloon is less than the shoot , then continue. This means that the current shoot index can burst this balloon. Else increase result by one and assign shoot as ending index of current balloon
Return res
'''



class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: x[1])
        
        res=1
        shoot=points[0][1]
        n=len(points)
        for i in range(1,n):
            if(points[i][0]<=shoot):
                continue
                
            else:
                res=res+1
                shoot=points[i][1]
                
        return res
