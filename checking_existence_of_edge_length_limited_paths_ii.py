An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes, and the graph may not be connected.

Implement the DistanceLimitedPathsExist class:

DistanceLimitedPathsExist(int n, int[][] edgeList) Initializes the class with an undirected graph.
boolean query(int p, int q, int limit) Returns true if there exists a path from p to q such that each edge on the path has a distance strictly less than limit, and otherwise false.


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        self.edgeList = edgeList
        self.parent_nodes = {i: i for i in range(n)}
        self.rank_nodes = {i: 0 for i in range(n)}
        
        from heapq import heappop, heapify
        
        self.heap = [[w, u, v] for u, v, w in edgeList]
        self.weight_nodes = dict()
        self.weight_list = []
        heapify(self.heap)
        
        while self.heap:
            weight, node_u, node_v = heappop(self.heap)
            
            parent_node_u = self.find(node_u, self.parent_nodes)
            parent_node_v = self.find(node_v, self.parent_nodes)
            
            if parent_node_u != parent_node_v:
                if weight not in self.weight_nodes:
                    self.weight_list.append(weight)
                self.merge(parent_node_u, parent_node_v)
                self.weight_nodes[weight] = self.parent_nodes.copy()

        self.minimum_weight = min(self.weight_nodes)
    
    def merge(self, node_x, node_y):
        
        rank_x = self.rank_nodes[node_x]
        rank_y = self.rank_nodes[node_y]
        
        if rank_x < rank_y: 
            self.parent_nodes[node_x] = node_y
        elif rank_x > rank_y:
            self.parent_nodes[node_y] = node_x
        else:
            self.parent_nodes[node_x] = node_y
            self.rank_nodes[node_y] += 1
    
    def find(self, node, parent_nodes):
        if node != parent_nodes[node]:
            parent_nodes[node] = self.find(parent_nodes[node], parent_nodes)
        return parent_nodes[node]
    
    def query(self, p: int, q: int, limit: int) -> bool:
        
        if limit <= self.minimum_weight:
            return False
        
        from bisect import bisect_left
        
        weight = self.weight_list[bisect_left(self.weight_list, limit) - 1]
        if p not in self.weight_nodes[weight] or q not in self.weight_nodes[weight]:
            return False
        
        return self.find(p, self.weight_nodes[weight]) == self.find(q, self.weight_nodes[weight])
        
        
--------------------------------------------------------------------------------------------------------
Props to @OTTFF for the idea of using a snapshot array.

Approach:

Sort edges in ascending order according to the distance between nodes.
Add edges into a union-find data structure one at a time.
Every time the distance increases, take a snap shot of the current state
of the union-find data structure.
For each query, binary search to find the union-find data structure that
that only contains nodes connected by edges less than limit.
Check if nodes p and q are in the same network of nodes.
Side Note:

My implementation of union-find is a little different than most.
Questions are welcome, but whatever implementation you are
comfortable with should work fine in it's place.


class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
        self.u = Union_Find()
        self.edges = sorted(edgeList, key = lambda e: e[2])
        self.snaps = {}
        self.take_snapshots()
        self.distances = sorted(self.snaps)
        
    def take_snapshots(self):
        for i, (a, b, dist) in enumerate(self.edges):
            self.u.union(a, b)
            if (i == len(self.edges) - 1) or self.edges[i][2] != self.edges[i+1][2]:
                self.snaps[dist] = self.u.node_id.copy()

    def query(self, p: int, q: int, limit: int) -> bool:
        i = min(bisect.bisect_left(self.distances, limit-1), len(self.distances) - 1)
        if not self.distances or limit <= self.distances[0]:
            return False
        dist = self.distances[i]
        return self.snaps[dist].get(p, -1) == self.snaps[dist].get(q, -2)

class UnionFind:

    def __init__(self):
        self.group_id = 0
        self.groups = {}
        self.node_id = {}
    
    def union(self, a, b):
        '''There is an edge between node a and node b.  Update the groups of nodes to reflect this.'''
        A, B = a in self.node_id, b in self.node_id
        if A and B and self.node_id[a] != self.node_id[b]:
            self.merge(a, b)
        elif A or B:
            self.add(a, b)
        else:
            self.create(a, b)
    
    def merge(self, a, b):
        '''Node a and node b belong to different groups.  Merge the smaller group with the larger group.'''
        obs, targ = sorted((self.node_id[a], self.node_id[b]), key = lambda id: len(self.groups[id]))
        for node in self.groups[obs]:
            self.node_id[node] = targ
        self.groups[targ] |= self.groups[obs]
        del self.groups[obs]
        
    def add(self, a, b):
        '''One node a or b belongs to a group.  Add the new node to the existing group.'''
        a, b = (a, b) if a in self.node_id else (b, a)
        targ = self.node_id[a]
        self.node_id[b] = targ
        self.groups[targ] |= set([b])
    
    def create(self, a, b):
        '''Neither node a or node b belongs to a group.  Create a new group consisting of {a, b}.'''
        self.groups[self.group_id] = set([a,b])
        self.node_id[a] = self.node_id[b] = self.group_id
        self.group_id += 1
