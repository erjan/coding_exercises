'''
A scenic location is represented by its name and attractiveness score, where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:

Adding scenic locations, one at a time.
Querying the ith best location of all locations already added, where i is the number of times the system has been queried (including the current query).
For example, when the system is queried for the 4th time, it returns the 4th best location of all locations already added.
Note that the test data are generated so that at any time, the number of queries does not exceed the number of locations added to the system.

Implement the SORTracker class:

SORTracker() Initializes the tracker system.
void add(string name, int score) Adds a scenic location with name and score to the system.
string get() Queries and returns the ith best location, where i is the number of times this method has been invoked (including this invocation).
 
 '''

from heapq import *

class MinHeapItem:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        return self.score < other.score or \
               (self.score == other.score and self.name > other.name)

class MaxHeapItem:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        return self.score > other.score or \
               (self.score == other.score and self.name < other.name)

class SORTracker:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.i = 1

    def add(self, name: str, score: int) -> None:
        current = MinHeapItem(name, score)
        if len(self.min_heap) < self.i:
            heappush(self.min_heap, current)
        elif current > self.min_heap[0]:
            temp = heapreplace(self.min_heap, current)
            heappush(self.max_heap, MaxHeapItem(temp.name, temp.score))
        else:
            heappush(self.max_heap, MaxHeapItem(name, score))
        

    def get(self) -> str:
        ans = self.min_heap[0].name
        self.i += 1        
        if self.max_heap:
            temp = heappop(self.max_heap)
            heappush(self.min_heap, MinHeapItem(temp.name, temp.score))
        return ans
----------------------------------------------------------------------------------
from sortedcontainers import SortedList

class SORTracker:

    def __init__(self):
        self.gets = 0
        self.locs = SortedList()

    def add(self, name: str, score: int) -> None:
	    # O(log(N)) where N is the number of locations before
        self.locs.add((-score, name))

    def get(self) -> str:
	    # O(log(N)) where N is the number of locations
        score, name = self.locs[self.gets]
        self.gets += 1
        return name
      
-----------------------------------------
from sortedcontainers import SortedList

class SORTracker:

    def __init__(self):
        self.main = SortedList()
        self.numcall = 0
        

    def add(self, name: str, score: int) -> None:
        self.main.add((-score,name))
              

    def get(self) -> str:
        _ , name = self.main[self.numcall]
        self.numcall+=1
        return name
