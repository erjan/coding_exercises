 '''
 There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.
'''
 
 
 def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range (0,len(s)):
             ch= s [i:]
             actualPos = copy.copy(startPos)
             numberSteps=0
             for step in ch :
                    if step == 'U':
                        actualPos[0]-=1
                    elif step == 'D':
                        actualPos[0] +=1
                    elif step == 'R':
                        actualPos[1]+=1
                    elif step =='L':
                        actualPos[1]-=1
                        
                    ## Condition of leaving the grid 
                    if actualPos[0]<0 or actualPos[1]<0 or actualPos[0]>n-1 or actualPos[1]> n-1 :
                        break
                    else: 
                        numberSteps +=1
                        
                   
             result.append (numberSteps)
                    
        return result
