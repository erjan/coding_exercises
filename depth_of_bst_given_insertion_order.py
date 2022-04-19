'''
You are given a 0-indexed integer array order of length n, a permutation of integers from 1 to n representing the order of insertion into a binary search tree.

A binary search tree is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
The binary search tree is constructed as follows:

order[0] will be the root of the binary search tree.
All subsequent elements are inserted as the child of any existing node such that the binary search tree properties hold.
Return the depth of the binary search tree.

A binary tree's depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


from sortedcontainers import SortedList

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        ans = 0 
        mp, sl = {}, SortedList()
        for x in order: 
            k = sl.bisect_left(x)
            val = 1
            if k: val = 1 + mp[sl[k-1]]
            if k < len(sl): val = max(val, 1 + mp[sl[k]])
            ans = max(ans, val)
            sl.add(x)
            mp[x] = val
        return ans 
from sortedcontainers import SortedDict

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        sd = SortedDict()
        for x in order: 
            k = sd.bisect_left(x)
            val = 1
            if k: val = 1 + sd.values()[k-1]
            if k < len(sd): val = max(val, 1 + sd.values()[k])
            sd[x] = val
        return max(sd.values())
      
---------------------------------------------------------------------------------------------
Since all elements are unique and within [1..n], we can represent our tree as intervals.

We start with [1..n] interval, and the depth of that interval is 0. When we insert, say, 3, we split that interval into two: [1..2] and [4..n], and increment their depth. For any value, we can quickly find it's interval using binary search.

The picture below demonstrates how we split intervals for this test case: [3,5,1,2,6,7,4]

image

To model this logic, we can use a map to store numbers and their depth. When we insert a new number, we first find the insert position (O(n log )). Then, we get the depth of numbers on the left and right (our interval). Finally, we insert a new value, and its depth is the maximum depth of the neighbours, plus 1.

C++

int maxDepthBST(vector<int>& order) {
    map<int, int> m{{0, 0}, {100001, 0}};
    for (int i : order) {
        auto it = m.upper_bound(i);
        m[i] = 1 + max(it->second, prev(it)->second);
    }
    return max_element(begin(m), end(m), [](const auto& a, const auto &b){ return a.second < b.second; })->second;
}
Java

public int maxDepthBST(int[] order) {
    TreeMap<Integer, Integer> m = new TreeMap<>();
    for (int i : order) {
        Map.Entry<Integer, Integer> l = m.floorEntry(i), r = m.ceilingEntry(i);
        m.put(i, 1 + Math.max(l == null ? 0 : l.getValue(), r == null ? 0 : r.getValue()));
    }
    return m.entrySet().stream().max((a, b) -> a.getValue().compareTo(b.getValue())).get().getValue();
}
Python 3
This also works with standard bisect_left; it's just faster with sortedcontainers.

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        from sortedcontainers import SortedList
        sl, d = SortedList([0, 100001]), { 0 : 0, 100001 : 0 }
        for i in order:
            j = sl.bisect_left(i)
            d[i] = 1 + max(d[sl[j - 1]], d[sl[j]])
            sl.add(i)
        return max(d.values())
      
--------------------------------------------------------------------------------------------------------------
Each value will be below its existing upper bould and lower bound, which even is lower in the tree

from sortedcontainers import SortedDict

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
		# python way for binary treemap
        depths = SortedDict()
		# add dummy bounds to avoid extra ifs
        depths[-math.inf] = 0
        depths[math.inf] = 0
        
		# for every value find bounds and take the lowest depth + 1
		# put the value back to depths
        for x in order:
            i = depths.bisect_left(x)
            depths[x] = 1 + max(depths.values()[i - 1:i + 1])
        # return the maximum value so far
        return max(depths.values())
      
      
