'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
'''

class MyQueue:

    def __init__(self):
        self.d = collections.deque()
        

    def push(self, x: int) -> None:
        self.d.appendleft(x)
        

    def pop(self) -> int:
        return self.d.pop()

    def peek(self) -> int:
        return self.d[-1]
        

    def empty(self) -> bool:
        return len(self.d) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
