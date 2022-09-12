'''
You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement of pairs.
'''

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        # in degree table for each node
        in_degree = defaultdict(int)
        
        # out degree table for each node
        out_degree = defaultdict(int)
        
        # adjacency matrix for each node
        adj_matrix = defaultdict(list)
        
        
        # update table with input edge pairs
        for src, dst in pairs:
            
            in_degree[dst] += 1
            out_degree[src] += 1
            adj_matrix[src].append(dst)
            
        
        ## Case_#1:
        # There is eular circuit in graph, any arbitrary node can be start point, here we use source node of first edge just for convenience
        start_node_idx = pairs[0][0]
        
        
        ## Case_#2
        # There is no eular circuit. But there is eular path, find the start node by indegree and outdegree relation
        for node in adj_matrix:
            
			# find the node whose outdegree is one more than indegree
            if out_degree[node] - in_degree[node] == 1:
                start_node_idx = node
                break
        
        # ------------------------------------------------
        def eular_path( adjMatrix, path, cur_node):
            
            # Keep traverse to next node in DFS until all edges of current node are visited
            while adjMatrix[cur_node]:
                
                # pop one edge and get next visit node
                next_visit_node = adjMatrix[cur_node].pop()
                
                eular_path( adjMatrix, path, next_visit_node )
                
                # post-order style
                # current explorer is finished, record current edge pair 
                path.append([cur_node, next_visit_node])
                
                
        # ------------------------------------------------
        record = []
        eular_path(adj_matrix, record, start_node_idx)
        
        # reversed of post-order record is the answer of eular path        
        return reversed(record)
-----------------------------------------------------------------------------------------------------------
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        pdict = collections.defaultdict(set)
        ans = list()
        visited = set()
        def zero():
            return 0
        diff = collections.defaultdict(zero)
        for i,j in pairs:
            diff[i] += 1
            diff[j] -= 1
            pdict[i].add(j)
        
        def findStartNode():
            full = list(diff.keys())
            for node in full:
                if diff[node] == 1:
                    return node
            return i
        def arrange(node):
            while len(pdict[node]) > 0:
                arrange(pdict[node].pop())
            ans.append(node)
        arrange(findStartNode())
        ans.reverse()
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]
