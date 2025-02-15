Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

--------------------------
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(x, target):
            if x==target: return True
            if x==0: return target==0
            for m in (10, 100, 1000):
                if partition(x//m, target-x%m):
                    return True
            return False
        return sum(x for i in range(1, n+1) if partition(x:=i*i, i))
       
