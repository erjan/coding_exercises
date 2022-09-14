'''
There is an undirected graph with n nodes, numbered from 0 to n - 1.

You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A node sequence is valid if it meets the following conditions:

There is an edge connecting every pair of adjacent nodes in the sequence.
No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.

Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.
'''

Intuition
We don't need to check all possible sequences,
but only some big nodes.


Explanation
For each edge (i, j) in edges,
we find a neighbour ii of node i,
we find a neighbour jj of node i,
If ii, i, j,jj has no duplicate, then that's a valid sequence.

Ad the intuition mentioned,
we don't have to enumearte all neignbours,
but only some nodes with big value.

But how many is enough?
I'll say 3.
For example, we have ii, i, j now,
we can enumerate 3 of node j biggest neighbour,
there must be at least one node different node ii and node i.

So we need to iterate all edges (i, j),
for each node we keep at most 3 biggest neighbour, which this can be done in O(3) or O(log3).


  def maximumScore(self, A, edges):
        n = len(A)
        G = [[] for i in range(n)]
        for i,j in edges:
            G[i].append([A[j], j])
            G[j].append([A[i], i])
        for i in range(n):
            G[i] = nlargest(3, G[i])
            
        res = -1
        for i,j  in edges:
            for vii, ii in G[i]:
                for vjj, jj in G[j]:
                    if ii != jj and ii != j and j != ii:
                        res = max(res, vii + vjj + A[i] + A[j])
        return res
      
------------------------------------------------------------------------
# defaultdict is the same as Python's usual dictionary, but if an
# element doesn't exist, you can give it a default value to initialize with. 
from collections import defaultdict
# nlargest(n, l) - returns the n largest values of collection l.
from heapq import nlargest
# "product" is a function that takes two collections and 
# returns every pair between them.
# product("ab", "cd") = [(a, c), (a, d), (b, c), (b, d)].
from itertools import product

Let V be the number of nodes and E = len(edges).
# Time complexity: O(V + E) - we iterate through every vertex 
#                  and every edge a constant number of times.
# Space complexity: O(V) - we save a constant 
#                   number of neighbors (3) for every node.
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        # Turn the edge list into an adjacency graph.
        m = defaultdict(list)
        for u, v in edges:
            m[u].append((scores[v], v)) 
            m[v].append((scores[u], u))
        
        # Cut down all neighbors of each node to the three
        # that have the highest value.
        for u in m:
            m[u] = nlargest(3, m[u])

        ret = -1
        # Consider each edge to potentially be (B, C) for a quadruplet.
        for b, c in edges:
            # For every possible A and D in the neighbors of B and C...
            for (aWeight, a), (dWeight, d) in product(m[b], m[c]):
                # ... If we have no redundant nodes, it's a quadruplet.
                # Since it's the highest value quadruplet we could
                # possibly make with B and C, this solution is always accurate.
                if a not in [b, c] and d not in [b, c] and a != d:
                    ret = max(ret, scores[b] + scores[c] + aWeight + dWeight)
                    
        return ret
