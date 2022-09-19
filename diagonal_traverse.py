'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
'''


import collections

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        rows, col = len(matrix), len(matrix[0])

        output = []
        diag = collections.defaultdict(list)

        for row in range(rows):
            for _col in range(col):
                diag[row + _col].append(matrix[row][_col])

        for index, data in enumerate(diag.values()):
            if index % 2 ==0:
                output.extend(reversed(diag[index]))
            else:
                output.extend(diag[index])


        return output
