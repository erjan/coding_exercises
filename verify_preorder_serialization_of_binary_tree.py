'''
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorderList = preorder.split(',')
        if len(preorderList)%2 != 1:
            return False
        stack = []
        for node in preorderList:
            stack.append(node)
            while len(stack) >= 3 and stack[-2] == stack[-1] == '#' and stack[-3] != '#':
                for i in range(3):
                    stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'
