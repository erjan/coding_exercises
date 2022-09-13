'''
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 
 '''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1,point2):
            return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
            
        D=[
        dist(p1,p2),
        dist(p1,p3),
        dist(p1,p4),
        dist(p2,p3),
        dist(p2,p4),
        dist(p3,p4)
        ]
        D.sort()
        return 0<D[0]==D[1]==D[2]==D[3] and D[4]==D[5]
      
--------------------------------------------------------------------------------------------------------------
def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:       
	def dis(d1, d2):
		return (d1[0]-d2[0])**2+(d1[1]-d2[1])**2

	s = set([dis(d1, d2) for d1, d2 in [[p1,p2],[p1,p3],[p1,p4],[p2,p3],[p2,p4],[p3,p4]]])
	if len(s) == 2 and 0 not in s: return True
	return False
