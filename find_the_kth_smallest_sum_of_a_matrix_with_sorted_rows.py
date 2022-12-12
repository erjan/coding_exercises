'''
You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

You are allowed to choose exactly one element from each row to form an array.

Return the kth smallest array sum among all possible arrays.
'''


import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        
    def push(self, matrixSum, indexes):
        heapq.heappush(self._queue, (matrixSum, indexes))
        
    def pop(self) -> tuple:
        return heapq.heappop(self._queue)

    
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        queue = PriorityQueue()
        
        m = len(mat)  # row
        n = len(mat[0]) # col
        
        smallestSum = sum(mat[i][0] for i in range(0, m))
        firstColIndexes = tuple([0 for _ in range(0, m)])
        queue.push(smallestSum, firstColIndexes)
        
        
        usedIndexes = set()
        usedIndexes.add(firstColIndexes)
        
        kCount = 0
        
        while 1:
            matSum, colIndexes = queue.pop()
            kCount += 1
            
            if kCount == k:
                return matSum

            for rowIndex, colIndex in enumerate(colIndexes):
                if colIndex < n - 1:
                    colIndexesCopy = list(colIndexes)
                    colIndexesCopy[rowIndex] += 1
                    colIndexesCopy = tuple(colIndexesCopy)
                    
                    if colIndexesCopy not in usedIndexes:
                        matSum = sum(mat[row][colIndexesCopy[row]] for row in range(0, m))
                        queue.push(matSum, colIndexesCopy)
                        usedIndexes.add(colIndexesCopy)
                        
-----------------------------------------------------------------------------------------------------
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row=len(mat)
        col=len(mat[0])
        temp=[i for i in mat[0]]
        for i in range(1,row):
            currSum=[]
            for j in range(col):
                for it in range(len(temp)):
                    currSum.append(temp[it]+mat[i][j])
            currSum.sort()
            temp.clear()
            maxSize=min(k,len(currSum))
            for size in range(maxSize):
                temp.append(currSum[size])
        return temp[k-1]
