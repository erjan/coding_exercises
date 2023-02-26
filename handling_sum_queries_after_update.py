We can find from the question:

We only need to answer sum(nums2) every time encounters a query of type 3.
Every time we can update sum(nums2) by a query of type 2 with sum(nums2) += sum(nums1) * p.
So, we should keep update the sum(nums1) for every query of type 1.
We use Segmentation tree with Lazy Propogation to solve the problem.
For Segmentation tree with Lazy Propogation, we should write three functions, Propogation(proplazy), Update and Query.
In addition to the three functions, we know if we are going to flip all the value in the interval, the sum of the interval will the sum(interval) = len(interval) - sum(interval).
So, we need to record the length self.len and the initial summation self.tree of each node in the first time(i.e. the __init__ function).
For Propogation function, if the parent node has the mark to flip, then we update all summation of children nodes.
This function will work every time we need to access to the children nodes when invoking the following functions.
For Update function, we mark the flipping operation and update the summation, or just iterate with children nodes with lazy propogation.
For Query function, we collect the summation from children nodes with lazy propogation.

class segtree():
    def __init__(self, n, nums):
        self.lazy = defaultdict(int)
        self.len = defaultdict(int)
        self.tree = defaultdict(int)
        # initial length and summation
        self.init_len(1, 0, n, 0, n, nums)
        self.init_num(1, 0, n, 0, n, nums)
        
    def init_len(self, ind, ul, ur, cl, cr, num):
        if cr < cl or cl >= len(num):
            return 0
        if cr == cl:
            self.len[ind] = 1
            return 1
        mid = (cl + cr) // 2
        if cl != cr:
            self.init_len(ind*2, ul, ur, cl, mid, num)
        self.init_len(ind*2+1, ul, ur, mid+1, cr, num)
        self.len[ind] = self.len[ind*2] + self.len[ind*2+1]
    
    def init_num(self, ind, ul, ur, cl, cr, num):
        if cr < cl or cl >= len(num):
            return
        if cl == cr:
            self.tree[ind] = num[cl]
            return
        mid = (cl + cr) // 2
        if cl != cr:
            self.init_num(ind*2, ul, ur, cl, mid, num)
        self.init_num(ind*2+1, ul, ur, mid+1, cr, num)
        
        self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
        
    
    def proplazy(self, ind):
        # if the parent node has the notation to flip, then we update all summation of children nodes.
        if self.lazy[ind]:
            self.lazy[ind*2] ^= self.lazy[ind]
            self.tree[ind*2] = self.len[ind*2] - self.tree[ind*2]
            self.lazy[ind*2 + 1] ^= self.lazy[ind]
            self.tree[ind*2 + 1] = self.len[ind*2+1] - self.tree[ind*2 + 1]
            self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
            self.lazy[ind] = 0
        
    def update(self, ind, ul, ur, cl, cr):
        if cl > ur or cr < ul:
            return 
        if ul <= cl and cr <= ur:
            # mark to flip
            self.lazy[ind] ^= 1
            self.tree[ind] = self.len[ind] - self.tree[ind]
        else:
            mid = (cl + cr) // 2
            self.proplazy(ind)
            self.update(ind*2, ul, ur, cl, mid)
            self.update(ind*2+1, ul, ur, mid+1, cr)
            self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
           
    def query(self, ind, ul, ur, cl, cr):
        if cl > ur or cr < ul:
            return 0
        if ul <= cl and cr <= ur:
            return self.tree[ind]
        else:
            mid = (cl + cr) // 2
            self.proplazy(ind)
            return self.query(ind*2, ul, ur, cl, mid) + self.query(ind*2+1, ul, ur, mid+1, cr)
         
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        seg = segtree(len(nums1) + 10, nums1)
        anss = []
        ans = sum(nums2)
        n = len(nums1) + 10
        for i, j, k in queries:
            if i == 1:
                seg.update(1, j, k, 0, n)
            if i == 2:
                ans += seg.tree[1] * j
            if i == 3:
                anss.append(ans)
        return anss
---------------------------------------------------------------------------------------------------------
class SegTreeLazy: 
    
    def __init__(self, arr: List[int]): 
        """Build the segmentation tree."""
        self.n = n = len(arr)
        self.tree = [0]*(4*n)
        self.lazy = [0]*(4*n)
        
        def build(k: int, lo: int, hi: int) -> None: 
            """Build segment tree from array."""
            if lo+1 == hi: self.tree[k] = arr[lo]
            else: 
                mid = lo + hi >> 1
                build(2*k+1, lo, mid)
                build(2*k+2, mid, hi)
                self.tree[k] = self.tree[2*k+1] + self.tree[2*k+2]
        
        build(0, 0, n)


    def update(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when value in [qlo, qhi) is flipped."""
        if not hi: hi = self.n
        if self.lazy[k]: 
            self.tree[k] = (hi - lo) - self.tree[k]
            if lo+1 < hi: 
                self.lazy[2*k+1] ^= 1
                self.lazy[2*k+2] ^= 1 
            self.lazy[k] = 0
        if lo < hi and qlo < hi and lo < qhi: 
            if qlo <= lo and hi <= qhi: # total overlap
                self.tree[k] = (hi - lo) - self.tree[k]
                if lo+1 < hi: 
                    self.lazy[2*k+1] ^= 1
                    self.lazy[2*k+2] ^= 1
                return 
            mid = lo + hi >> 1
            self.update(qlo, qhi, 2*k+1, lo, mid) 
            self.update(qlo, qhi, 2*k+2, mid, hi)
            self.tree[k] = self.tree[2*k+1] + self.tree[2*k+2]
            

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegTreeLazy(nums1)
        ans = []
        val = sum(nums2)
        for x, y, z in queries: 
            if x == 1: tree.update(y, z+1)
            elif x == 2: val += y * tree.tree[0]
            else: ans.append(val)
        return ans 
