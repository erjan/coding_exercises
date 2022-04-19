'''
Given a sorted integer array nums and three integers a, b and c, apply a quadratic 
function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and 
return the array in a sorted order.
'''



Intro
Math + Two Pointers

I feel like this is more of a Math question than Two Pointer algorithm.

Math fact:
if a>0: the quadratic function is something like this

y
^
|	+               +
|	 +             +
|	   +         +
|		   + +
---------------------------> x
if a<0: the quadratic function is something like this

y
^
|	       + +
|	   +         +  
|	 +             +
|	+	            +
---------------------------> x
About this question
We have a sort list nums from small to large.
I hope you know what vertex is and how it's calculated. Vertex x = -b/(2a). Tho, formula is not important, but the concept is. Vertex is the center x so that y is max or min (depending on sign of a).
When a > 0, we have 3 senarios:

nums[-1] <= vertex, meaning all values in nums will be on the left side of the center line of the quadratic function graph. (Decreasing side)
nums[0] >= vertex, meaning all values in nums will be on the right side of the center line of the quadratic function graph. (Increasing side)
nums[0] <= nums[i] <= vertex <= nums[j] <= nums[-1], meaning some values are on the left and some are on the right.
How do we take advantage of these given information? Above information can be summed up to following. It tells you:

When a>0, the largest number is either on left or right end of nums.

Correspondingly,
When a<0, the smallest number is either on left or right end of nums.

Then, I think the idea is pretty simple, we use Two Pointer method to pick current largest or smallest in nums and add to new array (you can also do in-place change), depends on the sign of a.

Why we don't care about when a = 0, b > 0 or b <0?
Because, above method can handle that. How?
When a = 0, b > 0, the graph is mono-increase, which is the same case as the right side of quadratic graph when a > 0 (or left side when a < 0).
You can figure out the cooresponding cases for a = 0, b < 0.

Python 3 implementation
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a*x*x + b*x + c 
        n = len(nums)
        index = 0 if a < 0 else n-1
        l, r, ans = 0, n-1, [0] * n
        while l <= r:
            l_val, r_val = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_val > r_val:
                    ans[index] = l_val 
                    l += 1
                else:    
                    ans[index] = r_val 
                    r -= 1
                index -= 1
            else:
                if l_val > r_val:
                    ans[index] = r_val 
                    r -= 1
                else:    
                    ans[index] = l_val 
                    l += 1
                index += 1
        return ans
------------------------------------------------------------------------

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        return sorted(map(lambda x : a*x**2+b*x+c,nums))
      
-----------------------------------

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        
        def cal(x):
            nonlocal a, b, c
            return a * x * x + b * x + c
        
        l, r = len(nums) - 1, 0 # lowest point are at two sides
        if a > 0: # lowest point at x = -b/2a since partial derivative is 2ax + b = 0, expanding around x
            minpos = bisect.bisect_left(nums, -b/2/a)   
            l, r = minpos - 1, minpos
            
        for count in range(len(nums)):
            left = cal(nums[l]) if l >= 0 else float('inf')
            right = cal(nums[r]) if r < len(nums) else float('inf')
            if left < right:
                res.append(left)
                l -= 1
            else:
                res.append(right)
                r += 1
        return res
      
------------------------------------------------------------

class Solution(object):
    def sortTransformedArray(self, nums, aa, bb, cc):
        (toReverse, a, b, c) = (False, aa, bb, cc) if aa >= 0 else (True, -aa, -bb, -cc)
        adapted = [a * (nums[indx] ** 2) + b * nums[indx] + c for indx in xrange(len(nums))]
        minIndx = adapted.index(min(adapted))        
        pos, neg = minIndx, minIndx - 1 
        res = []
        while pos < len(nums) or neg > -1:
            if (neg == -1) or (pos < len(nums) and adapted[pos] <= adapted[neg]):
                res.append(adapted[pos])
                pos += 1
            else:
                res.append(adapted[neg])
                neg -= 1
        return res if not toReverse else [-1 * num for num in reversed(res)]
-------------------------------------------------------------------------


from heapq import merge
from bisect import bisect_left

class Solution:
    def direction(self, a: int, b: int) -> Tuple[bool, bool]:
        if a == 0:
            sign = b >= 0
            return sign, sign
        
        sign = a >= 0
        return not sign, sign
    
    def axis(self, a: int, b: int) -> float:
        if a == 0:
            return 0
        
        return -b / (2 * a)
    
    def generate(self, nums: List[int], start: int, end: int, direction: bool, f: Callable):
        if direction:
            r = range(start, end)
        else:
            r = range(end - 1, start -1, -1)
        
        for i in r:
            yield f(nums[i])
            
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        dl, dr = self.direction(a, b)
        axis = self.axis(a, b)
        i = bisect_left(nums, axis)
        
        f = lambda x: (a * (x ** 2)) + (b * x) + c
                            
        return merge(
            self.generate(nums, 0, i, dl, f),
            self.generate(nums, i, len(nums), dr, f)
        )
-----------------------------------------------------      
      
      
      
      
