'''
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud = 0
        rl = 0
        m = moves
        for i in range(len(m)):

            if m[i] == 'U':
                ud+=1
            elif m[i] == 'D':
                ud-=1
            elif m[i] == 'R':
                rl-=1
            elif m[i] == 'L':
                rl+=1

        print(ud,rl)
        if ud == 0 and rl == 0:
            return True
        return False

def judgeCircle(self, moves: str) -> bool:
      return moves.count('R') ==  moves.count('L') ==  moves.count('U') ==  moves.count('D') 
