'''
Write an efficient algorithm that searches for a value target in an m x n 
integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

#solved it myself!

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        onelist = list()
        m = matrix
        for i in range(len(m)):
            row = m[i]

            onelist.extend(row)


        hi = len(onelist)
        lo = 0

        while lo < hi:
            mid = (hi+lo)//2

            midval = onelist[mid]
            if midval < target:
                lo = mid+1
            elif midval > target:
                hi = mid
            else:
                return True
        return False
