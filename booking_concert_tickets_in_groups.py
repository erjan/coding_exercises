'''
A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:

If a group of k spectators can sit together in a row.
If every member of a group of k spectators can get a seat. They may or may not sit together.
Note that the spectators are very picky. Hence:

They will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.
In case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest number is chosen.
Implement the BookMyShow class:

BookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.
int[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. Returns [] in case it is not possible to allocate seats to the group.
boolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.
 
 '''


class SegTree: 

    def __init__(self, arr: List[int]): 
        """Build the segmentation tree."""
        self.n = n = len(arr)
        self.mtree = [0]*(4*n) # for max 
        self.stree = [0]*(4*n) # for sum 
        self._build(arr, 0, 0, n)

    def _build(self, arr: List[int], k: int, lo: int, hi: int) -> None: 
        """Build segment tree from array."""
        if lo+1 == hi: 
            self.mtree[k] = self.stree[k] = arr[lo]
            return 
        mid = lo + hi >> 1
        self._build(arr, 2*k+1, lo, mid)
        self._build(arr, 2*k+2, mid, hi)
        self.mtree[k] = max(self.mtree[2*k+1], self.mtree[2*k+2])
        self.stree[k] = self.stree[2*k+1] + self.stree[2*k+2]

    def update(self, i: int, delta: int, k: int = 0, lo: int = 0, hi: int = 0) -> None:
        """Update segment tree when array value at i is incresed by delta."""
        if lo+1 == hi: # leaf node
            self.mtree[k] += delta
            self.stree[k] += delta
            return 
        mid = lo + hi >> 1
        if i < mid: self.update(i, delta, 2*k+1, lo, mid) 
        else: self.update(i, delta, 2*k+2, mid, hi)
        self.mtree[k] = max(self.mtree[2*k+1], self.mtree[2*k+2])
        self.stree[k] = self.stree[2*k+1] + self.stree[2*k+2]

    def query_max(self, qlo: int, qhi: int, k, lo, hi, val) -> int: 
        """Query max value from qlo (inclusive) and qhi (exclusive)."""
        if qhi <= lo or  hi <= qlo: return -1
        if qlo <= lo and hi <= qhi: 
            if self.mtree[k] < val: return -1 
            while lo+1 < hi: 
                mid = lo + hi >> 1
                if self.mtree[2*k+1] >= val: 
                    k = 2*k+1
                    hi = mid
                else: 
                    k = 2*k+2
                    lo = mid
            return lo
        mid = lo + hi >> 1
        ans = self.query_max(qlo, qhi, 2*k+1, lo, mid, val)
        if ans != -1: return ans 
        return self.query_max(qlo, qhi, 2*k+2, mid, hi, val)
    
    def query_sum(self, qlo: int, qhi: int, k: int = 0, lo: int = 0, hi: int = 0, val = 0) -> int: 
        """Query sum value from qlo (inclusive) and qhi (exclusive)."""
        if qhi <= lo or  hi <= qlo: return 0
        if qlo <= lo and hi <= qhi: return self.stree[k]
        mid = lo + hi >> 1
        return self.query_sum(qlo, qhi, 2*k+1, lo, mid) + self.query_sum(qlo, qhi, 2*k+2, mid, hi)


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.i = 0 
        self.n = n
        self.m = m
        self.seats = [m]*n
        self.tree = SegTree(self.seats)
        
    def gather(self, k: int, maxRow: int) -> List[int]:
        lo = self.tree.query_max(self.i, maxRow+1, 0, 0, self.n, k)
        if lo == -1: return []
        ans = [lo, self.m - self.seats[lo]]
        self.seats[lo] -= k 
        self.tree.update(lo, -k, 0, 0, self.n)
        if lo == self.i and self.seats[lo] == 0: self.i += 1
        return ans 

    def scatter(self, k: int, maxRow: int) -> bool:
        avail = self.tree.query_sum(self.i, maxRow+1, 0, 0, self.n)
        if avail < k: return False 
        lo, hi = self.i, maxRow
        while lo < hi: 
            mid = lo + hi >> 1
            y = self.tree.query_sum(self.i, mid+1, 0, 0, self.n)
            if y < k: lo = mid + 1
            else: hi = mid 
        k -= self.tree.query_sum(self.i, lo, 0, 0, self.n)
        self.seats[lo] -= k 
        self.tree.update(lo, -k, 0, 0, self.n)
        self.i = lo
        if not self.seats[lo]: self.i += 1
        return True 
      
----------------------------------------------------------------------------------------
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m=m
        self.n=n
        cur_list=[m for _ in range(n)]
        dim_sum=[[] for _ in range(n*4)]
        self.cur=0
        
        def build(ids,l,r):
            if l==r:
                dim_sum[ids]=[cur_list[l],cur_list[l]]
                return
            m=(l+r)//2
            build(ids*2,l,m)
            build(ids*2+1,m+1,r)
            dim_sum[ids]=[dim_sum[ids*2][0]+dim_sum[ids*2+1][0],max(dim_sum[ids*2][1],dim_sum[ids*2+1][1])]
        build(1,0,n-1)
        self.dim_sum=dim_sum
        
    def update_sum1(self,ids,l,r,u,v,val):
        if v<l or r<u or u>v:
            return
        if l==r:
            self.dim_sum[ids]=[val,val]
            return
        m=(l+r)//2
        self.update_sum1(ids*2,l,m,u,v,val)
        self.update_sum1(ids*2+1,m+1,r,u,v,val) 
        self.dim_sum[ids]=[self.dim_sum[ids*2][0]+self.dim_sum[ids*2+1][0],max(self.dim_sum[ids*2][1],self.dim_sum[ids*2+1][1])]
    
        
        
    def query_sum(self, ids,l,r,kk):
        if l==r:
            return l,self.dim_sum[ids][0]-kk
        m=(l+r)//2
        if self.dim_sum[ids*2][0]>=kk:
            return self.query_sum(ids*2,l,m,kk)
        else:
            kk-=self.dim_sum[ids*2][0]
            return self.query_sum(ids*2+1,m+1,r,kk)
        
    
    def query_max(self, ids,l,r,kk):
        if l==r:
            return l,self.dim_sum[ids][1]-kk
        m=(l+r)//2
        if self.dim_sum[ids*2][1]>=kk:
            return self.query_max(ids*2,l,m,kk)
        else:
            return self.query_max(ids*2+1,m+1,r,kk)
    
    
    def gather(self, k: int, maxRow: int) -> List[int]:
        a,b=self.query_max(1,0,self.n-1,k)
        if a<=maxRow and b>=0:
            self.update_sum1(1,0,self.n-1,a,a,b)
            return [a,self.m-b-k]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        a,b=self.query_sum(1,0,self.n-1,k)
        if a<=maxRow and b>=0:
            self.update_sum1(1,0,self.n-1,a,a,b)
            self.update_sum1(1,0,self.n-1,self.cur,a-1,0)
            if a-1>self.cur:
                self.cur=a-1
            return True
        return False

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
