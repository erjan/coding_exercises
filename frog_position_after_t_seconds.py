'''
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted
'''


class Solution:
    def dfs(self, node, target, t, prob):
        self.visited.add(node)
        if t == 0:
            return prob if node == target else 0.0
        children = set()
        for v in self.graph[node]:
            if v not in self.visited:
                children.add(v)
        if not children:
            return prob if node == target else 0.0
        for v in children:
            p = self.dfs(v, target, t-1, prob / len(children))
            if p > 0:
                return p
        return 0.0
    
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        self.graph = defaultdict(set)
        for v, u in edges:
            self.graph[v].add(u)
            self.graph[u].add(v)
        self.visited = set()
        return self.dfs(1, target, t, 1.0)
            
-------------------------------------------------------------------------------------------
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        # connections
        self.conn = collections.defaultdict(list)
        
        # get the connections
        for edge in edges:
            self.conn[edge[0]].append(edge[1])
            self.conn[edge[1]].append(edge[0])
            
        # safe the probability
        self.prob = 0
        
        # make an array for the visited nodes
        # since these are only identified by
        # an increasing int, we can use an array
        # of bools
        self.visited = [False]*n
        self.visited[0] = True
        
        # make a dfs - during dfs we always will
        # add probability of path if we found a valid
        # one
        self.dfs(1, 1, t, target)
        
        return self.prob
        
    def dfs(self, current, prob, time, target):

        # if time is over we need to check
        # whether we are at the target
        # otherwise we just return
		# -> stop condition 3b
        if time == 0:
            if current == target:
                self.prob += prob
            return

        # get the current nodes we can visit
        visible = self.conn[current]

        # get the amount of nodes we can
        # visit and have not already visited
        amount = 0
        for node in visible:

            # guard clause if we visited the node
            if self.visited[node-1]:
                continue

            # increase the amount of nodes we can visit
            amount += 1

        # check whether we can visit any nodes
        if amount:
            
            # check whether we are at target and therefore target is out
			# stop condition 3c
            if current == target:
                return
            
            # calculate the updated probability and time
            updated_time = time-1
            updated_probability = prob*(1/amount)

            # go through all nodes we have not visited
            for node in visible:

                # guard clause to skip nodes we have visited
                if self.visited[node-1]:
                    continue

                # set the current node as visited
                self.visited[current-1] = True

                # traverse further and with updated values
                self.dfs(node, updated_probability, updated_time, target)

                # reset that we visited this node
                self.visited[current-1] = False

        # we can not visit any further nodes
		# stop condition 3a
        else:
            
            # check whether we are at target
            if current == target:
                self.prob += prob


        return
