'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

'''
#life hack: if required fast O(1) - need to create additional data stucture!
#TRADE OFF : TIME VS SPACE! 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        self.stack = []
        """
        self.stack = list()
        self.stack_min = list()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack_min) != 0:
            
            min_so_far = self.stack_min[-1]
            if x < min_so_far:
                self.stack_min.append(x)
            else:
                self.stack_min.append(min_so_far)
        else:
            self.stack_min.append(x)
        

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]


        

    def getMin(self) -> int:
        if len(self.stack_min)!= 0:
            
            print(self.stack_min[-1])
            return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
