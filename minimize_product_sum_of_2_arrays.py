'''
The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (0-indexed).

For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed to rearrange the order of the elements in nums1. 

 

Example 1:

Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
Output: 40
Explanation: We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.
Example 2:

Input: nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]
Output: 65
Explanation: We can rearrange nums1 to become [5,7,4,1,2]. The product sum of [5,7,4,1,2] and [3,2,4,8,6] is 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65.
'''



Simple one liner O(nlogn)

def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum([x*y for x,y in zip(sorted(nums1), sorted(nums2, reverse=True))])
Make use of the fact that 1 <= nums1[i], nums2[i] <= 100 in order to achieve O(n) time

def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1count, nums2count = [0]*101, [0]*101
        m, n = len(nums1), len(nums1count)
        
        # Fill counting arrays
        for i in range(m):
            nums1count[nums1[i]] += 1
            nums2count[nums2[i]] += 1
        
        # Meet in the middle and multiply at each end
        l, r, product_sum = 0, n-1, 0
        while 0 < r and l < n:
            if not nums1count[l]:
                l += 1
            if not nums2count[r]:
                r -= 1
            if 0 < r and l < n and nums1count[l] and nums2count[r]:
                min_ = min(nums1count[l], nums2count[r])
                product_sum += l*r*min_
                nums1count[l] -= min_
                nums2count[r] -= min_
        return product_sum
      
----------------------------------------------

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        return sum([i*j for (i, j) in zip(sorted(nums1), sorted(nums2, reverse=True))])
      
      
-------------------------------------------------------------------------
The description says we can rearrange nums1. This means we get to decide which items of nums1 match up with which items of nums2. There are two obvious options: We either match up the numbers that are closest together or the ones that are furthest apart. You can think of this as making rectangles that are more or less square. Less square rectangles will give us a smaller total area, and therefore a smaller total sum. We can check this with an example. Let's say we have two lists of 1, 2, 3.

1 * 1 + 2 * 2 + 3 * 3 = 14
1 * 3 + 2 * 2 + 3 * 1 = 10
So we want to match largest and smallest. The description only says we can rearrange nums1, but we only have to return the sum of products. This means we can rearrange them both for simplicitly and speed. One sorted forward, one sorted backwards. Then we get:

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum(map(operator.mul, sorted(nums1), sorted(nums2, reverse=True)))
From inside to out: Sort both lists, one regular and one reverse. Map them as arguments to mul, which is just a multiplication function. Sum it up and return it.

The time complexity is O(n log n). There are other sorts with better complexity for this case, but the optimizations of Python's built-in sorted will be faster in practice.

But what if you were in an interview?

Try this and see what they say. At most you might be asked to implement your own sort function, in which case you could use the rest of the code here and your sort function.

-----------------------------------------------------------------------


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse = True)
        output = 0
        for index, val in enumerate(nums1):
            output += (val * nums2[index])
        return output
      
-----------------------------------------------------
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        def productSum(a,b):
            productsum = 0
            for i in range(0,len(a)):
                productsum+= (a[i]*b[i])
            return productsum
        
        return productSum(sorted(nums1,reverse=True),sorted(nums2))

---------------------------------------------------------------------------

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)        
        return sum(x*y for x,y in zip(nums1, nums2))
      
      
