'''
There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a value associated with it, and the root of the tree is node 0.

To represent this tree, you are given an integer array nums and a 2D array edges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree.

Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.

An ancestor of a node i is any other node on the shortest path from node i to the root. A node is not considered an ancestor of itself.

Return an array ans of size n, where ans[i] is the closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ancestor.
'''

class Solution:
	def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
		def gcd(a,b):
			if b==0:
				return a
			return gcd(b,a%b)
		coprimes=defaultdict(set)

		for i in range(1,51):
			for j in range(i,51):
				if gcd(i,j)==1:
					coprimes[i].add(j)
					coprimes[j].add(i)

		n=len(nums)
		G=[[] for _ in range(n)]
		for u,v in edges:
			G[u].append(v)
			G[v].append(u)
		path=defaultdict(list)
		ans=[None]*n
		def dfs(node,prev,path):
			if nums[node] not in path:
				ans[node]=-1
			else:
				ans[node]=path[nums[node]][-1]
			for x in coprimes[nums[node]]:
				path[x].append(node)
			for child in G[node]:
				if child==prev:
					continue
				dfs(child,node,path)
			for x in coprimes[nums[node]]:
				path[x].pop()
				if len(path[x])==0:
					del path[x]
		dfs(0,None,path)
		return ans
  
--------------------------------------------------------------------------------------------------
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        
        gcdset = [set() for i in range(51)]
        for i in range(1,51):
            for j in range(1,51):
                if math.gcd(i,j) == 1:
                    gcdset[i].add(j)
                    gcdset[j].add(i)
        
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        ans = [-1]*len(nums)
        q = [[0, {}]]
        seen = set([0])
        depth = 0
        while q:
            temp = []
            for node, ancestors in q:
                index_depth = (-1,-1)
                for anc in list(ancestors.keys()):
                    if anc in gcdset[nums[node]]:
                        index, d = ancestors[anc]
                        if d > index_depth[1]:
                            index_depth = (index,d)
                ans[node] = index_depth[0]
                
                copy = ancestors.copy()
                copy[nums[node]] = (node,depth)
                
                for child in graph[node]:
                    if child not in seen:
                        seen.add(child)
                        temp.append([child, copy])
            q = temp
            depth += 1
        return ans
'''

**:)**
