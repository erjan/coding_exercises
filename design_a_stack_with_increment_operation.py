'''
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.main = list()
        self.size = 0
        self.maxSize = maxSize

    def __repr__(self) -> str:
        print()
        print()
        return "-".join(str(el) for el in self.main)

    def push(self, x: int) -> None:
        print('pushing')
        if self.size < self.maxSize:
            print('adding to top - still have space')
            self.main.append(x)
            self.size += 1
            print('size is %d' % self.size)
        print()

    def pop(self) -> int:
        print('popping..')
        if self.size == 0:
            print('empty stack')
            return -1

        res = self.main.pop()
        self.size = self.size-1
        print()
        return res

    def increment(self, k: int, val: int) -> None:
        if self.size < k:
            for i in range(len(self.main)):
                self.main[i] = self.main[i] + val
        else:
            for i in range(k):
                self.main[i] = self.main[i] + val
                
----------------------------------------------------------------------------------------------
# sol-n using 2 stacks(lists)

def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
            
-------------------------------------------------------------------------------------------
class Entry:
    def __init__(self, value, offset ):
        
        self.value = value
        self.offset = offset

        
    def __repr__(self):
        # override __repr__ to help programmer trace and debug
        msg = [ f'value = {self.value}', f'offset = {self.offset}', '---']
        return '\n'.join( msg )
        
        
        
class CustomStack:

    def __init__(self, maxSize: int):
        
        self.stk = []
        self.size_limit = maxSize

        
        
    def push(self, x: int) -> None:

        
        if len(self.stk) < self.size_limit:
            
            # push new element when stack size is within limit
            self.stk.append( Entry( value = x, offset = 0) )


        
    def pop(self) -> int:
        
        if self.stk:
            
            # fetch and pop top element from stack
            top_element = self.stk.pop()
            
            if self.stk:
                # If stack is still non-empty, 
                # propagate increment offset to lower level
                self.stk[-1].offset += top_element.offset
            

            # compute result with increment offset
            return top_element.value + top_element.offset
        
        else:
            
            # stack is empty, directly return -1
            return -1

        
        
    def increment(self, k: int, val: int) -> None:
        

        if self.stk:
            
            # update offset at k-th element when stack is non-empty
            
            # adjust k if k is over stack size
            k = min( k, len(self.stk) )
            
            self.stk[k-1].offset += val
        
