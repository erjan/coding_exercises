'''
You are given a positive integer n representing the number of nodes in a tree, numbered from 0 to n - 1 (inclusive). You are also given a 2D integer array edges of length n - 1, where edges[i] = [node1i, node2i] denotes that there is a bidirectional edge connecting node1i and node2i in the tree.

You are given a 0-indexed integer array query of length m where query[i] = [starti, endi, nodei] means that for the ith query, you are tasked with finding the node on the path from starti to endi that is closest to nodei.

Return an integer array answer of length m, where answer[i] is the answer to the ith query.
'''



    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for a,b in edges:
            G[a].append(b)
            G[b].append(a)
        D = [[math.inf]*n for _ in range(n)]
        for a in range(n):
            que,D[a][a] = [a],0
            while que:
                tmp = []
                for q in que:
                    for b in G[q]:
                        if D[a][b]==math.inf:
                            D[a][b]=D[a][q]+1
                            tmp.append(b)
                que = tmp
        return [min(range(n), key=lambda x: D[x][a]+D[x][b]+D[x][q]) for a,b,q in query]
