'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
'''

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        status=[0]*(n)
        res=[]
        
        def dfs(i):# this function will check is there any loop, cycle and i is a part of that loop,cycle 
            if status[i]=="visited": #if this node is already visited, loop detected return true
                return True
            if status[i]=="safe": #if this node is previously visited and marked safe no need to repeat it ,return False no loop possible from it
                return False
            status[i]="visited" # so we have visited this node
            for j in graph[i]:
                if  dfs(j):# if loop detected return True
                    return True
            status[i]="safe" # if we reached till here means no loop detected from node i so this node is safe
            return False # no loop possible return false
       
    
        for i in range(n):
            if not dfs(i): #if no loop detected this node is safe 
                res.append(i)
        return res
