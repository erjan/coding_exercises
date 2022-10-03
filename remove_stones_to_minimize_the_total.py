'''
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
'''



class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            cur = -heapq.heappop(heap)
            heapq.heappush(heap, -(cur-cur//2))
        return -sum(heap) 
------------------------------------------------------------------------      


def minStoneSum(self, A, k):
        A = [-a for a in A]
        heapq.heapify(A)
        for i in xrange(k):
            heapq.heapreplace(A, A[0] / 2)
        return -sum(A)
      
-----------------------------------------------------
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
		To use Max Heap, we need to convert all values to -ve  integers
		"""
		for i in range(len(piles)):
            piles[i]= -1 * piles[i]
        
		"""
		Creating heap of the given list
		"""
        heapq.heapify(piles)
        
		"""
		while k > 0, applying the provided operation
		to the maximum value
		"""
        while k:
            a = heapq.heappop(piles)
            a = a//2
            heapq.heappush(piles, a)
            k -= 1
        
		"""
		The elements in the list are updated,
		now the contain the minimum possible sum
		"""
        return abs(sum(piles))
