'''
There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of the person 
sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second 
couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap consists 
of choosing any two people, then they stand up and switch seats.
'''



class UnionFind:
    
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1]*n
        
    def find(self, p): 
        if self.parent[p] != p: 
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
    def minSwapsCouples(self, row: List[int]) -> int:
        loc = {x: i for i, x in enumerate(row)} 
        uf = UnionFind(len(row)//2)
        for i, x in enumerate(row): 
            x += -1 if x&1 else 1
            uf.union(i//2, loc[x]//2)
        
        freq = defaultdict(int)
        for x in range(len(row)//2): 
            freq[uf.find(x)] += 1
        return sum(freq.values()) - len(freq)
