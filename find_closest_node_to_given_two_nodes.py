'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.
'''

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        res = float("inf")
        
        def dfs(node, arr, counter=0):
            
			#making sure we haven't visited the node before (i.e., value in the array != -1)
            while arr[node]==-1 and node!=-1:
                
				#assigning how many moves it takes to reach node 
                arr[node] = counter
                next_node = edges[node]
			
				#going through each neighbor if exists and updating the counter 
                dfs(edges[node], arr, counter+1)

            return arr
        
		#find moves to reach nodes from node1
        n1 = [-1 for i in range(len(edges))]
        dfs(node1, n1)
		
		#find moves to reach nodes from node2
        n2 = [-1 for i in range(len(edges))]
        dfs(node2, n2)
                    
        answer = -1
        
        for i in range(len(edges)):
		
			#check if the end node is reachable from both starting nodes
            if n1[i]!=-1 and n2[i]!=-1:
                maximum_distance = max(n1[i], n2[i])
				
				#update the distance and the final answer if relevant
                if maximum_distance<res:
                    res = maximum_distance
                    answer = i
                
        return answer
		
