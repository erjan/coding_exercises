'''
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
'''





class Solution(object):

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            self.p[parent_y] = parent_x 
            self.count-=1
            

    def find(self, x):
        while self.p[x] != x:
            x = self.p[x]
        return self.p[x]

    def removeStones(self, stones):
        self.p = range(len(stones))
        self.count = len(stones)
        for i in range(1, len(stones)):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j)
        return len(stones) - self.count
---------------------------------------------------------------------------------------------
class UnionFind:
	def __init__(self, n):
		self.root = list(range(n))

	def union(self, x, y):
		self.root[self.find(x)] = self.find(y)

	def find(self, x):
		if x != self.root[x]:
			self.root[x] = self.find(self.root[x])
		return self.root[x]

	def num_components(self):
		x = set([])
		for i in range(len(self.root)):
			x.add(self.find(i))
		return len(x)

class Solution:
	def removeStones(self, stones: List[List[int]]) -> int:
		uf = UnionFind(len(stones))

		col_prev = {}
		row_prev = {}
		for i, (x, y) in enumerate(stones):
			if x in row_prev:
				uf.union(i, row_prev[x])
			if y in col_prev:
				uf.union(i, col_prev[y])
			row_prev[x] = i
			col_prev[y] = i

		return len(stones) - uf.num_components()
