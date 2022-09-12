'''
There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.
'''

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
        a,b,c = sorted((a,b,c))
        
        dif1 = b-a-1
        dif2 = c-b-1
        
        if dif1 == 0 and dif2 == 0:
            mini = 0
        
        elif dif1 == 0 or dif2 == 0 or dif1 == 1 or dif2 == 1:
            mini = 1
        
        else:
            mini = 2
            
        return [mini, dif1+dif2]
---------------------------------------
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        if x + 1 == y == z - 1:
            min_steps = 0
        elif y - x > 2 and z - y > 2:
            min_steps = 2
        else:
            min_steps = 1
        max_steps = z - x - 2
        return [min_steps, max_steps]
