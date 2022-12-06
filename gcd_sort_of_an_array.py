'''
You are given an integer array nums, and you can perform the following operation any number of times on nums:

Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the 
greatest common divisor of nums[i] and nums[j].
Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.
'''


class UnionFind:
    
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True 
        

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        m = max(nums)
        uf = UnionFind(m+1)
        
        seen = set(nums)
        
        # modified sieve of eratosthenes
        sieve = [1]*(m+1)
        sieve[0] = sieve[1] = 0
        for k in range(m//2 + 1): 
            if sieve[k]: 
                for x in range(2*k, m+1, k): 
                    sieve[x] = 0
                    if x in seen: uf.union(k, x)
        return all(uf.find(x) == uf.find(y) for x, y in zip(nums, sorted(nums)))
