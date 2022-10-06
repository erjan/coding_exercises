'''
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
'''

First, move every stone to the right, (or you can rotate the box first and then drop stones. Both as fine).
The current location of stone does not matter.
We only need to remember how many stones each interval (seperated by obstacles) has,
and place the stones before the first seeing obstacle.

Second, rotate the box. Same as Leetcode problem # 48 Rotate Image.

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # move stones to right, row by row
        for i in range(len(box)):
            stone = 0
            for j in range(len(box[0])):
                if box[i][j] == '#': # if a stone
                    stone += 1
                    box[i][j] = '.'
                elif box[i][j] == '*': # if a obstacle
                    for m in range(stone):
                        box[i][j-m-1] = '#'
                    stone = 0
            # if reaches the end of j, but still have stone
            if stone != 0:
                for m in range(stone):
                        box[i][j-m] = '#'
        
        # rotate box, same as leetcode #48
        box[:]  = zip(*box[::-1])
        
        return box
      
      
