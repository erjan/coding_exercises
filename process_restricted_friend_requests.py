'''
You are given an integer n indicating the number of people in a network. Each person is labeled from 0 to n - 1.

You are also given a 0-indexed 2D integer array restrictions, where restrictions[i] = [xi, yi] means that person xi and person yi cannot become friends, either directly or indirectly through other people.

Initially, no one is friends with each other. You are given a list of friend requests as a 0-indexed 2D integer array requests, where requests[j] = [uj, vj] is a friend request between person uj and person vj.

A friend request is successful if uj and vj can be friends. Each friend request is processed in the given order (i.e., requests[j] occurs before requests[j + 1]), and upon a successful request, uj and vj become direct friends for all future friend requests.

Return a boolean array result, where each result[j] is true if the jth friend request is successful or false if it is not.

Note: If uj and vj are already direct friends, the request is still successful.
'''


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:        
        result = [False for _ in requests]
        
        connected_components = [{i} for i in range(n)]
        
        connected_comp_dict = {}
        for i in range(n):
            connected_comp_dict[i] = i
        
        banned_by_comps = [set() for i in range(n)]
        for res in restrictions:
            banned_by_comps[res[0]].add(res[1])
            banned_by_comps[res[1]].add(res[0])
        for i,r in enumerate(requests):
            n1, n2 = r[0], r[1]
            c1, c2 = connected_comp_dict[n1], connected_comp_dict[n2]
            if c1 == c2:
                result[i] = True
            else:
                if not (connected_components[c1].intersection(banned_by_comps[c2]) or connected_components[c2].intersection(banned_by_comps[c1])):
                    connected_components[c1].update(connected_components[c2])
                    banned_by_comps[c1].update(banned_by_comps[c2])
                    for node in connected_components[c2]:
                        connected_comp_dict[node] = c1
                    result[i] = True
                
        return result
        
----------------------------------------------------------------------------------------------------
class UnionFind:

	def __init__(self, n: int):
		self.parent = list(range(n))
		self.rank = [1] * n

	def find(self, p: int, halving: bool=True) -> int:
		if p != self.parent[p]:
			self.parent[p] = self.find(self.parent[p]) 
		return self.parent[p]

	def union(self, p: int, q: int) -> bool:
		prt, qrt = self.find(p), self.find(q)
		if prt == qrt: return False 
		if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt 
		self.parent[prt] = qrt
		self.rank[qrt] += self.rank[prt]
		return True


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ans = []
        uf = UnionFind(n)
        for u, v in requests: 
            uu = uf.find(u)
            vv = uf.find(v)
            for x, y in restrictions: 
                xx = uf.find(x)
                yy = uf.find(y)
                if uu == xx and vv == yy or uu == yy and vv == xx: 
                    ans.append(False)
                    break 
            else: 
                ans.append(True)
                uf.union(u, v)
        return ans 
