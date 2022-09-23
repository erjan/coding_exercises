class Codec:

    def serialize(self, root: TreeNode) -> str:
        def process(node: TreeNode):
            if not node:
                return
            numbers.append(node.val)
            process(node.left)
            process(node.right)
            
        numbers = []
        process(root);
        answer = ""
        for num in numbers:
            if answer:
                answer += " "
            answer += str(num)
        print(answer)
        return answer
        

    def deserialize(self, data: str) -> TreeNode:
        def create(sortedNumbers: List[int], numbers: List[int]) -> TreeNode:
            assert len(numbers) == len(sortedNumbers)
            if not numbers:
                return None
            
            val = numbers[0]
            valIndex = bisect_left(sortedNumbers, val)
            
            left = create(sortedNumbers[:valIndex], numbers[1:valIndex + 1])
            right = create(sortedNumbers[valIndex + 1:], numbers[valIndex + 1:])
            
            return TreeNode(val, left, right)
            
        numbers = [int(number) for number in data.split()]
        sortedNumbers = sorted(numbers)
        return create(sortedNumbers, numbers)
      
-----------------------------------------------------------------------------------------------
from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        # record of preorder traversal path
        path_of_preorder = []
        
        # Generate pre-order traversal path of binary search tree
        def helper( node ):
            
            if node:
                path_of_preorder.append( node.val )
                helper( node.left )
                helper( node.right )
        
        # ---------------------------------------------
        helper( root )
        # output as string, each node is separated by '#'
        return '#'.join( map(str, path_of_preorder) )
                
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            # corner case handle for empty tree
            return None
        
        # convert input string into doubly linked list of integer type, each node is separated by '#'
        node_values = deque(  int(value) for value in data.split('#') )
        
        # Reconstruct binary search tree by pre-order traversal
        def helper( lower_bound, upper_bound):
            
            if node_values and lower_bound < node_values[0] < upper_bound:
                
                root_value = node_values.popleft()
                root_node = TreeNode( root_value )
                
                root_node.left = helper( lower_bound, root_value )
                root_node.right = helper( root_value, upper_bound )
                
                return root_node
        
        # ---------------------------------------------
        
        return helper( float('-inf'), float('inf'))    
