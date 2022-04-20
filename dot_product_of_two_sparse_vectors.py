'''
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

 
 '''

Suggestions to make it better are always welcomed.

We can write 1 liners for below code as well.

Approach:
If dotProduct() is called million times, it will be good if we consider only the non-zero values to save time. So, let's use dictionary.
Now, we can multiply the values for same indexes in both the dictionaries.

What if 1 dictionary is thousand times bigger than the other? Can we reduce the time it takes to get the result?
If we compare the lengths and loop on the smaller dictionary, we can get result much faster. Time complexity still remains O(len(dictionary)) but it's better.

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i: n for i, n in enumerate(nums) if n}

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        if len(self.nums) < len(vec.nums):
            for key in self.nums.keys():
                if key in vec.nums:
                    result += self.nums[key] * vec.nums[key]
        else:
            for key in vec.nums.keys():
                if key in self.nums:
                    result += self.nums[key] * vec.nums[key]
                    
        return result      
----------------------------------------

We are instructed to store the sparse vector efficently. This is a clue to use a dict/map.

class SparseVector:

    def __init__(self, nums):
        self.ix = {i: x for i, x in enumerate(nums) if x}

    def dotProduct(self, vec):
        a, b = self.ix, vec.ix
        return sum(a[i] * b[i] for i in a if i in b)
If one vector is sparse, and the other is not, we can update dotProduct() to iterate through the shorter:

class SparseVector:

    # as above

    def dotProduct(self, vec):
        a, b = self.ix, vec.ix
        if len(a) > len(b):
            a, b = b, a
        return sum(a[i] * b[i] for i in a if i in b)
We can also use this question as an opporunity to showcase familiarity with supporting Python's built-in functions. See Slatkin's "Effective Python" Item 28 for details.

class SparseVector:

    def __init__(self, nums: List[int]):
        self.ix = {i: x for i, x in enumerate(nums)}

    def __getitem__(self, i):
        return self.ix.__getitem__(i)

    def __contains__(self, i):
        return self.ix.__contains__(i)

    def __iter__(self):
        return self.ix.__iter__()

    def __len__(self):
        return self.ix.__len__()

    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self, vec
        if len(a) > len(b):
            a, b = b, a
        return sum(a[i] * b[i] for i in a if i in b)
---------------------------------------------

class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse = [(i, v) for i, v in enumerate(nums) if v]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        
        i1 = 0
        i2 = 0         
        while i1 < len(vec.sparse) and i2 < len(self.sparse):
            if vec.sparse[i1][0] < self.sparse[i2][0]:
                i1 += 1
            elif vec.sparse[i1][0] > self.sparse[i2][0]:
                i2 += 1
            else:
                product += vec.sparse[i1][1] * self.sparse[i2][1]
                i1 += 1
                i2 += 1
                
        return product
      
-------------------------------------

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vect = {i:n for i,n in enumerate(nums) if n != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        tot = 0
        for k, v in self.vect.items():
            tot += v * vec.vect.get(k, 0)
        return tot
----------------------------------

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums=nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum=0
        for i,v in zip(self.nums,vec.nums):
            sum+=(i*v)
        return sum
      
----------------------------------      
      
      
      
