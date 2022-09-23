'''
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
'''

class DetectSquares:

    def __init__(self):
        self.mapp = {}
        
    def add(self, point: List[int]) -> None:
        if tuple(point) not in self.mapp:
            self.mapp[tuple(point)] = 0
        self.mapp[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0 
        px,py = point
        for x,y in self.mapp.keys():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (x,py) in self.mapp and (px,y) in self.mapp:
                res += self.mapp[(x,py)] * self.mapp[(px,y)] * self.mapp[(x,y)]
        return res 
