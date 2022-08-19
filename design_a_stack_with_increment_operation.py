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
