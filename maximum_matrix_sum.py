'''
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
'''

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # count -'s
        count = 0
        for row in matrix:
            for col_num in row:
                if col_num < 0:
                    count += 1
        tot_sum = sum([sum([abs(x) for x in row])
                       for row in matrix])
        if count % 2 == 0:
            return tot_sum
        else:
            min_val = min([min([abs(x) for x in row])
                       for row in matrix])
            return tot_sum - 2 * min_val
          
--------------------------------------------------------------------------
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        count_neg = 0
        total = 0
        m = math.inf
        for i in range(n):
            for j in range(n):
                total += abs(matrix[i][j])
                m=min(m,abs(matrix[i][j]))

                if matrix[i][j] < 0:
                    
                    count_neg +=1                                        
        if count_neg %2 == 0: #even neg nums
            return total
        
        elif count_neg %2 == 1:
            return total - 2*m
            
