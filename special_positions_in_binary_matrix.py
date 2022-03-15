'''
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
'''


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        def check_row(mat, x, y):
            row_to_check = mat[x]

            num_zeroes = row_to_check.count(0)
            num_columns = len(mat[0])
            if num_zeroes == num_columns - 1:
                return True
            return False


        def check_columns(mat, x, y):

            column_to_check = [row[y] for row in mat]

            num_zeroes = column_to_check.count(0)
            num_rows = len(mat)

            if num_zeroes == num_rows-1:
                return True
            return False
        
        special = 0
        for i in range(len(mat)):

            for j in range(len(mat[0])):

                if mat[i][j] == 1:
                    print('----------------------------------')
                    print('need to check at %d %d' % (i, j))

                    if check_row(mat, i, j) and check_columns(mat, i, j):
                        special += 1
        print('special ', special)
        return special
