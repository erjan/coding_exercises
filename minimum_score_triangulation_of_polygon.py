'''
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.
'''

#dp bottom up
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
    	SP, L = [[0]*50 for _ in range(50)], len(A)
    	for i in range(2,L):
    		for j in range(L-i):
    			s, e, SP[s][e] = j, j + i, math.inf
    			for k in range(s+1,e): SP[s][e] = min(SP[s][e], A[s]*A[k]*A[e] + SP[s][k] + SP[k][e])
    	return SP[0][L-1]
    
-------------------------------------------------------------------------------------------------------------------
#dp top down 

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
    	SP, LA = [[0]*50 for i in range(50)], len(A)
    	def MinPoly(a,b):
    		L, m = b - a + 1, math.inf; 
    		if SP[a][b] != 0 or L < 3: return SP[a][b]
    		for i in range(a+1,b): m = min(m, A[a]*A[i]*A[b] + MinPoly(a,i) + MinPoly(i,b))
    		SP[a][b] = m; return SP[a][b]
    	return MinPoly(0,LA-1)
