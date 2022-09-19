'''
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
'''


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obst = { (x,y) for x,y in obstacles}
        
        dist = 0
        x = 0
        y = 0
        dx,dy = 0,1
        
        for com in commands:
            if com == -2:
                dx,dy = -dy,dx
            
            elif com == -1:
                dx,dy = dy,-dx
            else:
                for _ in range(com): #so we have some k steps to move!
                    if (x+dx, y + dy) in obst: #we move for as long as we can - increas x ,y by dx,dy
                        break
                    x = x+dx
                    y = y + dy
                    
                dist = max(dist, x*x+y*y)
        
        return dist
            
