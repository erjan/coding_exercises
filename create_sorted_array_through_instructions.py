'''
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7
'''


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        # Segment Tree
        # use a segment tree to trace the count of each possible value in instructions
        # Time: O(nlogm)
        # Space: O(m)
        
        m = max(instructions)
        tree = [0] * (2 * m)
        
        def update(n):
			# convert the number to tree index
            i = m + n - 1

            while i > 0:
                tree[i] += 1
                i >>= 1
        
        def query(n):
			# query the total count of the numbers in range [1, n], or [1, n + 1)
			# convert left and right boundary to tree index by + m - 1
            left = m
            right = n + m
			
            res = 0
            
            # note that the interval is [left, right)
            while left < right:
                if left & 1:
                    res += tree[left]
                    left += 1
                if right & 1:
                    right -= 1
                    res += tree[right]
                
                left >>= 1
                right >>= 1
                
            return res
        
        cost = 0
        for i, v in enumerate(instructions):
            cost += min(query(v-1), i - query(v))
            update(v)
            
        return cost % (10 ** 9 + 7)
        
---------------------------------------------------------------------------
from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        tree = SortedList()
        counter = Counter()
        cost = 0
        for idx, val in enumerate(instructions):
            tree.add((val, idx))
            pos = tree.index((val, idx))
            cost += min(pos-counter[val], idx - pos)
            counter[val] += 1
        return cost % 1000000007
      
------------------------------------------------------------------------------
from sortedcontainers import SortedList


MOD = int(1e9+7)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        res = SortedList()
        ans = 0
        for i in instructions:
            ans += min(res.bisect_left(i), len(res) - res.bisect_right(i))
            res.add(i)
        return ans % MOD
---------------------------------------------------------------------------
class Solution:
    def createSortedArray(self, A):
        m = max(A)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)

