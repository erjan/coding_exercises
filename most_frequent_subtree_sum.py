'''
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).
'''


from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        def subtree_freqs(node, curr_sum=0, freqs=defaultdict(int)):
                    if node is None:  # this is our base recursive case
                        return 0, freqs
                    curr_sum += subtree_freqs(node.left, curr_sum, freqs)[0] + \
                    subtree_freqs(node.right, curr_sum, freqs)[0]# because we are returning our values in a tuple, we use [0] to specify we want curr_sum
                    curr_sum += node.val
                    freqs[curr_sum] += 1
                    return curr_sum, freqs

        final_freqs = subtree_freqs(root)[1]
        max_val = max(final_freqs.values())
        maxis = [k for k, v in final_freqs.items() if v == max_val]
        return maxis

    
---------------------------------------------------------------------------
class Solution:
    # 48 ms, 99%
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        D = collections.defaultdict(int)
        # DFS recursively
		def cal_sum(node):
            if not node: return 0
            rv = node.val + cal_sum(node.left) + cal_sum(node.right)
            D[rv] += 1
            return rv
        
        cal_sum(root)
        mx = max(D.values())
        return [k for k, v in D.items() if v == mx] # return key if its val == max
