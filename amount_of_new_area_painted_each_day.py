There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.


---------------------------------------
This is a question testing your data structure skill, the more advanced data structure you know, the easier it will be. I will provide 3 different solutions

Red-Black Tree (sortedcontainer in python & set in c++)
Prioirty Queue & Set
Segment Tree
The basic concept is called sweep line.

For example paint = [[1,4],[5,8],[4,7]], The picture would be like below


First, put each [start, end] as brown lines, put them on top of the number line one by one ordered by index. and imagine a blue line which will sweep from left to right across all the brown lines.

Moveover, we need another box which can:

add number
delete choosen number
get minimum number
we will discuss the suitable data structure for this box later.

Now, when the blue line sweeps, every time when it touches a start position, it will add the index number to the box, and when it touches an end position, it will remove the index number from the box as the picture shows below.


Now, the answer is very easy, in each position, you will look at the box and get the minimum number from it. If it has a minimum number, it's the index you should +1 for the answer. Since it means this is the index show up earliest at this position.

Solution 1 (Red-Black Tree)
So, which data structure can support quick O(logN) random add, delete and get minimum? You will need an auto-balanced tree structure like AVL or Red-Black tree for this. Of course you won't construct one of them by yourself, so you can use sortedcontainer in python or set in c++. It can make things much easier. Below is a Python sample code.

from sortedcontainers import SortedList
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # constructure the sweep line
        records = []
        max_pos = 0
        for i, [start, end] in enumerate(paint):
            records.append((start, i, 1)) # use 1 and -1 to records the type.
            records.append((end, i, -1))
            max_pos = max(max_pos, end)
        records.sort()

        # sweep across all position
        ans = [0 for _ in range(len(paint))]
        indexes = SortedList()
        i = 0
        for pos in range(max_pos + 1):
            while i < len(records) and records[i][0] == pos:
                pos, index, type = records[i]
                if type == 1:
                    indexes.add(index)
                else:
                    indexes.remove(index)
                i += 1
            if indexes:
                ans[indexes[0]] += 1
        return ans
Solution 2 (Priority Queue + Set)
If you didn't feel good to use this kind of data structure, you could use priority queue plus a set

The priority queue could add and get minimum
The set will be used to record those indexes which already ended
Each time when you want to get minimum number from the priority queue, you need to discard all those ended indexes already recoeded in the set

The code will be a little more complex. like below:

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # constructure the sweep line
        records = []
        max_pos = 0
        for i, [start, end] in enumerate(paint):
            records.append((start, i, 1)) # use 1 and -1 to records the type.
            records.append((end, i, -1))
            max_pos = max(max_pos, end)
        records.sort()

        # sweep across all position
        ans = [0 for _ in range(len(paint))]
        indexes = []
        ended_set = set()
        i = 0
        for pos in range(max_pos + 1):
            while i < len(records) and records[i][0] == pos:
                pos, index, type = records[i]
                if type == 1:
                    heapq.heappush(indexes, index)
                else:
                    ended_set.add(index)
                i += 1
            
            while indexes and indexes[0] in ended_set:
                heapq.heappop(indexes)

            if indexes:
                ans[indexes[0]] += 1
        return ans
So Problem solved? Wait a Minute!!

Solution 3 (Segment Tree)
Actually, we have another very easy and naive way to handle this question. If only you know how to construct a Segment-Tree, you don't even need to use the sweep line.

A sophisticated Segment-Tree (with lazy evaluation) can support efficient range update and query. That is, it can do the following two things at O(logN) time.

Choose a range and update all the values in that range to some new value
Query a range and return the sum of the range.
So, for this question, we can use 1 and 0 to records a place is used or not. For the beginning, the whole array will be zero, like: [0,0,0,0,0,0,0]. (If we only have 7 places).

After we add a range [2,5]. We can update all the value between [2, 5) to 1, so the array will be [0,0,1,1,1,0,0]. Notice that we should update the position from start to end - 1.

image

Now, when we want to count the answer, we only need to know how many 1 are already in that range (which is equal to the sum of the range). The pseudo code will be as easy as

ans = []
for (int i = 0; i < paint.size(); i++) {
    start = paint[i][0];
    end = paint[i][1] - 1;
    ans.append(end - start + 1 - segment_tree_query(start, end)); # query the sum of this range, takes O(logN) time.
    segment_tree_update(start, end, 1); # update all value in this range to be 1, which also takes O(logN) time.
}
return ans;
Unfortunately, a Python version won't be quick enough to pass the question since the time constraint is tight. However, a c++ version can do it, below is my solution.

const int MAX_SIZE = 5e4+5;
long long seg_tree[4*MAX_SIZE], lazy[4*MAX_SIZE];

