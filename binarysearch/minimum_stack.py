'''
Implement a stack with the following methods:

MinimumStack() constructs a new instance of a minimum stack
append(int val) appends val to the stack
peek() retrieves the last element in the stack
min() retrieves the minimum value in the stack
pop() pops and returns the last element in the stack
Each method should be done in \mathcal{O}(1)O(1) time. You can assume that for peek, min and pop, the stack is non-empty when they are called.
'''


class MinimumStack:
    def __init__(self):
        self.main = []
        self.mintracker = []
        

    def append(self, val):
        self.main.append(val)
        if len(self.mintracker)>0 and val < self.mintracker[-1]:
            self.mintracker.append(val)
        elif len(self.mintracker)>0:
            top = self.mintracker[-1]
            self.mintracker.append(top)
        else:
            self.mintracker.append(val)

        

    def peek(self):
        return self.main[-1]
        

    def min(self):
        return self.mintracker[-1]
        

    def pop(self):
        top = self.main.pop()
        self.mintracker.pop()
        return top
      
---------------------------------------------------------------------------------------------------------
class MinimumStack:
    def __init__(self):
        self.stack, self.mins = [], [float("inf")]

    def append(self, val):
        self.stack.append(val)
        self.mins.append(min(val, self.mins[-1]))

    def peek(self):
        return self.stack[-1]

    def min(self):
        return self.mins[-1]

    def pop(self):
        self.mins.pop()
        return self.stack.pop()

      
        
