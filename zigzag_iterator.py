'''
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.
 

Example 1:

Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
Example 2:

Input: v1 = [1], v2 = []
Output: [1]
Example 3:

Input: v1 = [], v2 = [1]
Output: [1]

'''

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        from itertools import zip_longest, chain, filterfalse
        self.zigzag = filterfalse(lambda x: x is None, chain.from_iterable(zip_longest(v1, v2)))
		# alterly use pure list comprehension
		# self.zigzag = (v for k1, k2 in zip_longest(v1, v2) for v in (k1, k2) if v is not None)
        self.n = len(v1) + len(v2)

    def next(self) -> int:
        self.n -= 1
        return next(self.zigzag)

    def hasNext(self) -> bool:
        return self.n > 0
-------------------------------------------

class ZigzagIterator:

def __init__(self, v1: List[int], v2: List[int]):
    v1.reverse()
    v2.reverse()
    self.res = collections.deque()
    while v1 and v2:
        self.res.append(v1.pop())
        self.res.append(v2.pop())
    while v1:
        self.res.append(v1.pop())
    while v2:
        self.res.append(v2.pop())

def next(self) -> int:
    return self.res.popleft()
    

def hasNext(self) -> bool:
    if self.res:
        return True
    return False
---------------------------------------------

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
		# initialize the list to be processed next
        if self.v1:
            self.queue = [ (self.v1, 'v1')]
        else:
            self.queue = [ (self.v2, 'v2')]

    def next(self) -> int:
        list_to_pop, label = self.queue.pop()
        rtn = list_to_pop.pop(0)
		
		# decide which list to be added back to the queue for next process
        if label == 'v1':
            if self.v2:
                self.queue.append((self.v2, 'v2'))
            else:
                self.queue.append((self.v1, 'v1'))
        else:
            if self.v1:
                self.queue.append((self.v1, 'v1'))
            else:
                self.queue.append((self.v2, 'v2'))
                
        return rtn
		
    def hasNext(self) -> bool:
        if self.v1 or self.v2:
            return True
        else:
            return False
-----------------------------------------------------------

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.idx1 = 0 
        self.idx2 = 0
        self.turn = 0 # or 1 

    def hasNext(self) -> int:
        return  self.idx1 < len(self.v1) or self.idx2 < len(self.v2)
            

    def next(self) -> bool:
        if self.idx1 < len(self.v1) and self.idx2 < len(self.v2):
            if self.turn == 0:
                self.idx1 += 1
                self.turn = 1- self.turn
                return self.v1[self.idx1 - 1]
            else:  # self.turn == 1
                self.idx2 += 1
                self.turn = 1- self.turn
                return self.v2[self.idx2 - 1]
            
        elif self.idx1 < len(self.v1) and self.idx2 == len(self.v2):
            self.idx1 += 1
            return self.v1[self.idx1 - 1]
        elif self.idx1 == len(self.v1) and self.idx2 < len(self.v2):
            self.idx2 += 1
            return self.v2[self.idx2 - 1]
        else:
            return None
-------------------------------------------------------------------------------

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = collections.deque()
        
        if v1:
            self.queue.append((v1, 0))
        
        if v2:
            self.queue.append((v2, 0))
        
    def next(self) -> int:
        if self.queue:
            v, _iter = self.queue.popleft()
            val = v[_iter]
            _iter += 1
            if _iter < len(v):
                self.queue.append((v, _iter))
            
            return val

    def hasNext(self) -> bool:
        return len(self.queue) != 0
-------------------------------------------------------------------------------      
          
          
  
      
