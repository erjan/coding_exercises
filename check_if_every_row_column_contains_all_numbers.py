'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
'''

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        def check_columns(mat):
            cols = get_column(mat)
            for c in cols:
                print('column ', c)
                temp = dict(collections.Counter(c))
                temp = temp.values()
                for i in temp:
                    if i != 1:
                        return False
            return True

        def get_column(mat):
            total = list()
            for i in range(len(mat)):
                l = list()
                for j in range(len(mat[0])):
                    l.append(mat[j][i])
                total.append(l)
            return total

        def check_rows(mat):
            for i in range(len(mat)):
                row = mat[i]
                print('row ', row)
                temp = dict(collections.Counter(row))
                temp = temp.values()

                for i in temp:
                    if i != 1:
                        print('bad! ', i)
                        return False
            return True
        
        mat = matrix
        res = None
        if check_rows(mat) and check_columns(mat):
            res = True
            return res
        res = False
        print(res)
        return res

