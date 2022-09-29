'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
'''

from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) < k:
            return []
        
        
        heap = []
        
        for val in arr:
            dist = abs(val - x)
            
            if len(heap) < k:
                heappush(heap, (-1 * dist, val))
            else:
                if -1 * heap[0][0] > dist:
                    heappop(heap)
                    heappush(heap, (-1 * dist, val))
        
        return sorted([val for _, val in heap])  
      
-------------------------------------------------------------------------------------------------------------
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        result = []
        for i in arr:
            heapq.heappush(heap, (abs(i - x), i))
        
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k-= 1
        
        return sorted(result)
