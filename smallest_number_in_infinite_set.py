'''
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 
 '''

from heapq import heapify, heappop, heappush

class SmallestInfiniteSet:
    def __init__(self):
        self.next_num = 1
        self.added_back_heap = []
        self.added_back_set = set()
        

    def popSmallest(self) -> int:
        if self.added_back_heap:
            smallest = heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
            return smallest
    
        num_to_return = self.next_num
        self.next_num += 1
        return num_to_return
        

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.added_back_set:
            self.added_back_set.add(num)
            heappush(self.added_back_heap, num)
