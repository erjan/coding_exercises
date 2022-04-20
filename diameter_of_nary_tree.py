'''
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

 
 '''


class Solution:
    def diameter(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
        
            max_depth = 0
            for child in node.children:
                depth = 1 + dfs(child)
                self.diameter = max(self.diameter, depth + max_depth)
                max_depth = max(max_depth, depth)
    
            return max_depth
        
        self.diameter = 0
        dfs(root)
        
        return self.diameter
      
------------------------------------------

The heap is used to track 2 maximum height from all subtrees.
since the size of the heap is restricted to 2, therefore insertions and deletions to the heap are O(log2) = O(1)

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        self.helper(root)
        return self.res
    
    def helper(self, root):
        heap = []
        for child in root.children:
            h = self.helper(child)
            heappush(heap, h)
            if len(heap) > 2:
                heappop(heap)
                
        h1 = heappop(heap) if heap else 0
        h2 = heappop(heap) if heap else 0
        self.res = max(self.res, h1 + h2)
        return 1 + max(h1, h2)
-----------------------------------------
It can be further improved by not sorting but only keep track of the largest and the second largest depth. But I prefer simpler code.

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root or not root.children:
                return 0
            depths = sorted((d+1 for d in map(dfs, root.children)), reverse=True) + [0]
            ans = max(ans, sum(depths[:2]))
            return depths[0]
        dfs(root)
        return ans
------------------------------------------------

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res = 0
        def dfs(node):
            nonlocal res
            if not node or not node.children:
                return 0
            child_depth = [0]
            d1 = 0
            d2 = 0
            for child in node.children:
                d = dfs(child)+1
				#to find first and second maximum depths out of all children
                if d1<=d:
                    d2 = d1
                    d1 = d
                elif d2<d:
                    d2 = d
            res = max(res,d1+d2)
            return d1
       
        dfs(root)
        return res
----------------------------------------
def diameter(self, root: 'Node') -> int:
        def height(root):
            heights = heapq.nlargest(2, (height(c) for c in root.children))
            self.ans = max(self.ans, len(heights) + sum(heights))
            return max(heights or [-1]) + 1
        
        self.ans = 0
        if root:
            height(root)
        return self.ans
      
      
      
