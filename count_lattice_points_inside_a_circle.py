'''
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:

A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.
'''

class Solution:
   def countLatticePoints(self, circles: List[List[int]]) -> int:

    res = set()
    
    def point(x, y, r):
        nonlocal res
        
        for a in range(x-r, x+r+1):
            for b in range(y-r, y+r+1):
                if (a-x)*(a-x) + (b-y)*(b-y) <= r*r:
                    res.add((a,b))

        return res
        
    for x in circles:
        
        point(x[0],x[1],x[2])
        
    return len(res)
  
-------------------------------------------
def countLatticePoints(self, circles: List[List[int]]) -> int:
    
    pt={} #to keep track of the points; we can also use set 
    check=[] # a list to work with all unique circle datas
    ret = 0 # returns the count 
    for circle in circles: # we go through every points
        if circle not in check: # checking that if we have never faced the data before
            check.append(circle) # adding the data as we checked the point now
            x,y,r = circle[0],circle[1],circle[2] 
            for i in range(x-r,x+r+1):
                for j in range(y-r,y+r+1):
                    if ((x-i)**2+(y-j)**2)<=r*r: # using circle formula to check a point is inside of a given circle
					# formula: A point (h,k) is on or inside of a circle if (x-h)^2+(y-k)^2 <= r^2
                        key  = '(' + str(i) + '+' + str(j) + ')' # we add the point in our hashtable as key '(i+j)' and increment the countvalue i.e. ret
                        if key not in pt:
                            pt[key] = 1
                            ret += 1
                        else: pt[key] += 1
            
    #print(pt)
    return ret
  
--------------------------------------------------------------
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        visited = set()
        res = 0
        for cx, cy, r in circles:
            for x in range(cx-r,cx+r+1):
                for y in range(cy-r,cy+r+1):
                    if (x,y) not in visited and (x-cx)**2 + (y-cy)**2 <= r**2:
                        visited.add((x,y))
                        res += 1
        return res
  
