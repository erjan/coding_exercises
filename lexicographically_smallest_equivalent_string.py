'''
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
'''

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        
    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for i in range(len(s1)):
            uf.union(ord(s1[i])-ord('a'), ord(s2[i])-ord('a'))
        
        res = ""
        
        indexes = defaultdict(list)
        for i in range(len(uf.root)):
            if not indexes[uf.root[i]]:    
                indexes[uf.root[i]].append(i)
            
        for base in baseStr:
            root = uf.find(ord(base)-ord('a'))
            t = indexes[root]
            res += chr(t[0] + ord('a'))
            
        return res
            
-------------------------------------------------------


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        g = defaultdict(list)
        for a, b in zip(A, B):
            g[a].append(b)
            g[b].append(a)
            
        def findEquivalent(u):
            seen = set()
            least = 'z'
            def dfs(u):
                nonlocal least
                if u in seen:
                    return
                seen.add(u)
                least = min(least, u)
                for v in g[u]:
                    dfs(v)
            dfs(u) 
            return seen, least
        
        smallest = {}
        for c in A:
            if c in smallest:
                continue
            equiv, least = findEquivalent(c)
            for e in equiv:
                smallest[e] = least
        return ''.join(smallest[c] if c in smallest else c for c in S)   
      
        
--------------------------------------------------------------------------------------------------------
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        """
        Union Find (Disjoint Set)
        Complexities:
            Time: O(N), N - number of unqiue characters
            Space: O(N), N - number of unqiue characters, actually can be O(1) because number of eglish letters is 26 which is constant
        """
        
        parent = {char: char for char in string.ascii_lowercase}
        
        def _find(char: str) -> str:
            while parent[char] != char:
                char = parent[char]
                
            return char
        
        def _union(char1: str, char2: str) -> None:
            char1_set = _find(char1)
            char2_set = _find(char2)
            
            if char1_set != char2_set:
                if ord(char1_set) < ord(char2_set):
                    parent[char2_set] = char1_set
                else:
                    parent[char1_set] = char2_set
                
                
        for char1, char2 in zip(A, B):
            _union(char1, char2)
            
        return ''.join([_find(char) for char in S])
      
---------------------------------------------------------------------------------------------------
Here are similar problems (that are annotated) where you can try out this method:

Problem synonymous-sentences with a similar Solution
Problem the-earliest-moment-when-everyone-become-friends with a similar Solution

Hope this helps!

def smallestEquivalentString(self, A: str, B: str, S: str) -> str:

	group_id = 0
	char_id = {}
	group = {}

	for a,b in zip(A,B):

		if a in char_id and b in char_id:
			if char_id[a] == char_id[b]:
				continue
			elif char_id[a] < char_id[b]:
				group[char_id[a]] |= group[char_id[b]]
				obsolete_id = char_id[b]
				for char in group[char_id[b]]:
					char_id[char] = char_id[a]
				del group[obsolete_id]
			else:
				group[char_id[b]] |= group[char_id[a]]
				obsolete_id = char_id[a]
				for char in group[char_id[a]]:
					char_id[char] = char_id[b]
				del group[obsolete_id]

		elif a in char_id:
			group[char_id[a]] |= set([b])
			char_id[b] = char_id[a]

		elif b in char_id:
			group[char_id[b]] |= set([a])
			char_id[a] = char_id[b]

		else:
			group[group_id] = set([a,b])
			char_id[a] = group_id
			char_id[b] = group_id
			group_id += 1

	smallest_equivalent_char = {g : min(group[g]) for g in group}

	return ''.join(smallest_equivalent_char[char_id[char]] if (char in char_id) else char for char in S)
--------------------------------------------------------------------------------------------------------------------
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        def root(c):
            return c if parent[c] == c else root(parent[c])
        parent = {s: s for s in string.ascii_lowercase}
        for a, b in zip(A, B):
            p1, p2 = root(a), root(b)
            if p1 <= p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        return ''.join(root(s) for s in S)

      
        
