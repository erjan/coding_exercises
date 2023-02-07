'''
For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.

Implement the DataStream class:

DataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.
boolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and false otherwise. If there are less than k integers, the condition does not hold true, so returns false.
'''


class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.target = value
        self.n_cons = 0

    def consec(self, num: int) -> bool:
        if num == self.target:
            self.n_cons += 1
        else:
            self.n_cons = 0
        
        return self.n_cons >= self.k
        
-------------------------------------------------------------------
class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.memory = {}
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        self.stream.appendleft(num)
        self.memory[num] = self.memory.get(num, 0) + 1
        if len(self.stream) > self.k:
            last = self.stream.pop()
            self.memory[last] -= 1
        if self.memory.get(self.value, 0) == self.k:
            return True
        return False
