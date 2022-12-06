'''
You are given a 0-indexed array of strings words. Each string consists of lowercase English letters only. No letter occurs more than once in any string of words.

Two strings s1 and s2 are said to be connected if the set of letters of s2 can be obtained from the set of letters of s1 by any one of the following operations:

Adding exactly one letter to the set of the letters of s1.
Deleting exactly one letter from the set of the letters of s1.
Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.
The array words can be divided into one or more non-intersecting groups. A string belongs to a group if any one of the following is true:

It is connected to at least one other string of the group.
It is the only string present in the group.
Note that the strings in words should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.

Return an array ans of size 2 where:

ans[0] is the maximum number of groups words can be divided into, and
ans[1] is the size of the largest group.
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
        self.parent[prt] = self.parent[qrt]
        self.rank[qrt] += self.rank[prt]
        return True 


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        uf = UnionFind(n)
        seen = {}
        for i, word in enumerate(words): 
            m = reduce(or_, (1<<ord(ch)-97 for ch in word))
            if m in seen: uf.union(i, seen[m])
            for k in range(26): 
                if m ^ 1<<k in seen: uf.union(i, seen[m ^ 1<<k])
                if m & 1<<k: 
                    mm = m ^ 1<<k ^ 1<<26
                    if mm in seen: uf.union(i, seen[mm])
                    seen[mm] = i
            seen[m] = i 
        freq = Counter(uf.find(i) for i in range(n))
        return [len(freq), max(freq.values())]
