'''
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.
'''

class DinnerPlates:

    def __init__(self, capacity: int):
        self.size = capacity
        self.arr = []
        self.leftmost = []
        self.rightmost = []
        self.nonempty = set()
        self.presentInLeftmost = set()

    def push(self, val: int) -> None:
        if self.leftmost:
            top = self.leftmost[0]
            self.arr[top].append(val)
            if len(self.arr[top]) == self.size:
                self.presentInLeftmost.remove(top)
                heappop(self.leftmost)
            
            if top not in self.nonempty:
                self.nonempty.add(top)
                heappush(self.rightmost, -top)
            
        else:
            self.arr.append([val])
            curr = len(self.arr) - 1
            if len(self.arr[-1]) < self.size:
                self.presentInLeftmost.add(curr)
                heappush(self.leftmost, curr)
                
            heappush(self.rightmost, -curr)
            self.nonempty.add(curr)

    def pop(self) -> int:
        if not self.rightmost:
            return -1
        
        flag = 0
        while self.rightmost:
            top = -self.rightmost[0]
            if top in self.nonempty:
                flag = 1
                break
                
            heappop(self.rightmost)
            
        if flag == 0:
            return -1
        
        ans = self.arr[top].pop()
        if len(self.arr[top]) == 0:
            self.nonempty.remove(top)
            heappop(self.rightmost)
            
        if top not in self.presentInLeftmost:
            self.presentInLeftmost.add(top)
            heappush(self.leftmost, top)
            
        return ans

    def popAtStack(self, index: int) -> int:
        if index > len(self.arr) - 1 or len(self.arr[index]) == 0:
            return -1
        
        ans = self.arr[index].pop()
        if len(self.arr[index]) == 0:
            self.nonempty.remove(index)
        
        if index not in self.presentInLeftmost:
            self.presentInLeftmost.add(index)
            heappush(self.leftmost, index)
            
        return ans


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

-----------------------------------------------------------------------------------------------------------------------
class DinnerPlates:

    def __init__(self, capacity: int):
        self.cpty = capacity
        self.pq = [] # min heap of non-full stacks
        self.stacks = []

    def push(self, val: int) -> None:
        while self.pq: 
            k = heappop(self.pq)
            if k < len(self.stacks): break 
        else: 
            k = len(self.stacks)
            self.stacks.append([])
        self.stacks[k].append(val)
        if len(self.stacks[k]) < self.cpty: heappush(self.pq, k)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]: self.stacks.pop()
        if self.stacks: 
            if len(self.stacks[-1]) == self.cpty: heappush(self.pq, len(self.stacks)-1)
            return self.stacks[-1].pop()
        return -1 
        
    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]: return -1 
        if len(self.stacks[index]) == self.cpty: heappush(self.pq, index)
        return self.stacks[index].pop()
