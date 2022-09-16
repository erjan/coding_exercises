'''
A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
'''

class Robot:

    def __init__(self, width: int, height: int):
        self.perimeter = 2*width + 2*(height - 2)
        self.pos = 0
        self.atStart = True

        self.bottomRight = width - 1
        self.topRight = self.bottomRight + (height - 1)
        self.topLeft = self.topRight + (width - 1)

    def step(self, num: int) -> None:
        self.atStart = False
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        if 0 <= self.pos <= self.bottomRight:
            return [self.pos, 0]

        if self.bottomRight < self.pos <= self.topRight:
            return [self.bottomRight, self.pos - self.bottomRight]

        if self.topRight < self.pos <= self.topLeft:
            return [self.bottomRight - (self.pos - self.topRight), self.topRight - self.bottomRight]
        
        return [0, self.topRight - self.bottomRight - (self.pos - self.topLeft)]

    def getDir(self) -> str:
        if self.atStart or 0 < self.pos <= self.bottomRight:
            return 'East'

        if self.bottomRight < self.pos <= self.topRight:
            return 'North'

        if self.topRight < self.pos <= self.topLeft:
            return 'West'
        
        return 'South'
      
----------------------------------------
class Robot:

    def __init__(self, w: int, h: int):

        self.build = {0:[[0, 0], 'e']}
        self.moves = 0
        self.isMoved = False
        
        x, y = 1, 0
        d = 'e'
        count = 1
        while x or y:
            
            self.build[count] = [[x, y], d]
            
            
            if x == w - 1 and d == 'e':
                d = 'n'
            if y == h - 1 and d == 'n':
                d = 'w'
            if x == 0 and d == 'w':
                d = 's'
  
            
            
            if d == 'e':
                x += 1
                
            if d == 'n':
                y += 1
            if d == 'w':
                x -= 1
            if d == 's':
                y -= 1
            
            count += 1
        
        # print(self.build)
    

    def step(self, num: int) -> None:
        self.isMoved = True
        self.moves += num
        self.moves %= len(self.build)
 
    def getPos(self) -> List[int]:
        
        pos, d = self.build[self.moves]
        
        return pos
        

    def getDir(self) -> str:
        
        pos, d = self.build[self.moves]
        
        dirMap = {'e':'East', 'n': 'North', 's':"South", 'w': 'West'}
        
        
        if self.isMoved and self.moves == 0:
            return 'South'
        
        return dirMap[d]
