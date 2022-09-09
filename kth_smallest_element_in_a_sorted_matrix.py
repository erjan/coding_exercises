'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).
'''


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        tmp = []
        
        for r in matrix:
            tmp.extend(r)
        tmp.sort()
        
        return tmp[k-1]
-----------------------------------------------------------------------
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        N = len(matrix)
                
        def less_k(m):
            cnt = 0
            for i in range(N):
                x = bisect_right(matrix[i],m)
                cnt+=x
            return cnt
        
        while l < r:
            mid = (l+r)//2
            if less_k(mid) < k:
                l = mid+1
            else:
                r= mid
        return l
