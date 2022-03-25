 #Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.   
  
  def one_pass(self, root):
        self.out = float('inf')
        self.prev = float('-inf')
        def rec(node):
            if node:
                rec(node.left)
                self.out = min(self.out, node.val - self.prev)
                self.prev = node.val
                rec(node.right)
            return float('inf')
        rec(root)
        return self.out
    
    def two_pass(self, root):
        arr = []
        def rec(node):
            if node:
                rec(node.left)
                arr.append(node.val)
                rec(node.right)
              
        rec(root)
        diff = float('inf')
        for i in range(1, len(arr)):
            diff = min(diff, arr[i] - arr[i-1])
        return diff
