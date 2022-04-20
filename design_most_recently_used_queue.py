'''
Design a queue-like data structure that moves the most recently used element to the end of the queue.

Implement the MRUQueue class:

MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.
 

Example 1:

Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.
'''


Approach 1 - brute force
O(N) initialization & fetch

class MRUQueue:

    def __init__(self, n: int):
        self.data = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        self.data.append(self.data.pop(k-1))
        return self.data[-1]
Approach 2 - square root decomposition
O(N) initializaiton & O(sqrt(N)) fetch

class MRUQueue:

    def __init__(self, n: int):
        self.n = n 
        self.nn = int(sqrt(n))
        self.data = []
        self.index = []
        for i in range(1, n+1):
            ii = (i-1)//self.nn 
            if ii == len(self.data): 
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)
            
    def fetch(self, k: int) -> int:
        i = bisect_right(self.index, k)-1
        
        x = self.data[i].pop(k - self.index[i])
        for ii in range(i+1, len(self.index)): # shift index
            self.index[ii] -= 1
        if len(self.data[-1]) >= self.nn: # add new bucket 
            self.data.append([])
            self.index.append(self.n)
        self.data[-1].append(x) # append to bucket at end
        if not self.data[i]: # remove empty bucket 
            self.data.pop(i)
            self.index.pop(i)
        return x
Approach 3 - Fenwick tree
O(NlogN) initialization & O(log^2N) fetch

class Fenwick: 
    def __init__(self, n: int): 
        self.nums = [0]*(n+1)
        
    def sum(self, k: int) -> int: 
        ans = 0
        while k: 
            ans += self.nums[k]
            k &= k-1
        return ans 
    
    def add(self, k: int, x: int) -> int: 
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 


class MRUQueue:

    def __init__(self, n: int):
        self.size = n 
        self.tree = Fenwick(n+2000) # buffer for 2000 calls
        self.vals = [0]*(n+2000)
        for i in range(n):
            self.tree.add(i, 1)
            self.vals[i] = i+1

    def fetch(self, k: int) -> int:
        lo, hi = 0, self.size
        while lo < hi: 
            mid = lo + hi >> 1 
            if self.tree.sum(mid) < k: lo = mid + 1
            else: hi = mid 
        self.tree.add(lo-1, -1)
        self.tree.add(self.size, 1)
        self.vals[self.size] = self.vals[lo-1]
        self.size += 1
        return self.vals[lo-1]

Edited on 2/14/2021
SortedList (based on binary search tree) from sortedcontainers library can be used to solve this problem efficiently.

from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.data = SortedList((i, i) for i in range(1, n+1))

    def fetch(self, k: int) -> int:
        _, x = self.data.pop(k-1)
        i = self.data[-1][0] + 1 if self.data else 0
        self.data.add((i, x))
        return x
-----------------------------------------------

lass MRUQueue:
    def __init__(self, n: int):
        self.queue = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        item = self.queue[k-1]
        self.queue.remove(item)
        self.queue.append(item)
        return item
      
