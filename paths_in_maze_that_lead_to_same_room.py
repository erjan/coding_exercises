'''
A maze consists of n rooms numbered from 1 to n, and some rooms are connected by corridors. You are given a 2D integer array corridors where corridors[i] = [room1i, room2i] indicates that there is a corridor connecting room1i and room2i, allowing a person in the maze to go from room1i to room2i and vice versa.

The designer of the maze wants to know how confusing the maze is. The confusion score of the maze is the number of different cycles of length 3.

For example, 1 → 2 → 3 → 1 is a cycle of length 3, but 1 → 2 → 3 → 4 and 1 → 2 → 3 → 2 → 1 are not.
Two cycles are considered to be different if one or more of the rooms visited in the first cycle is not in the second cycle.

Return the confusion score of the maze.

 
 '''


Solution 1 - Brute Force (TLE)

Explanation:

Iterate through each trio of nodes.
See if a cycle is formed by checking:
Does the secondNode connect to both the first and third node?
Does the third node connect to the first node, to complete the cycle?
Code:

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        neighbors = defaultdict(set)
        for source,target in corridors:
            neighbors[source].add(target)
            neighbors[target].add(source)
        
        ans = 0
        for firstNode in range(1,n+1):
            for secondNode in range(firstNode+1,n+1):
                for thirdNode in range(secondNode+1,n+1):
				
                    if secondNode in neighbors[firstNode] and \
						secondNode in neighbors[thirdNode] and \
                        thirdNode in neighbors[firstNode]:
                            ans += 1
                            
        return ans
Time Complexity: O(V^3)

Solution 2 - Intersection of Node Pairs (No TLE)

Explanation:

For each cycle, the last node must connect to the first.
Therefore if we have some connected pairing (FirstNode, ThirdNode), and there exists some kind of common node inbetween the two, we can route the cycle to go through that secondNode and extend the cycle length == 3.
Iterate through all direct pairings of nodes and try to find some common node inbetween the two. We can use set intersection for detecting commonalities.
Divide by 3 to prevent duplicate counting.
Code:

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        neighbors = defaultdict(set)
        for source, target in corridors:
            neighbors[source].add(target)
            neighbors[target].add(source)
            
        ans = 0
        for firstNode in range(1,n+1):
            for thirdNode in range(firstNode+1,n+1):
                if firstNode in neighbors[thirdNode]:
                    ans += len(neighbors[firstNode].intersection(neighbors[thirdNode]))
        return ans//3
Time Complexity: O(E * V^2)

Solution 3 - Greedy

Explanation:

Same idea as approach 2, but calculating the intersection on the fly.
Since we know any pair in corridors is directly connected, we can treat them the same way firstNode & thirdNode was in the previous approach.
No need to check for duplicates since there was no pre-processing.
Code:

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        ans = 0
        neighbors = defaultdict(set)
        for firstNode, thirdNode in corridors:
            neighbors[thirdNode].add(firstNode)
            neighbors[firstNode].add(thirdNode)
            ans += len(neighbors[firstNode].intersection(neighbors[thirdNode]))
        return ans
Time Complexity: O(V*E)
  
  -------------------------------------------------------------------------------------
  
  Since we only need to check cycle with length of 3, we can use nested loops instead of a DFS.
To avoid duplicated cycle, we only add edge from a smaller node to a larger node.
We check every triplet path as x->y->z, and then check if there is a direct edge x->z.

def numberOfPaths(n, corridors):
	g = collections.defaultdict(set)
	for x, y in corridors:
		g[min(x,y)].add(max(x,y))
	return sum(z in g[x] for x in range(1,n+1) for y in g[x] for z in g[y])

-----------------------------------------------------------------

The solution seems a bit slow(1796 ms // 36%); however, I think it is pretty intuitive to explain during the interview with fair time complexity. I have noticed that since the node is given from 1 to n-1, we can just iterate over the numbers and look up on the graph.
Most optimized solution I found is solution#3 in this link -> https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/discuss/1583945/Python-or-Set-Intersection-or-Brute-Force-greater-Most-Optimal by AlexSzeto.

Thought process

build undirected graph, so we can traverse from the source node
Everytime I visit new node and when to add its neighbor nodes to queue(stack doesnt matter for this case) for the DFS, I check if there is common node in current node's neighbors and current node's neighbor's neighbors. (graph[curr] vs graph[neigh])
If there is common node, that means the 3 nodes are cycled, therefore count is incremented
Return the count divided by 3, because we are counting redundantly for each nodes in a cycle.
Where E for edges and V for vertices
Time Complexity
Building graph is O(E) where E is number of edges. Then we do DFS traversal -> we are visiting every node once therefore O(V). And at each traversal, we are checking the intersection of neighbors -> O(min(S, L)) -> which can be O(V) and we check that for every edge at worst case so O(E)
Therefore, O(E) + O(V^2 * E) => O(V^2 * E)

Space Complexity
We are saving every node with every of edges into graph O(E + V). Visited set can be upto O(V). stack can also be up to O(V)
Therefore, O(E + V) + O(V) + O(V) => O(E + V)

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = defaultdict(set)
        count = 0
        stack = [1]
        visited = set()
        
		# building bidirectional graph
        for s, e in corridors:
            graph[s].add(e)
            graph[e].add(s)
		# BFS traversal
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for neigh in graph[curr]:
                if neigh not in visited:
                    stack.append(neigh)
					# graph[neigh] => neigh's neighbors // graph[curr] => current node's neighbors
                    tmpInter = graph[neigh].intersection(graph[curr])
					# number of intersected nodes can create length of three cycle
                    count += len(tmpInter)
        
		# divide by 3 because redundatnly counted from every vertices 
        return count // 3
    ----------------------------------------------------------------------------
    
    The key to avoid duplicate cycles (and visiting the same node again) is to traverse nodes in increasing order. That is, we only do [1, 2, 3] and never [2, 3, 1].

After we identify 3 nodes, we check if there is a connection between the first and last node to count it as a loop.

With this, we can write a DFS solution. However, since we only need to check triplets, three loops will do.

I tried a few container options for edges; adjacency list (backed by a hash set) was fastest for Python, and a boolean adjacency matrix - for C++.

Python 3

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        al, res = [set() for _ in range(n + 1)], 0
        for (p1, p2) in corridors:
            al[min(p1, p2)].add(max(p1, p2))
        for i in range(n + 1):
            for j in al[i]:
                for k in al[j]:
                    res += 1 if k in al[i] else 0
        return res
---------------------------------------------------------------------

Explanation
Avoid cycle by traversing only in order small -> medium -> large
You can avoid using set, by using the dictionary ans += 1 if nei_nei in graph[node] else 0
Implementation
class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        s = set()
        for r1, r2 in corridors:
            if r1 < r2:
                graph[r1].append(r2)
                s.add((r2, r1))
            else:    
                graph[r2].append(r1)
                s.add((r1, r2))
        ans = 0        
        for node in range(1, n+1):
            for nei in graph[node]:
                for nei_nei in graph[nei]:
                    ans += 1 if (nei_nei, node) in s else 0
        return ans
      

      
    

  
