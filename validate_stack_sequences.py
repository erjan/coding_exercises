'''
Given two integer arrays pushed and popped each with 
distinct values, return true if this could have been the result of 
a sequence of push and pop operations on an initially empty stack, or false otherwise.
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        for num in pushed:
            stack.append(num)

            while len(stack) > 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
                
        if len(stack) == 0:
            return True
        else:
            return False
