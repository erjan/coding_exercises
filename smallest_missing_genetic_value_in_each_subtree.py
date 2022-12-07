'''
There is a family tree rooted at 0 consisting of n nodes numbered 0 to n - 1. You are given a 0-indexed integer array parents, where parents[i] is the parent for node i. Since node 0 is the root, parents[0] == -1.

There are 105 genetic values, each represented by an integer in the inclusive range [1, 105]. You are given a 0-indexed integer array nums, where nums[i] is a distinct genetic value for node i.

Return an array ans of length n where ans[i] is the smallest genetic value that is missing from the subtree rooted at node i.

The subtree rooted at a node x contains node x and all of its descendant nodes.
'''


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        ans = [1] * len(parents)
        if 1 in nums: 
            tree = {}
            for i, x in enumerate(parents): 
                tree.setdefault(x, []).append(i)
                
            k = nums.index(1)
            val = 1
            seen = set()
            
            while k != -1: 
                stack = [k]
                while stack: 
                    x = stack.pop()
                    seen.add(nums[x])
                    for xx in tree.get(x, []): 
                        if nums[xx] not in seen: 
                            stack.append(xx)
                            seen.add(nums[xx])
                while val in seen: val += 1
                ans[k] = val
                k = parents[k]
        return ans 
