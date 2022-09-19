'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        while True:
            for do in instructions:
                if do == 'G':
                    x += directions[i][0]
                    y += directions[i][1]
                elif do == 'R':
                    i = (i + 1) % 4
                else:
                    i = (i - 1) % 4
                    
            if i == 0:
                return x == 0 and y == 0
