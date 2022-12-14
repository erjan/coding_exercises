'''
Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
Given an integer k, return the number of non-negative integers x have the property that f(x) = k.
'''

class Solution:
    def findzeroes(self,num):
        # This part takes log(n) time
        tmp=0
        val=5
        while val<=num:
            tmp+=num//val
            val*=5
        return tmp
    def preimageSizeFZF(self, k: int) -> int:

        if k==0:return 5
        high=5
        while True:
            tmp=self.findzeroes(high)
            if tmp==k:return 5
            if tmp>k:break
            high*=5
        low=high//5
        while low<=high:
            mid=(low+high)//2
            tmp=self.findzeroes(mid)
            if tmp==k:return 5
            if tmp<k:low=mid+1
            else:high=mid-1
        return 0
      
---------------------------------------------------------------------------------
class Solution:

    def preimageSizeFZF(self, k: int) -> int:
        if k < 5:
            return 5
        elif k == 5:
            return 0
        left, right = 4, 5 * k
        while left < right:
            middle = (left + right) // 2
            zeros = sum(middle // pow(5, p)
                        for p in range(1, int(log(middle, 5)) + 1))
            if zeros < k:
                left = middle + 1
            elif zeros > k:
                right = middle - 1
            else:
                return 5
        return 0
      
----------------------------------------------------------------------
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        lo, hi = 0, 1 << 32
        while lo <= hi: 
            mid = lo + hi >> 1
            x, y = mid, 0 
            while x: 
                x //= 5
                y += x
            if y < k: lo = mid + 1
            elif y > k: hi = mid - 1
            else: return 5
        return 0 
