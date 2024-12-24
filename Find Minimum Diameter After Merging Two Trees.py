'''
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.
'''

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1)+1
        m = len(edges2)+1

    
        adj1 = self.buildAdjList(n,edges1)
        adj2 = self.buildAdjList(m,edges2)

        d1 = self.find_diameter(n,adj1)
        d2 = self.find_diameter(m,adj2)
        comb = ceil(d1/2) + ceil(d2/2)+1
        return max(comb, d1,d2)

    def buildAdjList(self,n,e):

        graph = defaultdict(list)
        for a,b in e:
            graph[a].append(b)
            graph[b].append(a)
        return graph

        
    def find_diameter(self,n,adj):
        farthest_node,_ = self.find_farthest_node(n,adj,0)
        _,diameter = self.find_farthest_node(n,adj,farthest_node)
        return diameter

    def find_farthest_node(self,n,adj,source_node):
        q = deque([source_node])
        visited = [False]*n
        visited[source_node] = True
        maxd = 0
        farthest_node =source_node
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                farthest_node = cur
                for n in adj[cur]:
                    if not visited[n]:
                        visited[n]=True
                        q.append(n)
            if q:
                maxd+=1
        return farthest_node,maxd
