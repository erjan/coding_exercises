'''
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.
'''

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maximum_num_each_list(nums: List[int], k_i: int) -> List[int]:
            # monotonically decreasing stack
            s = []
            m = len(nums) - k_i
            for n in nums:
                while s and s[-1] < n and m > 0:
                    s.pop()
                    m -= 1
                s.append(n)
            s = s[:len(s)-m] # very important
            return s
        def greater(a, b, i , j): # get the number which is lexiographically greater
            while i< len(a) or j < len(b): 
                if i == len(a): return False
                if j == len(b): return True
                if a[i] > b[j]: return True
                if a[i] < b[j]: return False
                i += 1 # we increment until each of their elements are same
                j += 1
        
        def merge(x_num, y_num):
            n = len(x_num)
            m = len(y_num)
            i = 0
            j = 0
            s = []
            while i < n or j < m:
                a = x_num[i] if i < n else float("-inf") 
                b = y_num[j] if j < m else float("-inf") 

                if a > b or greater(x_num, y_num, i , j):
# greater(x_num, y_num, i , j): this function is meant for check which list has element lexicographically greater means it will iterate through both arrays incrementing both at the same time until one of them is greater than other.
                    chosen = a
                    i += 1
                else:
                    chosen = b
                    j += 1
                s.append(chosen)
            return s

        max_num_arr = []
        for i in range(k+1): # we check for all values of k and find the maximum number we can create for that value of k and we repeat this for all values of k and then at eacch time merge the numbers to check if arrive at optimal solution
            first = maximum_num_each_list(nums1, i)
            second = maximum_num_each_list(nums2, k-i)
            merged = merge(first, second)
            # these two conditions are required because list comparison in python only compares the elements even if one of their lengths is greater, so I had to add these conditions to compare elements only if length is equal.
			# Alternatively you can avoid this and convert them both to int and then compare, but I wanted to this as  it is somewhat more efficient.
            if len(merged) == len(max_num_arr) and  merged > max_num_arr:
                max_num_arr = merged
            elif len(merged) > len(max_num_arr):
                max_num_arr = merged
        return max_num_arr
      
-------------------------------------------------------------------------------------------------------

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maximum_num_each_list(nums: List[int], k_i: int) -> List[int]:
            # monotonically decreasing stack
            s = []
            m = len(nums) - k_i
            for n in nums:
                while s and s[-1] < n and m > 0:
                    s.pop()
                    m -= 1
                s.append(n)
            s = s[:len(s)-m] # very important
            return s
        def greater(a, b, i , j): # get the number which is lexiographically greater
            while i< len(a) or j < len(b): 
                if i == len(a): return False
                if j == len(b): return True
                if a[i] > b[j]: return True
                if a[i] < b[j]: return False
                i += 1 # we increment until each of their elements are same
                j += 1
        
        def merge(x_num, y_num):
            n = len(x_num)
            m = len(y_num)
            i = 0
            j = 0
            s = []
            while i < n or j < m:
                a = x_num[i] if i < n else float("-inf") 
                b = y_num[j] if j < m else float("-inf") 

                if a > b or greater(x_num, y_num, i , j):
# greater(x_num, y_num, i , j): this function is meant for check which list has element lexicographically greater means it will iterate through both arrays incrementing both at the same time until one of them is greater than other.
                    chosen = a
                    i += 1
                else:
                    chosen = b
                    j += 1
                s.append(chosen)
            return s

        max_num_arr = []
        for i in range(k+1): # we check for all values of k and find the maximum number we can create for that value of k and we repeat this for all values of k and then at eacch time merge the numbers to check if arrive at optimal solution
            first = maximum_num_each_list(nums1, i)
            second = maximum_num_each_list(nums2, k-i)
            merged = merge(first, second)
            # these two conditions are required because list comparison in python only compares the elements even if one of their lengths is greater, so I had to add these conditions to compare elements only if length is equal.
			# Alternatively you can avoid this and convert them both to int and then compare, but I wanted to this as  it is somewhat more efficient.
            if len(merged) == len(max_num_arr) and  merged > max_num_arr:
                max_num_arr = merged
            elif len(merged) > len(max_num_arr):
                max_num_arr = merged
        return max_num_arr
      
---------------------------------------------------------------------------------
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMaxOrder(nums, n, total, res): # monotonic stack
            for i, v in enumerate(nums):
                while res and len(res) + total - i > n and res[-1] < v:
                    res.pop()
                if len(res) < n:
                    res.append(nums[i])
            return res

        def merge(nums1, nums2, ans): # check lexicographically greater
            while nums1 or nums2:
                if nums1 > nums2:
                    ans.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    ans.append(nums2[0])
                    nums2 = nums2[1:]
            return ans

        n1, n2 = len(nums1), len(nums2)
        res = []
        for i in range(max(0, k - n2), min(k, n1) + 1): # find all combinations of nums1 and nums2
            ans = merge(getMaxOrder(nums1, i, n1, []), getMaxOrder(nums2, k - i, n2, []), [])
            res = max(ans, res)
        return res
