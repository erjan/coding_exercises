'''
There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.

'''

'''
Explanation
Intuition: Maximum product of 3 branches, need to know how many nodes in each branch, use DFS to start with
Build graph
Find left, right, up (number of nodes) for each node
left: use recursion
right: use recursion
up: n - 1 - left - right
Calculate score store in a dictinary
Return count of max key
Time: O(n)
Implementation
'''

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = collections.defaultdict(list)
        for node, parent in enumerate(parents):  # build graph
            graph[parent].append(node)
        n = len(parents)                         # total number of nodes
        d = collections.Counter()
        def count_nodes(node):                   # number of children node + self
            p, s = 1, 0                          # p: product, s: sum
            for child in graph[node]:            # for each child (only 2 at maximum)
                res = count_nodes(child)         # get its nodes count
                p *= res                         # take the product
                s += res                         # take the sum
            p *= max(1, n - 1 - s)               # times up-branch (number of nodes other than left, right children ans itself)
            d[p] += 1                            # count the product
            return s + 1                         # return number of children node + 1 (self)
        count_nodes(0)                           # starting from root (0)
        return d[max(d.keys())]                  # return max count
    
-----------------------------------------------------------------------------------------
'''
for each node, when we remove it, we have the following parts:

child subtree if any
parent subtree if any
we use dfs to count the number of node in each child subtree (no.1) and calculate the number of 
node in the parent subtree by N - sum(child_subtree) - 1(node itself). We use memo to aovid duplicated calculation in dfs.
'''

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = collections.defaultdict(list)
        for i, par in enumerate(parents):
            children[par].append(i)

        @lru_cache(None)
        def dfs(root):
            count = 1
            for child in children[root]:
                count += dfs(child)
            return count

        N = len(parents)
        max_score = 0
        score_counter = collections.defaultdict(int)

        for root in range(N):
            child = children[root]
            _sum = 0
            score = 1

            # score of the child tree
            for c in child:
                count = dfs(c)
                score *= count
                _sum += count

            curr_score = score * max(1, N-_sum-1) # score of the parent subtree
            score_counter[curr_score] += 1
            max_score = max(max_score, curr_score)

        return score_counter[max_score]
