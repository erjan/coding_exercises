'''
You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.
'''


from collections import Counter

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size+1))
        self.size = [1 for _ in range(size+1)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x == parent_y: return 
        if self.size[parent_x] < self.size[parent_y]:
            self.parent[parent_x] = parent_y 
            self.size[parent_y] += self.size[parent_x]
            return parent_y 
        else:
            self.parent[parent_y] = parent_x 
            self.size[parent_x] += self.size[parent_y]
            return parent_x

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        ds = DisjointSet(max(nums))
        for x in nums:
            for A in range(2, int(sqrt(x)) + 1):
                if x % A == 0:
                    ds.union(x, A)
                    ds.union(x, x // A)
        # find the max size among all sets
        c = Counter()
        for n in nums:
            c[ds.find(n)] += 1
        return max(c.values())
      
------------------------------------------------------------------------------------------------------------------------------
Union and Find is must !!
One way is to find GCD of every pair and if GCD > 1 means they have an edge so do union 
But this method will give TLE 

Now a better solution is by using factors
Factors of 21 are : 3 , 7 
Factors of 63 are : 3 , 7 , 9 , 21

So for 21 we have a child 3 and 7
For 63 we have child 3 
But 3's parent is 21 so 21 and 63 will be joined



class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        def find(node):
            if parent[node] == -1: return node
            else:
                parent[node] = find(parent[node])
                return parent[node]
        
        def union(idx1,idx2):
            par1,par2 = find(idx1),find(idx2)
            if par1!=par2:
                if rank[par1] > rank[par2]:
                    parent[par2] = par1
                elif rank[par2] > rank[par1]:
                    parent[par1] = par2
                else:
                    parent[par2] = par1
                    rank[par1] += 1
        
        n = len(nums)
        parent = defaultdict(lambda:-1)
        rank = defaultdict(lambda:0)
        for i in range(n):
            limit = int(nums[i]**0.5)
            for j in range(2,limit+1):
                if nums[i] % j == 0:
                    union(nums[i],j)
                    union(nums[i],nums[i]//j)
        count = defaultdict(lambda:0)
        best = -1
        for num in nums:
            par = find(num)
            tmp = count[par] + 1
            if tmp > best: best = tmp
            count[par] = tmp
        return best
