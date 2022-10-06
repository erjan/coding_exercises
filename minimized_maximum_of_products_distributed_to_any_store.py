'''
You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.
'''

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def cond(m, n):
            return sum([(q // m) + (q % m > 0) for q in quantities]) <= n
        
        l, r = 1, max(quantities)
        while l < r:
            m = (l + r) // 2
            if cond(m, n):
                r = m
            else:
                l = m + 1
        return l
      
-----------------------------------------------------------------
'''
Explanation
Binary search the products distributed to every store.
The search range it between left = 1 and right = 100000.
We can also use right = max(A), no big difference.

For a products to distributed,
we needs ceil(A[i] / mid) store,
I use (a + mid - 1) / mid to calculate this.

We sum up the stores we needs and check whether we have that enough stores.
If we have enough stores,
mid is big enough.
then change right = mid

If we have no enough stores,
mid is too small,
then change left = mid + 1
'''

    def minimizedMaximum(self, n, A):
        left, right = 1, max(A)
        while left < right:
            x = (left + right) / 2
            if sum((a + x - 1) / x for a in A) > n:
                left = x + 1
            else:
                right = x
        return left
