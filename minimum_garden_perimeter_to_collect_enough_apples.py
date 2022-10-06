'''
In a garden represented as an infinite 2D grid, there is an apple tree planted at every integer coordinate. The apple tree planted at an integer coordinate (i, j) has |i| + |j| apples growing on it.

You will buy an axis-aligned square plot of land that is centered at (0, 0).

Given an integer neededApples, return the minimum perimeter of a plot such that at least neededApples apples are inside or on the perimeter of that plot.

The value of |x| is defined as:

x if x >= 0
-x if x < 0
'''

For half of side length 1: it has [1] * 4 apples on side edges, [1 * 2] * 4 apples on corners;
For half of side length 2: it has [2,3,3] * 4 apples on side edges, [2 * 2] * 4 apples on corners.
For half of side length 3, it has [3,4,4,5,5] * 4 apples on side edges, [3 * 2] * 4 apples on corners.
...
Therefore, by mathematical induction, for half of side length n, it has [n, (n+1)* 2, ... (2n-1) * 2] * 4 apples on side edges, [n * 2] * 4 apples on corners. Hence, it will have (3 * n^2 - 2 * n) * 4 apples on side edges since it is an arithmetic sequence from (n+1) to (2n-1), then sum it over to get the total of apples, once it's greater than needed apples, simply return its perimeter.
class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        num_apples = 0
        for radius in range(1, 1000000):
            edge_apples = (3*radius**2 - 2*radius)*4
            corner_apples = 2*radius * 4 
            num_apples += corner_apples + edge_apples
            if num_apples >= neededApples:
                return 2*radius*4 
              
--------------------------------------------------------------
    def minimumPerimeter(self, neededApples: int) -> int:
        lo, hi = 1, 100000
        while lo < hi:
            m = (lo+hi)//2
            n = 2*m*(m+1)*(2*m+1)
            if n < neededApples: lo = m+1
            else: hi = m
        return 8*lo
      
-------------------------------------------------------------------------------
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def apples(r):
            return 2 * r * (r + 1) * (2*r + 1)
        
        low, high = 1, neededApples
        while low <= high:
            mid = (low + high) // 2
            total = apples(mid)
            if total == neededApples:
                return 8*mid
            elif total < neededApples:
                low = mid + 1
            else:
                high = mid - 1
        
        return 8 * (mid + (total < neededApples))
