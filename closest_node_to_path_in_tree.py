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
-------------------------------------------------------------------------------------------------
class Solution:
    def closestNode(self, n, edges, query):
        dict1 = collections.defaultdict(list)

        for i,j in edges:
            dict1[i].append(j)
            dict1[j].append(i)

        def dfs(start,end):
            if start == end:
                return True

            visited.add(start)

            for neighbor in dict1[start]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    if dfs(neighbor,end):
                        return True
                    stack.remove(neighbor)


        def bfs(ans,path):
            visited = set()

            visited.add(ans[0])

            while ans:
                node = ans.pop(0)

                if node in path:
                    return node

                for neighbor in dict1[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        ans.append(neighbor)

        result = []

        for i in query:
            visited = set()
            stack = [i[0]]
            dfs(i[0],i[1])

            if i[2] in stack:
                result.append(i[2])
                continue

            result.append(bfs([i[2]],stack))

        return result
