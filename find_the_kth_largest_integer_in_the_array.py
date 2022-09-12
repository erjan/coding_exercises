'''
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.
'''

def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n=[]
        for i in nums:
            n.append(int(i))
        return str(sorted(n)[-k])
        
---------------------------------------------------------------------
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = [(0, "")] * k
        
        for num in nums:
            heappushpop(heap, (len(num), num))
            
        return heap[0][1]
      
---------------------------------------------------
from functools import cmp_to_key
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sorter(x, y):
            n, m = len(x), len(y)
            if n < m: # if you want to keep x in left of y, return -1, here if len(x) is shorter, so it is smaller, so left # ['33', '4'], 4 to left
                return -1
            elif n > m: # +1, if to keep in right of y
                return 1
            else:
                for i in range(n):
                    if x[i] < y[i]: # if x[i] smaller, then left
                        return -1
                    elif x[i] > y[i]: # else in right 
                        return 1
                    else:
                        continue
            return 0 # if both same, x==y
            
        key = cmp_to_key(sorter)
        nums.sort(key=key, reverse=True)
        # print(nums)
        return nums[k-1]
