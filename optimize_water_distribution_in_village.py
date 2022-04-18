'''
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.
'''


class UnionFind:
    def __init__(self, n: int):
        self._groups = [i for i in range(n)]
        
    def find(self, node: int) -> int:
        while node != self._groups[node]:
            node = self._groups[node]
        return node
    
    def union(self, node1: int, node2: int) -> bool:
        group1: int = self.find(node1)
        group2: int = self.find(node2)
        if group1 == group2:
            return False
        
        self._groups[group2] = group1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # 1. Add virtual node 0, connect all nodes to the virtual one, and set costs from wells
        for i, cost in enumerate(wells):
            pipes.append([0, i + 1, cost])
            
        # 2. Use Kruskal's Algorithm to solve Minimum Spanning Tree problem
        pipes.sort(key=lambda x: x[2])  # sort by cost
        
        uf = UnionFind(n + 1)
        total_cost: int = 0
        for pipe in pipes:
            if uf.union(pipe[0], pipe[1]):
                total_cost += pipe[2]
                
        return total_cost
      
----------------------------------------------------------------------------------------------------------------
[Basic Ideas]
1st.
Build all wells total = sum(wells).

2nd.
Build a pipe between i and j and destroy a well,
if pipe_ij < max(well_i, well_j).

[Implement Ideas]

Using Union-Find to remember connected houses.
Root of the Union has the cheapest well. (union by cost)
Look for a cheaper pipe first.
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        unions = list(range(n+1)); unions[0] = -1
        def find(i): # with zipping
            if unions[i] != i: unions[i] = find(unions[i])
            return unions[i]
        
        total = sum(wells)
        destroyed = set()
        for i, j, cost in sorted(pipes, key=lambda pipe: pipe[2]):
            dst, rsv = find(i), find(j)
            if dst == rsv: continue
            if dst in destroyed or (wells[dst-1] < wells[rsv-1] and rsv not in destroyed):
                dst, rsv = rsv, dst # not destroyed and max cost
            if dst in destroyed: continue
            
            if wells[dst-1] > cost: # build a pipe and destory well
                total += cost - wells[dst-1]
                destroyed.add(dst)
                unions[dst] = rsv # update destroyed's root as reserved
        return total
[Time Complexity]
n := number of houses n == n (parameter) == len(wells)
m := number of pipes m == len(pipes)

O(n) for total = sum(wells)
O(m log(m)) for sorted(pipes, key=lambda pipe: pipe[2])
O(m*a(n)) for loop

Thanks to zipping, find(i) is O(a(n)).
in operation to set is O(1)

So, time complexity is O(n + m log(m)).

[Space Complexity]
O(n) A list for representing union.
O(n) A set for remember destroyed wells.
O(m) Sort the pipes.
So, space complexity is O(n + m).

----------------------------------------------------------------------------------------
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False
        
        if self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] =  rootX
        elif self.rank[rootX] == self.rank[rootY]:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
            
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        unionfind = UnionFind(n+1)
        
        for i, well_weight in enumerate(wells):
            pipes.append([0, i+1, well_weight])
            
        pipes.sort(key = lambda x: x[2])
        total_cost = 0
        
        for i, (house_a, house_b, weight) in enumerate(pipes):
            if unionfind.union(house_a, house_b):
                total_cost += weight
        
        return total_cost
      
--------------------------------------------------------------------------------------------------------
At first, look in code for ''' ''' to get more in-depth view.

We start by traversing wells to create virtual vertex. Why? MST (minimum spanning tree) allows
us to get shortes path with undirected weighted edges. But well is a weight of vertex. Hence we're
to trick it in some way. Create additional vertex which has edges to all nodes. +1 in vertex here as
we start from 0 (index counting), but 0 is our self-made vertex and our count starts with 1.

