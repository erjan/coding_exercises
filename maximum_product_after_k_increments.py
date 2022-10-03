'''
You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

Return the maximum product of nums after at most k operations. Since the 
answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 
'''


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
        heap = nums
        
        heapq.heapify(nums)
        
        while k :
            
            temp = heapq.heappop(heap)
            heapq.heappush(heap,temp+1)
            k = k-1
        
        res = 1
        
        for n in heap:
            res = (res * n) % (10**9+7)
            
        return res
            
----------------------------------------------------------------------------------------------------------
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap = nums.copy()
        heapify(heap)
        for i in range(k):
            t = heappop(heap)
            heappush(heap, t + 1)
        ans = 1
        mod = 1000000007
        for i in heap:
            ans = (ans*i) % mod
        return ans
--------------------------------------------------------------------------------------------------
import heapq

class Solution:
    def maximumProduct(self, nums, k: int) -> int:
        
        # creating a heap
        heap = []
        for i in nums:
            heapq.heappush (heap,i)
            
            
        # basic idea here is keep on incrementing smallest number, then only multiplication of that number will be greater
        # so basically till I have operations left I will increment my smallest number
        while k :
            current = heapq.heappop(heap)
            heapq.heappush(heap, current+1)
            k-=1
            
        result =1
        
        # Just Multiply all the numbers in heap and return the value
        while len(heap)>0:
            x= heapq.heappop(heap)
            result =(result*x )% (10**9+7)
            
        return result
