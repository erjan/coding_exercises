'''
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.
'''


class Solution:
    def numberOfBoomerangs(self, points):
        n = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                # NOTE: x,y == a,b can only be registered once, so...
				#       radius=0 never has enough points to make a false triplet
                key = (x-a)**2 + (y-b)**2
                if key in counter:
                    n += 2*counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n
      
----------------------------------------------

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3: # tuple must have at least 3 elements
            return 0
        
        res = 0
        # idea: iterate all points, calculate distances between each point and other points,
		# put distances in dictionaries. If there are values greater than 1, 
		# meaning there are multiple points have the same distance with it.
		# Since order matters, total combination numbers would be val * (val - 1).
        for p1 in points:
            tmp = {}
            for p2 in points:
                d = self.dist(p1, p2)
                tmp[d] = tmp.get(d, 0) + 1
            for val in [val for val in tmp.values() if val > 1]:
                res += val * (val - 1)
                
        return res
        
    def dist(self, p1, p2): # calculate pointwise distance
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
      
--------------------------------------------------------      
