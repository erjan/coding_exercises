'''
You are given a weighted tree consisting of n nodes numbered from 0 to n - 1.

The tree is rooted at node 0 and represented with a 2D array edges of size n where edges[i] = [pari, weighti] indicates that node pari is the parent of node i, and the edge between them has a weight equal to weighti. Since the root does not have a parent, you have edges[0] = [-1, -1].

Choose some edges from the tree such that no two chosen edges are adjacent and the sum of the weights of the chosen edges is maximized.

Return the maximum sum of the chosen edges.

Note:

You are allowed to not choose any edges in the tree, the sum of weights in this case will be 0.
Two edges Edge1 and Edge2 in the tree are adjacent if they have a common node.
In other words, they are adjacent if Edge1 connects nodes a and b and Edge2 connects nodes b and c.
'''




'''
Explanation
Intuition: For each node the max score out of it can be discussed in two situation
NE (neighbor edge) Score: One directly connected edge is picked
NNE (no neighbor edge) Score: No directly connected edge is picked
The max score out of a tree is the max(max(NE, NNE) for each node in the tree))
Since there is a recursive relation in the tree structure, we can leverage that and conduct the calculation with a top-down fashion
See more explanation in below comments
'''


class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        for i, (p, w) in enumerate(edges):            # build tree to a graph {node: [(child_node, branch_weight), ...]}
            d[p].append((i, w))
        res = 0
        def dfs(node):                                # return a tuple -> {max_score_if_picking_a_directly_connected_edge, max_score_without_picking_a_directly_connected_edge}
            nonlocal res
            if not d[node]:
                return 0, 0                           # handle special case
            child_scores = [] 
            mx_score_nne = 0                          # max score without picking a directly connected edge (mx_score_nne: max score no neighbor edge)
            for nei, w in d[node]:
                ne, nne = dfs(nei)                    # get score for each child
                mx = max(ne, nne)                     # when not picking any directly connected edge, the max score between two will be counted
                if mx > 0:
                    mx_score_nne += mx
                child_scores.append((ne, nne))
            mx_score_ne = 0                           # max score if picking a directly connected edge (mx_score_ne: max score neighbor edge)
            for i, (ne, nne) in enumerate(child_scores):                
                if d[node][i][1] <= 0:                # if a directley connected branch weight less than 0, ignore it
                    continue
                cur = mx_score_nne + d[node][i][1]    # taking one directly connected edge
                if ne > nne:                          # if ne > nne meaning `ne` was selected in previous calculation of `mx_score_nne`, thus we need to undo that effect by removing `ne` and adding `nne` if it's greater than 0
                    cur = cur - ne + max(nne, 0)      # so effectively, mx_score_ne = one_directly_connected_edge_weight + nne_for_corresponding_child_node + sum(max_ne_nne_of_all_other_child_nodes)
                mx_score_ne = max(mx_score_ne, cur)
            res = max(res, mx_score_nne, mx_score_ne) # update max score of this tree               
            return mx_score_ne, mx_score_nne          # return ne & nne as explained in "Intution" section
        dfs(0)                                       # Top-down starting from the root node
        return res
