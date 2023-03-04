'''
Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Alice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:

Chooses two distinct integers u and v such that there exists an edge [u, v] in the tree.
He tells Alice that u is the parent of v in the tree.
Bob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.

Alice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.

Given the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.
'''

Intuition
let n = len(edges)
and # of correct witrh guesses is fixed if we explore from i->j (since it's a tree, which means there always only one path between nodes)

thus we will only have 2n possible values (i->j, j<-i)

and finally let we set each i as root, check how many root align with guesses >= k

Approach
Complexity
Time complexity:
O(n)

Space complexity:
O(n)

Code
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # n memory
        # build graph
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        gt = set((i, j) for i, j in guesses)

        # dfs traverse from parent -> i
        @cache
        def get_correct_pairs(i, parent):
            next_nodes = graph[i]
            n_correct = 0
            for next_node in next_nodes:
                if next_node == parent:
                    continue
                if (i, next_node) in gt:
                    n_correct += 1
                n_correct += get_correct_pairs(next_node, i)
            return n_correct
        
        ans = 0
        for i in graph:
            if get_correct_pairs(i, None) >= k:
                ans += 1
        return ans
