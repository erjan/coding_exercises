'''
You are given a list of strings ops where each element is either:

A non-negative integer that should be pushed into a stack
"POP" meaning pop the top element in the stack
"DUP" meaning duplicate the top element in the stack
"+" meaning pop the top two and push the sum
"-" meaning pop the top two and push top - second
Return the top element in the stack after applying all operations. If there are any invalid operations, return -1.
'''



class Solution:
    def solve(self, ops):

        stack = list()

        for op in ops:

            if op == 'POP':
                if len(stack) != 0:
                    stack.pop()
                else:
                    return -1
            
            elif op == 'DUP':
                if len(stack)!= 0:
                    top = stack[-1]
                    stack.append(top)
                else:
                    return -1
            
            elif op == '+':
                if len(stack) >= 2:
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    stack.append(t1+t2)
                else:
                    return -1

            elif op == '-':
                if len(stack) >= 2:
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    stack.append(t1 - t2)
                else:
                    return -1
            else:
                stack.append(op)
        if len(stack)> 0:                    
            return int(stack[-1])
        else:
            return -1
            
