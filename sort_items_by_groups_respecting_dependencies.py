'''
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.
'''

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n): 
            if group[i] == -1: group[i] = i + m # re-group 
        
        graph0 = {} # digraph of groups 
        indeg0 = [0]*(m+n) # indegree of groups 
        
        graph1 = {} # digrpah of items 
        indeg1 = [0]*n # indegree of items
        
        for i, x in enumerate(beforeItems): 
            for xx in x: 
                if group[xx] != group[i]: 
                    graph0.setdefault(group[xx], []).append(group[i])
                    indeg0[group[i]] += 1
                graph1.setdefault(xx, []).append(i)
                indeg1[i] += 1
        
        def fn(graph, indeg): 
            """Return topological sort of graph using Kahn's algo."""
            ans = []
            stack = [k for k in range(len(indeg)) if indeg[k] == 0]
            while stack: 
                n = stack.pop()
                ans.append(n)
                for nn in graph.get(n, []):
                    indeg[nn] -= 1
                    if indeg[nn] == 0: stack.append(nn)
            return ans 
        
        tp0 = fn(graph0, indeg0) 
        if len(tp0) != len(indeg0): return [] 
        
        tp1 = fn(graph1, indeg1)
        if len(tp1) != len(indeg1): return []
        
        mp0 = {x: i for i, x in enumerate(tp0)}
        mp1 = {x: i for i, x in enumerate(tp1)}
        
        return sorted(range(n), key=lambda x: (mp0[group[x]], mp1[x]))
----------------------------------------------------------------------------------------------------------
from collections import defaultdict
class Cyclic(object):
	def __init__(self,n,g):
		super(Cyclic,self).__init__()
		self.vertices=n
		self.isCylicAns=False
		self.g=g
	def isCylic(self):
		used=[0 for i in range(self.vertices)]
		for i in range(0,self.vertices):
			if used[i]==0:
				self.dfs(i,used)
				if self.isCylicAns==True:
					return True
		return False
	def dfs(self,v,used):
		used[v]=1
		for i in self.g[v]:
			if used[i]==1:
				self.isCylicAns=True
				return
			elif used[i]==0:
				self.dfs(i,used)
		used[v]=2
class TopoSort(object):
	def __init__(self, n,g):
		super(TopoSort, self).__init__()
		self.vertices=n
		self.g=g
	def Sort(self):
		used={}
		res=[]
		for i in range(self.vertices):
			if i not in used:
				self.dfs(i,used,res)
		res.reverse()
		return res
	def dfs(self,v,used,res):
		used[v]=1
		for u in self.g[v]:
			if u not in used:
				self.dfs(u,used,res)
		res.append(v)
class TopoSortInGroup(object):
	def __init__(self, listVertices,graph,groupId,group):
		super(TopoSortInGroup, self).__init__()
		self.vertices=listVertices
		self.groupId=groupId
		self.g=graph
		self.group=group
		self.isCylicAns=False
	def Sort(self):
		used={}
		res=[]
		for i in self.vertices:
			if i not in used:
				self.dfs(i,used,res)
		res.reverse()
		return res
	def dfs(self,v,used,res):
		used[v]=1
		for u in self.g[v]:
			if u not in used and self.group[u]==self.groupId:
				self.dfs(u,used,res)
		res.append(v)
	def isCylic(self):
		used={}
		for i in self.vertices:
			if i not in used:
				# print(used)
				self.dfsCyclic(i,used)
				if self.isCylicAns==True:
					return True
		return False
	def dfsCyclic(self,v,used):
		used[v]=1
		for u in self.g[v]:
			if u in used and self.group[u]==self.groupId and used[u]==1:
				self.isCylicAns=True
				return
			elif u not in used and self.group[u]==self.groupId:
				self.dfsCyclic(u,used)
		used[v]=2
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
    	graph=[[]for i in range(n)]
    	idx_group=defaultdict(list)
    	graph_group=defaultdict(list)
    	for v in range(n):
    		for u in beforeItems[v]:
    			graph[u].append(v)
    	for i in range(n):
    		if group[i]==-1:
    			group[i]=m
    			idx_group[m].append(i)
    			m+=1
    		else:
    			idx_group[group[i]].append(i)
    	for idgroup in range(m):
    		for idtask in idx_group[idgroup]:
    			for neighbortask in graph[idtask]:
    				if group[neighbortask]!=idgroup:
    					graph_group[idgroup].append(group[neighbortask])
    	callCycleFinding = Cyclic(m,graph_group)
    	ans=[]
    	if callCycleFinding.isCylic() == False:
    		callTopo = TopoSort(m,graph_group)
    		topoGroup = callTopo.Sort()
    		for idgroup in topoGroup:
    			calTopoInsideGroup = TopoSortInGroup(idx_group[idgroup],graph,idgroup,group)
    			if calTopoInsideGroup.isCylic() == False:
    				ans.extend(calTopoInsideGroup.Sort())
    			else:
    				ans=[]
    				return ans
    	return ans
		
