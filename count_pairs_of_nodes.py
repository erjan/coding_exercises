'''
You are given an undirected graph defined by an integer n, the number of nodes, and a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

Let incident(a, b) be defined as the number of edges that are connected to either node a or b.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy both of the following conditions:

a < b
incident(a, b) > queries[j]
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

Note that there can be multiple edges between the same two nodes.
'''


Five steps:

For each node, accumulate the number of its edges in Nodes. Also, create a counter of ordered edges in Pairs.
Create a counter from Nodes. From the constraints, one can see that there probably will be many nodes with the same number of edges.
The ans counts the number of pairs with the given cnt. The cnt is defined in the problem description.
Iterate over pairs of elements in the counter of nodes, and increment the ans.
Finally, iterate over all Pairs counter and adjust the ans.
Output: accumulate ans from the end and, for each request, either output ans for request+1 or, if the request is too high, ouput 0.

Complexity: max of four values:

The number of nodes (length of Nodes).
The number of edges (length of ans, length of input edges).
Squared number of nodes with different number of edges (product of the counter with itself). Per @StarsThu2016 post, this part has complexity e (edges).
The number of queries.
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        
        Nodes={i:0 for i in range(1, n+1)}                              # Collect the number of in-/out-going edges for each of the nodes
        Pairs=defaultdict(int)                                          # Collect the number of edges connecting pairs of the nodes
        
        for u,v in edges:
            Nodes[u] += 1
            Nodes[v] += 1
            Pairs[(min(u,v), max(u,v))] += 1
        
        ans = [0] * (2*max(Nodes.values())+2)                           # Contains the number of pairs for given cnt
        counter=Counter(Nodes.values())                                 # Count nodes with the same number of edges
        
        for i, j in product(counter, counter):                          # Loop over all pairs of the number of edges from the nodes
            if i < j: ans[i+j] += counter[i] * counter[j]               # Update  ans for the pairs with i (one node) and j (another node) edges 
            if i == j: ans[i+j] += counter[i] * (counter[j]-1)//2       # Update ans if the number of edges in both nodes is the same and equals i=j

        for i, j in Pairs:                                              # Go over all the ordered edges
            ans[Nodes[i] + Nodes[j]] -= 1                               # Decrement ans for the separate nodes
            ans[Nodes[i] + Nodes[j] - Pairs[(i,j)]] += 1                # Increment ans if the edges between the nodes are accounted for
                
        for i in range(len(ans)-2, -1, -1): ans[i] += ans[i+1]          # Accumulate ans from the end
            
        return [ans[min(query+1, len(ans)-1)] for query in queries]
