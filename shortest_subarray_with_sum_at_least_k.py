'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.
'''


from collections import deque

class Solution:
    def shortestSubarray(self, A: 'List[int]', K: 'int') -> 'int':
        n = len(A)
        sums = [0] * (n+1)
        for i in range(n):
            sums[i+1] = sums[i] + A[i]
        
        mono = deque()
        res = n
        for i in range(n+1):
            while mono and sums[mono[-1]] > sums[i]:
                mono.pop()
            
            while mono and sums[i] - sums[mono[0]] >= K:
                res = min(res, i - mono[0])
                mono.popleft()
                
            mono.append(i)
        if res < n:
            return res
        
        return -1 if sums[n] < K else n
      
------------------------------------------------------------------------------------------------------
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pre = [0]
        for num in A:
            pre.append(pre[-1]+num)
            
        deque = collections.deque()
        result = float(inf)
        for i,sum_ in enumerate(pre):
            
            while(deque and deque[-1][1] >=sum_):
                deque.pop()
            
            while deque and sum_ - deque[0][1] >= K:
                result = min(i-deque[0][0], result)
                deque.popleft()
                
            deque.append([i,sum_])
        return result if result!= float(inf) else -1           