Next, traverse pipes to get all verticies and their adjacent nodes. I.e. we get vertex1 and vertex2 from
every list in pipes and create 2 separate verticies that point to each other. Example:
{2: [(1,3)], 3: [(1,2)}

We need to keep track of explored nodes for being able to finish traversal. Also, we create Heap
with slight modification. As we use heap to pop() smallest cost vertex, we're to write
additional "feature". Simply speaking, adding ** [0]** when comparing indicies as our goal to have
smallest cost edge on the top: arr[idxOne][0] > arr[idxTwo][0]

We remove node with cost and vertex in the loop. To prevent self-loops we check whether we've
already visited such vertex. Then crucial part: we're not guaranteed with the fact that our vertex
may not be the dead end. If so, we just continue by popping next. If not, traverse it's neighbours and add to the heap.

Probable question(at least I had it at first): why do we need traversal at all? So, we have graph
where all verticies are dumped. We're to visit them all (our loop makes it a condition). But we need to
do it in minimun cost fashion. Hence Heap allows us to put with min. cost at the top.
When we start with 0 vertex, we pop one node with smallest cost that 0 leads to. If it does have
adjacent nodes -> traverse them as we're on the path to have smallest cost. If it is a dead lock, then
just switch to the next smallest vertex. And if vertex already in explored, then we does have water provided to it.

Important: when we take from 0 - means we build well, when we traverse adjacent from non-zero -> pipes

Hope you find helpful. Upvote, please!

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        '''
        In traditional MST we can't have weighted
        vertices, only edges. In our case we have pipes
        construction cost as edges and wells construction
        cost as verticies weights. Hence we're to remove
        weights from verticies to edges by creating 
        virtual edge.
        
        1. `adjacency list` to keep our graph
        2. `set` to keep our final MST and determine
        whether the vertex has been added
        3. Min Heap to determine min cost vertex
        '''
        graph = {0: []}
        
        for vertex in range(len(wells)):
            cost = wells[vertex]
            '''
            +1 because we want to simulate
            other vertices => they start from 1
            '''
            graph[0].append((cost, vertex + 1))
        
        for vertex1, vertex2, cost in pipes:
            if vertex1 not in graph:
                graph[vertex1] = []
            
            graph[vertex1].append((cost, vertex2))
            
            if vertex2 not in graph:
                graph[vertex2] = []
            
            graph[vertex2].append((cost, vertex1))
        
        explored = set([0])
        heap = MinHeap(graph[0])
        
        result = 0
        while len(explored) < n + 1:
            cost, next_vertex = heap.remove()
            if next_vertex not in explored:
                explored.add(next_vertex)
                result += cost
                if next_vertex not in graph:
                    continue
                else:
                    for new_cost, adjacent_vertex in graph[next_vertex]:
                        if adjacent_vertex not in explored:
                            heap.insert((new_cost, adjacent_vertex))
        
        return result

    
class MinHeap:
	def __init__(self, arr):
		self.heap = self.buildHeap(arr)
	
	def check(self):
		return len(self.heap) == 0
	
	def buildHeap(self, arr):
		parentIdx = (len(arr) - 2) // 2
		for i in reversed(range(parentIdx + 1)):
			self.siftDown(i, len(arr) - 1, arr)
		return arr
	
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		to_remove = self.heap[0]
		node = self.heap.pop()
		if len(self.heap) > 0:
			self.heap[0] = node
			self.siftDown(0, len(self.heap) - 1, self.heap)
		return to_remove
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp()
	
	def siftDown(self, idx, length, arr):
		idxOne = idx * 2 + 1
		while idxOne <= length:
			idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
			if idxTwo != -1 and arr[idxOne][0] > arr[idxTwo][0]:
				swap = idxTwo
			else:
				swap = idxOne
			
			if arr[swap][0] < arr[idx][0]:
				self.swapValues(swap, idx, arr)
				idx = swap
				idxOne = idx * 2 + 1
			else:
				return
	
	def swapValues(self, i, j, arr):
		arr[i], arr[j] = arr[j], arr[i]
	
	def siftUp(self):
		idx = len(self.heap) - 1
		while idx > 0:
			parentIdx = (idx - 1) // 2
			if self.heap[idx][0] < self.heap[parentIdx][0]:
				self.swapValues(idx, parentIdx, self.heap)
				idx = parentIdx
			else:
				return
                 
--------------------------------------------------------------------------------------
                 The fastest code I could achieve, some methods to speed up:

inspired by Union-Find & Kruskal algorithm;
use index 0 as the well, significant speed up;
optimize Union-Find, we want to decrease the depth of Union-Find path, let small path to join big path, significant speed up in theory (unfortunately test cases is weak, almost no speed up in fact);
let all path join the root 0 path, significant speed up;
DO NOT FORGET, use [1 for _ in range(n + 1)] instead of [1] * (n + 1)
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        def get_root(node):
            while roots[node] != node:
                node = roots[node]
            return node

        def join(n1, n2):
            r1, r2 = get_root(n1), get_root(n2)
            if r1 != r2:
                s1, s2 = sizes[r1], sizes[r2]
                if s1 < s2 or r2 == 0:
                    roots[r1] = r2
                    sizes[s2] += s1
                else:
                    roots[r2] = r1
                    sizes[s1] += s2
                return 1
            return 0

        roots = [i for i in range(n + 1)]
        sizes = [1 for _ in range(n + 1)]

        w = [(wells[i], i + 1, 0) for i in range(n)]
        w += [(c, i, j) for i, j, c in pipes]
        w.sort()

        res = 0
        for cost, c1, c2 in w:
            if join(c1, c2):
                res += cost
                n -= 1
                if n == 0:
                    return res
                 
                 
----------------------------------------------------------------------------------------------
                 class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # minimum spanning tree problem
        # create a well node as source, all villages are connected to it
        # we're trying to find a minimum spanning tree.
        # the tree is acyclic, otherwise we're wasting an edge
        # need to create weighted edge
        method = 'Kruskal' # 'Kruskal'
        
        if method == 'Prim':
        # Prim
        # If we use Prim's algorithm, we pick a minimum cost edge that is 
        # connected to the current tree (meaning currently we have a tree
        # so this new edge should have one and only one vertex in the
        # current set)
        # we also maintain a priority queue, everytime we add an edge, we
        # push all it's connecting edges into queue. next time we pop the min
        # from this queue, we check if it doesn't form cycle using the above method
        # start with min_e
            # preprocess
            edges = collections.defaultdict(set) # store u: {(cost, v),...}
            min_e = (float('inf'),[])
            for ind,w in enumerate(wells):
                # house number actually ind+1
                # wells is index 0
                edges[0].add((w,ind+1))
                edges[ind+1].add((w,0))
                if w < min_e[0]:
                    min_e = (w, [0,ind+1])

            for u,v,cost in pipes:
                edges[u].add((cost,v))
                edges[v].add((cost,u))
                if cost < min_e[0]:
                    min_e = (cost, [u,v])
            A = set(min_e[1])
            ans = min_e[0]
            pq = []
            for item in (edges[min_e[1][0]] | edges[min_e[1][1]]):
                heapq.heappush(pq, item)

            while len(A) < n+1:
                cost, new_v = heapq.heappop(pq)
                if new_v not in A:
                    ans += cost
                    A.add(new_v)
                    for cost, new_u in edges[new_v]:
                        if new_u not in A:
                            heapq.heappush(pq, (cost,new_u))
            return ans
        
        elif method == 'Kruskal':
        # Kruskal
        # If we use Kruskal, we need to design DSU (disjoint set union) 
        # to find to detect cycle since we could be forming a forest at early stage.
        # also use minheap to maintain
            edges = []
            for ind,w in enumerate(wells):
                # house number actually ind+1
                # wells is index 0
                edges.append((w,(0,ind+1)))
            heapq.heapify(edges)
            
            for u,v,cost in pipes:
                heapq.heappush(edges,(cost,(u,v)))
            
            parent = [0]*(n+1)
            
            # Use Disjoint Set Union to detect cycles
            def find(x):
                if parent[x] == 0:
                    return x
                parent[x] = find(parent[x])
                return parent[x]
            
            def union(x,y):
                parent_x, parent_y = find(x), find(y)
                if parent_x == parent_y:
                    return False
                parent[parent_x] = parent_y
                return True
            
            count = 0
            ans = 0
            # we have V = n+1 vertices, end computation at E = V-1=n
            while count < n:
                cost, (u, v) = heapq.heappop(edges)
                while not union(u,v):
                    cost, (u, v) = heapq.heappop(edges)
                count += 1
                ans += cost
            return ans
