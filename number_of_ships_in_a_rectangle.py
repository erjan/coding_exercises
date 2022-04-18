'''
(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

constraints:
On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000
topRight != bottomLeft
'''




Intuition:
Leaves are single grid points, either containing ships or not. Our goal is to count all the leaves containing ships.

def countShips(self, sea, topRight, bottomLeft):
	x1, y1 = bottomLeft.x, bottomLeft.y
	x2, y2 = topRight.x, topRight.y
	if x1 > x2 or y1 > y2 or not sea.hasShips(topRight, bottomLeft): 
		return 0
	if x1 == x2 and y1 == y2:
		return 1
	x, y = (x1+x2)//2, (y1+y2)//2
	return self.countShips(sea, Point(x,y2), Point(x1,y+1)) + \
		   self.countShips(sea, Point(x2,y2), Point(x+1,y+1)) + \
		   self.countShips(sea, Point(x,y), Point(x1,y1)) + \
		   self.countShips(sea, Point(x2,y), Point(x+1,y1))



----------------------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        X, Y = topRight.x - bottomLeft.x, topRight.y - bottomLeft.y

        if X == Y == 0: 
            // area is a point, hasShips returns exact count of ships: 1 or 0
            return sea.hasShips(topRight, bottomLeft)

        if not sea.hasShips(topRight, bottomLeft):
            return 0

        // there is at least 1 ship in the area
        // divide area to two by the longest edge
        if X > Y:
            half = bottomLeft.x + X // 2
            midTopRight = Point(half, topRight.y)
            midBottomLeft = Point(half + 1, bottomLeft.y)
            return self.countShips(sea, midTopRight, bottomLeft) + self.countShips(sea, topRight, midBottomLeft)

        else:
            half = bottomLeft.y + Y // 2
            midTopRight = Point(topRight.x, half)
            midBottomLeft = Point(bottomLeft.x, half + 1)
            return self.countShips(sea, midTopRight, bottomLeft) + self.countShips(sea, topRight, midBottomLeft)
          
          
--------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        filled_xs = []
        num_xs_found = 0
        result = 0
        def recur_x(left_x, right_x):
            nonlocal num_xs_found
            
            if num_xs_found == 10:
                return
            has_ships = sea.hasShips(Point(right_x, topRight.y), Point(left_x, bottomLeft.y))
            if has_ships:
                if right_x == left_x:
                    filled_xs.append(left_x)
                    num_xs_found += 1
                else:
                    mid_x = (left_x + right_x) // 2
                    recur_x(left_x, mid_x)
                    recur_x(mid_x + 1, right_x)
                
        def recur_y(x, bottom_y, top_y):
            nonlocal result            
                                                
            has_ships = sea.hasShips(Point(x, top_y), Point(x, bottom_y))
            if has_ships:
                if top_y == bottom_y:
                    result += 1
                else:
                    mid_y = (bottom_y + top_y) // 2
                    recur_y(x, bottom_y, mid_y)
                    recur_y(x, mid_y + 1, top_y)
        
        recur_x(bottomLeft.x, topRight.x)
        for x in filled_xs:
            recur_y(x, bottomLeft.y, topRight.y)
        return result
      
      
-----------------------------------------------------------------------------------------------------------
So the basic idea is to isolate single points as rectangles and count the number of such points that host a ship.

The brute force way to do this would be to simply iterate over all the points within and on the boundary, but that would clearly take well over 400 calls for a moderately large input.

This can be easily addressed by splitting the rectangle into two NON-OVERLAPPING parts at each step. First making horizontal splits, then making the vertical ones.

Here is the commented code,

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0
        def sliceRect(tr, bl):
            nonlocal res
            lx, rx, ly, ry = bl.x, tr.x, bl.y, tr.y
            
            # For the given bounding coordinates, we check if there is at least 1 ship in the rectangle
            if not sea.hasShips(tr, bl): return
            
            # If we have reached here, it means that the ractangle has at least 1 ship
            # If the rectangle is a single point, we increase the count
            if lx == rx and ly == ry:
                res += 1
                return
            
            # If the bottomLeft and topRight points have are at different heights, we horizontally slice the rectangle
            if ry-ly > 0:
                sliceRect(Point(rx, ry), Point(lx, (ry+ly+1)//2))
                sliceRect(Point(rx, (ry+ly+1)//2-1), Point(lx, ly))
                
            # If the bottomLeft and topRight points have horizontal space between them, we vertically slice the recatngle
            elif rx-lx > 0:
                sliceRect(Point(rx, ry), Point((rx+lx+1)//2, ly))
                sliceRect(Point((rx+lx+1)//2-1, ry), Point(lx, ly))
            # In both the above slices, the important point to not is that there is NO OVERLAP
            return
        sliceRect(topRight, bottomLeft)
        return res
      
------------------------------------------------------------------------------
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        filled_xs = []
        num_xs_found = 0
        result = 0
        def recur_x(left_x, right_x):
            nonlocal num_xs_found
            
            if num_xs_found == 10:
                return
            has_ships = sea.hasShips(Point(right_x, topRight.y), Point(left_x, bottomLeft.y))
            if has_ships:
                if right_x == left_x:
                    filled_xs.append(left_x)
                    num_xs_found += 1
                else:
                    mid_x = (left_x + right_x) // 2
                    recur_x(left_x, mid_x)
                    recur_x(mid_x + 1, right_x)
                
        def recur_y(x, bottom_y, top_y):
            nonlocal result            
                                                
            has_ships = sea.hasShips(Point(x, top_y), Point(x, bottom_y))
            if has_ships:
                if top_y == bottom_y:
                    result += 1
                else:
                    mid_y = (bottom_y + top_y) // 2
                    recur_y(x, bottom_y, mid_y)
                    recur_y(x, mid_y + 1, top_y)
        
        recur_x(bottomLeft.x, topRight.x)
        for x in filled_xs:
            recur_y(x, bottomLeft.y, topRight.y)
        return result
