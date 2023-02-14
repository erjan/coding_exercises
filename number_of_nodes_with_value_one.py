'''
There is an undirected connected tree with n nodes labeled from 1 to n and n - 1 edges. You are given the integer n. The parent node of a node with a label v is the node with the label floor (v / 2). The root of the tree is the node with the label 1.

For example, if n = 7, then the node with the label 3 has the node with the label floor(3 / 2) = 1 as its parent, and the node with the label 7 has the node with the label floor(7 / 2) = 3 as its parent.
You are also given an integer array queries. Initially, every node has a value 0 on it. For each query queries[i], you should flip all values in the subtree of the node with the label queries[i].

Return the total number of nodes with the value 1 after processing all the queries.

Note that:

Flipping the value of a node means that the node with the value 0 becomes 1 and vice versa.
floor(x) is equivalent to rounding x down to the nearest integer.
'''



class Solution:
    def numberOfNodes(self, n, queries):
        dict1, res = collections.defaultdict(list), []

        queries = [key for key,val in Counter(queries).items() if val%2 == 1]

        for i in range(2,n+1):
            dict1[i//2].append(i)

        def dfs(node):
            visited.add(node)

            for neighbor in dict1[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for i in queries:
            visited = set()
            dfs(i)
            res += list(visited)

        dict2 = collections.Counter(res)

        return len([key for key,val in dict2.items() if val%2 == 1])
