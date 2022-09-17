'''
You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.
'''

class SegmentTree:
    def __init__(self, max_value: int):
        self.max_value = 1
        while max_value > 0:
            max_value //= 2
            self.max_value *= 2
            
        self.count = [0] * (2*self.max_value)
        self.sum = [0] * (2*self.max_value)
        
    def _update(self, left: int, right: int, node: int, num: int, cnt: int) -> None:
        if left == right:
            self.count[node] += cnt
            self.sum[node] += cnt * num
            return
        
        middle = (left + right) // 2
        if num <= middle:
            self._update(left, middle, node*2, num, cnt)
        else:
            self._update(middle+1, right, node*2+1, num, cnt)
            
        self.count[node] = self.count[node*2] + self.count[node*2+1]
        self.sum[node] = self.sum[node*2] + self.sum[node*2+1]
        
    def add(self, num: int) -> None:
        self._update(left=1, right=self.max_value, node=1, num=num, cnt=1)
        
    def remove(self, num: int) -> None:
        self._update(left=1, right=self.max_value, node=1, num=num, cnt=-1)
        
    def _query(self, left: int, right: int, node: int, target: int) -> int:
        if left == right:
            return self.sum[node] // self.count[node] * target
        
        middle = (left + right) // 2
        if target <= self.count[node*2]:
            return self._query(left, middle, node*2, target)
        else:
            return self.sum[node*2] + self._query(middle+1, right, node*2+1, target-self.count[node*2])
        
    def query(self, target: int) -> int:
        if target == 0:
            return 0
        
        return self._query(left=1, right=self.max_value, node=1, target=target)

class MKAverage:

    def __init__(self, m: int, k: int):
        self.buffer_size = m
        self.offset = k
        self.buffer = collections.deque()
        self.tree = SegmentTree(100_000)

    def addElement(self, num: int) -> None:
        if len(self.buffer) == self.buffer_size:
            value = self.buffer.popleft()
            self.tree.remove(value)
            
        self.buffer.append(num)
        self.tree.add(num)

    def calculateMKAverage(self) -> int:
        if len(self.buffer) < self.buffer_size:
            return -1
        
        return (self.tree.query(self.buffer_size - self.offset) - self.tree.query(self.offset)) // (self.buffer_size - 2*self.offset)
      
----------------------------------------------------------------------------------------------------------------------------------------------
from sortedcontainers import SortedList

class MKAverage:

    MAX_NUM = 10 ** 5
    def __init__(self, m: int, k: int):
        
        self.m = m
        self.k = k
        
        # sorted list
        self.sl = SortedList([0] * m)
		# sum of k smallest elements
        self.sum_k = 0
		# sum of m - k smallest elements
        self.sum_m_k = 0
        
        # queue for the last M elements if the stream
        self.q = deque([0] * m)
        
    def addElement(self, num: int) -> None:
        # Time: O(logm)
		
        m, k, q, sl = self.m, self.k, self.q, self.sl            
            
        # update q
        q.append(num)
        old = q.popleft()
        
        # remove the old num
        r = sl.bisect_right(old)
		# maintain sum_k
        if r <= k:
            self.sum_k -= old
            self.sum_k += sl[k]
		# maintain sum_m_k
        if r <= m - k:
            self.sum_m_k -= old
            self.sum_m_k += sl[m-k]
        # remove the old num
        sl.remove(old)
        
        # add the new num
        r = sl.bisect_right(num)
        if r < k:
            self.sum_k -= sl[k-1]
            self.sum_k += num
        if r < m - k:
            self.sum_m_k -= sl[m - k - 1]
            self.sum_m_k += num
        
        sl.add(num)
            
        return

    def calculateMKAverage(self) -> int:
		# Time: O(1)
        if self.sl[0] == 0:
            return -1
        return (self.sum_m_k - self.sum_k) // (self.m - self.k * 2)
--------------------------------------------------------------------------------------
from sortedcontainers import SortedList
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.sl = SortedList()
        self.window = deque()
        self.sum = 0

    def addElement(self, num: int) -> None:
        if len(self.sl) < self.m:
            self.window.append(num)
            self.sl.add(num)
            if len(self.sl) == self.m:
                self.sum = sum(self.sl[self.k:-self.k])
        else:
            v = self.window.popleft()
            self.window.append(num)
            i = self.sl.bisect_left(v)
            j = self.sl.bisect_left(num)
            if 0<=i<self.k:
                if self.k < j:
                    self.sum -= self.sl[self.k]
                    if j <= self.m - self.k:
                        self.sum += num
                    else:
                        self.sum += self.sl[self.m-self.k]
            elif self.k <= i < self.m - self.k:
                self.sum -= v
                if 0<= j < self.k:
                    self.sum += self.sl[self.k-1]
                elif self.k <= j <= self.m-self.k:
                    self.sum += num
                else:
                    self.sum += self.sl[self.m-self.k]
            else:
                if j < self.m - self.k:
                    self.sum -= self.sl[self.m-self.k-1]
                    if self.k <= j:
                        self.sum += num
                    else:
                        self.sum += self.sl[self.k-1]
            self.sl.remove(v)
            self.sl.add(num)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        return self.sum//(self.m-2*self.k)
      
