'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.
'''

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
		# create the map 
        adj = collections.defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)

		# find the start num
        start = adjacentPairs[0][0]
        for k, v in adj.items():
            if len(v) ==1:
                start = k
                break
				
		# dfs to connect the graph
        nums=[]
        seen = set()
        def dfs(num):
            seen.add(num)
            for next_num in adj[num]:
                if next_num in seen: continue
                dfs(next_num)
            nums.append(num) 
        dfs(start)
        return nums
      
-------------------------------------------------------------------------------------
def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        for adj in adjacentPairs:
            d[adj[0]].append(adj[1])
            d[adj[1]].append(adj[0])
        
        def find_first(dic) -> int:
            for i in dic:
                if len(dic[i]) == 1:
                    return i
        
        first = find_first(d)
        res = [first]
        visited = {first}
        stack = [d[first]]
        while stack:
            cur = stack.pop()
            for adj in cur:
                if adj not in visited:
                    stack.append(d[adj])
                    visited.add(adj)
                    res.append(adj)
        return res
      
---------------------------------------------------------------------------------------------------------------
The key here is that the start or end of the array will only have 1 other element next to it. Therefore, create a graph/adjacency list to go from one element to the next (its neighbor) by using DFS. Inside our graph/adjacency list, each key element will have at most 2 element values (its neighbor before and after). We want to start DFS at a key element with 1 element associated (the start or end of the array doesn't matter as the array forwards/backwards is accepted).

Visited set to keep track of elements already added to our return array.
Standard DFS to explore neighbors.
Start DFS at key value of our graph/adjacency list where there is only 1 associated value.

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        visited = set()
        res = []
        
        for a, b in adjacentPairs:
            adjList[a].append(b)
            adjList[b].append(a)
            
        def dfs(element):
            visited.add(element)
            res.append(element)
            for nei in adjList[element]:
                if nei not in visited:
                    dfs(nei)
        
        for start in adjList.keys():
            if len(adjList[start]) == 1:
                dfs(start)
                break
        
        return res
