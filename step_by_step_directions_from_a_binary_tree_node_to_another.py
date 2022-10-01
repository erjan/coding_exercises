'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
'''

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def buildAdjacencyList(node):
            if not node:
                return
            
            if node.left:
                adj[node.val].append((node.left.val, 'L'))
                adj[node.left.val].append((node.val, 'U'))
                buildAdjacencyList(node.left)
                
            if node.right:
                adj[node.val].append((node.right.val, 'R'))            
                adj[node.right.val].append((node.val, 'U'))
                buildAdjacencyList(node.right)

                
        def findNode(value, prior, path):
            if value == destValue:
                return True
                
            for next_value, char in adj[value]:
                if next_value != prior:               
                    if findNode(next_value, value, path):
                        path.append(char)                        
                        return True
                
            return False
                    
        adj = defaultdict(list)            
        buildAdjacencyList(root)

        path = []
        findNode(startValue, -1, path)
        
        return "".join(reversed(path))
      
--------------------------------------------------------------------------------------
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        dq = deque([[root, ""]])
        sourceDirections = ""
        destDirections = ""
        while len(dq) > 0:
            curr = dq.popleft()
            if curr[0] is None:
                continue
            if curr[0].val == startValue:
                sourceDirections = curr[1]
            if curr[0].val == destValue:
                destDirections = curr[1]
            dq.append([curr[0].left, curr[1]+"L"])
            dq.append([curr[0].right, curr[1]+"R"])

        index = 0
        for i in range(min(len(sourceDirections), len(destDirections))):
            if sourceDirections[i] == destDirections[i]:
                index += 1
            else:
                break
        
        return (len(sourceDirections) - index) * "U" + destDirections[index:]
