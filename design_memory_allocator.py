'''
You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

Allocate a block of size consecutive free memory units and assign it the id mID.
Free all memory units with the given id mID.
Note that:

Multiple blocks can be allocated to the same mID.
You should free all the memory units with mID, even if they were allocated in different blocks.
Implement the Allocator class:

Allocator(int n) Initializes an Allocator object with a memory array of size n.
int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
int free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.
'''


import numpy as np

class Allocator:

    def __init__(self, n: int):
        
        self.num = np.zeros(n)
        self.n = n
        
        return 

    def allocate(self, size: int, mID: int) -> int:
    #return the box's first index
        i = 0
        while i < self.n:
            if self.num[i] > 0:
                i = i+1
            elif self.num[i] == 0:
                if i+size > self.n:
                    return -1
                ret = self.check(i,size)
                if ret is True:
                    for m in range(i,i+size):
                        self.num[m] = mID
                    # print(self.num)
                    return i
                else:
                    i = ret+1
        return -1
        

    def free(self, mID: int) -> int:
                
        count = 0
        for i in range(self.n):
            if self.num[i] == mID:
                self.num[i] = 0
                count = count+1
        
        return count
    
    
    def check(self,z,k):
        # print(z,z+k)
        for i in range(z,z+k):
            # print(i)
            if self.num[i] !=0:
                return i
        return True
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

---------------------------------------------------------------------------------------------------------
class Allocator:

    def __init__(self, n: int):
        self.memory = ['_' for i in range(n)]

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        yes = 0
        n = len(self.memory)
        while i < n:
            if self.memory[i] == '_':
                ptr = i
                flag = 0
                while ptr < n and self.memory[ptr] == '_':
                    if ptr - i + 1 == size:
                        flag = 1
                        break
                    ptr += 1
                if flag == 1:
                    for q in range(i,ptr+1):
                        self.memory[q] = mID
                    yes = 1
                    break
                else:
                    i = ptr
            else:
                i += 1
        if yes:
            return i
        else:
            return -1

    def free(self, mID: int) -> int:
        freed = 0 
        n = len(self.memory)
        for i in range(n):
            if self.memory[i] == mID:
                self.memory[i] = '_'
                freed += 1
        return freed
