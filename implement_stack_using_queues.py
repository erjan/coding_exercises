'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
'''

#using deque - my own solution
from collections import deque

class MyStack:

    def __init__(self):
        self.d = deque()
     
    def push(self, x: int) -> None:
        self.d.append(x)
        

    def pop(self) -> int:
        return self.d.pop()


    def top(self) -> int:
        if len(self.d) > 0:
            return self.d[-1]

    def empty(self) -> bool:
        return len(self.d) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


#another solution from discussions

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = collections.deque([])

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

        self.stack.popleft()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0
    
# proper solution using 2 queues
class MyStack:
    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def push(self, x: int) -> None:
        self.queue2.append(x)
        for _ in range(len(self.queue1)-1):
            self.queue2.append(self.queue1.pop(0)) 
        self.queue1 = self.queue2

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        if(self.queue1==[]):
            return True
        return False

    
#1 queue

class MyStack:
    def __init__(self):
        self.queue = []
    def push(self, x: int) -> None:
        length = len(self.queue)
        self.queue.append(x)
        for i in range(length):
            y = self.queue.pop(0)
            self.queue.append(y)
    def pop(self) -> int:
        return self.queue.pop(0)
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return not self.queue
