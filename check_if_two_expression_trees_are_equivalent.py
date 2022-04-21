'''
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the '+' operator (i.e. addition).

You are given the roots of two binary expression trees, root1 and root2. Return true if the two binary expression trees are equivalent. Otherwise, return false.

Two binary expression trees are equivalent if they evaluate to the same value regardless of what the variables are set to.

 
 '''

class Solution:
    
    def parse(self, node, counter):
        if node.val != '+':
            counter[node.val] += 1
        else:
            self.parse(node.left, counter)
            self.parse(node.right, counter)
        return counter
    
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        return self.parse(root1, Counter()) == self.parse(root2, Counter())
      
-----------------------------------------

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        freq = defaultdict(int)
        
        def fn(x, k): 
            if not x: return 
            freq[x.val] += k
            if freq[x.val] == 0: freq.pop(x.val)
            fn(x.left, k)
            fn(x.right, k)
                
        fn(root1, 1)
        fn(root2, -1)
        return not freq
-----------------------------------------------------

Explanation
Since + is the only sign, no need to worries about the order of addition
a + b + c == c + a + b
Simply count how many times a number appeared in the tree
In order traversal a tree
Use a dictionary to count node value freqeuncy for the first tree root1
Dis-count node value from the dictionary when doing in-order for the second tree root2
Return true if frequency for each node was back to 0, other wise return False
Meaning for any node n, the frequency of it in tree 1 == the frequency of it in tree 2
Time Complexity: O(2N) -> O(N)
Space Complexity: O(K), K is number of unique values len(set(N))
Implementation
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        c = collections.defaultdict(int)             # dictionary to count frequency
        def in_order(node, count=True):              # very standard iterative in-order traversal, with count/dis-count frequency toggled
            stack = []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left 
                node = stack.pop()
                if node.val != '+': c[node.val] = c[node.val] + (1 if count else -1)
                node = node.right      
        in_order(root1, True)                        # count frequency (increase)
        in_order(root2, False)                       # dis-count frequency (decrease)
        return all(val == 0 for _, val in c.items()) # check whether all values are 0
---------------------------------------

Idea

We can use a dictionary to keep track of each value.

When traverse the first tree, we do dic[node.val] += 1. And when traverse the second tree, we do dic[node.val] -= 1. If two trees are equivalent, all dic values should be 0 at the end.

This method extends nicely to the follow-up question. If there's a minus sign, we simply revert the increment value (sign) of the right child.


Complexity

Time complexity: O(N)
Space complexity: O(logN)


Python

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        
        dic = collections.Counter()
        
        def dfs(node, sign):
            if not node:
                return
            if node.val == '+':
                dfs(node.left, sign)
                dfs(node.right, sign)
            elif node.val == '-': # for follow-up
                dfs(node.left, sign)
                dfs(node.right, -sign)
            else:
                dic[node.val] += sign
        
        dfs(root1, 1)
        dfs(root2, -1)
        return all(x == 0 for x in dic.values())
-----------------------------------------------------------------------------------

class Solution:
    def evaluate(self, n: 'Node') -> int:
        if n.val == '+':
            return self.evaluate(n.left) + self.evaluate(n.right)
        else:
            return hash(n.val)
    
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        r1_val = self.evaluate(root1)
        r2_val = self.evaluate(root2)
        return r1_val == r2_val
      
      
      