void build(long long a[], int v, int tl, int tr) {
    if (tl == tr) {
        seg_tree[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        seg_tree[v] = seg_tree[v*2] + seg_tree[v*2+1];
    }
}

void push(int v, int tl, int tr) {
    if (lazy[v] > -(1e18+10)) {
        seg_tree[v] = lazy[v] * (tr - tl + 1);
        if (tl < tr) { // still have children
            lazy[v*2] = lazy[v];
            lazy[v*2+1] = lazy[v];
        }
        lazy[v] = -(1e18+10);
    }
}

void _update(int v, int tl, int tr, int l, int r, int addend) {
    push(v, tl, tr);
    if (l > r) 
        return;
    if (l == tl && tr == r) {
        lazy[v] = addend;
    } else {
        int tm = (tl + tr) / 2;
        _update(v*2, tl, tm, l, min(r, tm), addend);
        _update(v*2+1, tm+1, tr, max(l, tm+1), r, addend);
        push(v*2, tl, tm);
        push(v*2+1, tm+1, tr);
        seg_tree[v] = seg_tree[v*2] + seg_tree[v*2+1];
    }
}

void update(int N, int l, int r, int addend) {
    _update(1, 0, N-1, l, r, addend);
}

long long _query(int v, int tl, int tr, int l, int r) {
    push(v, tl, tr);
    if (l > r)
        return 0;
    if (l <= tl && tr <= r)
        return seg_tree[v];
    int tm = (tl + tr) / 2;
    return _query(v*2, tl, tm, l, min(r, tm)) + _query(v*2+1, tm+1, tr, max(l, tm+1), r);
}

long long query(int N, int l, int r) {
    return _query(1, 0, N-1, l, r);
}

class Solution {
public:
    vector<int> amountPainted(vector<vector<int>>& paint) {
        // Reset global variables
        memset((seg_tree), 0, sizeof((seg_tree)));
        memset((lazy), 0, sizeof((lazy)));

        // Solution
        vector<int> ans = {};
        for (int i = 0; i < paint.size(); i++) {
            int start = paint[i][0];
            int end = paint[i][1] - 1;
            ans.push_back(end - start + 1 - query(MAX_SIZE, start, end));
            update(MAX_SIZE, start, end, 1);
        }
        return ans;
    }
};
Time complexity
Solution 1 & 2:
O(NlogN)

Solution 3:
K = (max position of all end points)
O(NlogK)


--------------------------------------------------------------------------------------------------------
class SegmentTree:
    def __init__(self, N: int):
        self.tree = [0] * N
    
    def increment(self, qlo: int, qhi: int, lo: int, hi: int, pos: int) -> int:
        total = hi - lo + 1
        
        if self.tree[pos] == total:     # if the node is full, return 0
            return 0
        
        if qlo <= lo <= hi <= qhi:      # case 1, total overlap
            missing = total - self.tree[pos]
            self.tree[pos] = total
            return missing
        elif qlo > hi or qhi < lo:      # case 2, NO overlap
            return 0
        
        mid = lo + (hi - lo) // 2       # case 3, partial overlap
        left = self.increment(qlo, qhi, lo, mid, 2 * pos + 1)
        right = self.increment(qlo, qhi, mid + 1, hi, 2 * pos + 2)
        self.tree[pos] += left + right
        return left + right
                

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        
        N = max(r for _, r in paint)
        
        tree = SegmentTree(4 * N)
        worklog = []
        
        for qlo, qhi in paint:
            work = tree.increment(qlo, qhi-1, 0, N, 0)
            worklog.append(work)
            
        return worklog
        
-----------------------------------------------------------------------------
Initialize a 1D number jump array of size 50000
Iterate on intervals
For each interval traverse start to end marking jump value as end.
if any jump index is already marked (i.e. > 0) skip to the jump value, saving traversal. and continue #3 till interval is complete.
        p = [0] * 50000 # 1D number array
        ans = []
        for (start,end) in paint:
            res = 0
            # loop from start to end of the interval
            while start < end : 
                # if jump value is set
                if p[start] != 0 : 
                    start = p[start]
                # if jump value is not set
                else :
                    res += 1
                    p[start] = end
                    start += 1
           
            ans.append(res)
        return ans
        
---------------------------------------------
class Solution:
	def amountPainted(self, paint: List[List[int]]) -> List[int]:
		"""
		"""
		wall=(1<<max([end for start,end in paint]))-1
		output=[]
		for start, end in paint:
			### count ones from start to end. remove everything before end by wall-((wall>>end)<<end). 
			###remove everything after start by >>start. count number of 1s using .bit_count()
			output.append(((wall-((wall>>end)<<end))>>start).bit_count())
			### make everything from start to end 0. get a number will 1s till end by ((1<<end)-1) make everything zero after start by (num>>start)<<start. 
			###Negate the bits using ~ operations to get a mask with 0s only at position start to end. 
			### the mask with the wall to get the new painted wall.
			wall&= ~((((1<<end)-1)>>start)<<start)
		return output
    
-------------------------------------------
This solution is a small tweak of merge-intervals where the intervals arrive out-of-order. The premise is to keep an array of start/end points that it never overlaps. The array is arranged [s0, e0, s1, e1, s2, e2, ...]. The invariant is that it's strictly increasing, otherwise there would be overlaps. To insert a new interval, use binary-search for the start and end points. Using the insertion points and the sub-intervals you erase, you can calculate the new area.

The only tricky thing here is that slice replacement in python is O(n), since I suppose it may need to replace the entire backing array.

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        arr = []
        result = []
        for si, ei in paint:
            left = bisect.bisect_left(arr, si)
            right = bisect.bisect_right(arr, ei)
            segment = []
            area = 0
            if left == right and left % 2 == 0:
                area += ei - si
            if left % 2 == 0:
                segment.append(si)
                if left != right:
                    area += arr[left]-si
            if right % 2 == 0:
                segment.append(ei)
                if left != right:
                    area += ei - arr[right-1]
            
			# Count area between intervals we're overwriting, 
			# e.g. [...e1, s2, ...]
			# Ensure we start from an e and not an s.
            for i in range(2*(left//2) + 1, right-1, 2):
                area += arr[i+1]-arr[i]
            result.append(area)
            arr[left:right] = segment
            
        return result
