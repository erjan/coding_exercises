'''
Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.
'''


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.indexes = defaultdict(list)
        [self.indexes[v].append(i) for i, v in enumerate(arr)]
        self.arr = arr
        
    def range_query(self, l, r, t):
        return bisect_left(self.indexes[t], r+1) - bisect_left(self.indexes[t], l)
    
    def query(self, left: int, right: int, threshold: int) -> int:
        for v in set(self.arr[randint(left, right)] for _ in range(10)):
            if self.range_query(left, right, v) >= threshold:
                return v
        return -1
      
----------------------------------------------------------------------------------------

import numpy as np

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.a = arr
        self.tree = np.zeros(4 * self.n, int)
        self.loc = collections.defaultdict(list)
        for i, v in enumerate(arr):
            self.loc[v].append(i)
        self.build(1, 0, self.n - 1)

    def get_num(self, val, l, r):
        ll = bisect.bisect_left(self.loc[val], l)
        rr = bisect.bisect_right(self.loc[val], r)
        return rr - ll

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.a[start]
        else:
            mid = (start + end) // 2
            l_val = self.build(node * 2, start, mid)
            r_val = self.build(node * 2 + 1, mid + 1, end)
            if l_val > 0 and 2 * self.get_num(l_val, start, end) > end - start + 1:
                self.tree[node] = l_val
            elif r_val > 0 and 2 * self.get_num(r_val, start, end) > end - start + 1:
                self.tree[node] = r_val
        return self.tree[node]

    def query_freq(self, node, start, end, l, r):
        if end < l or start > r:
            return 0
        if l <= start and end <= r:
            if node==15:return self.tree[node]
            return self.tree[node]
        else:
            mid = (start + end) // 2
            l_val = self.query_freq(node * 2, start, mid, l, r)
            r_val = self.query_freq(node * 2 + 1, mid + 1, end, l, r)
            if l_val > 0 and 2 * self.get_num(l_val, l, r) > r-l + 1:
                return l_val
            elif r_val > 0 and 2 * self.get_num(r_val, l, r) > r-l + 1:
                return r_val
        return 0

    def query(self, left: int, right: int, threshold: int) -> int:
        fre_char = self.query_freq(1, 0, self.n - 1, left, right)
        if fre_char>0 and self.get_num(fre_char, left, right) >= threshold:
            return fre_char
        else:
            return -1
