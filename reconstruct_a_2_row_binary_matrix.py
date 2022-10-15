'''
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.
'''


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if (upper+lower)!=sum(colsum):
            return []
        
        res=[[0 for i in range(len(colsum))] for j in range(2)]
        
        for i in range(len(colsum)):
            if colsum[i]==2:
                if upper>0 and lower>0:
                    lower-=1
                    upper-=1
                    res[0][i]=1
                    res[1][i]=1
                else:
                    return []
        for i in range(len(colsum)):
            
            if colsum[i]==1:
                
                if upper>0:
                    res[0][i]=1
                    upper-=1
                elif lower>0:
                    res[1][i]=1
                    lower-=1
                else:
                    return []
        return res
