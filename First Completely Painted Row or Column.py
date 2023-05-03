'''
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.
'''


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        map = {}

        for i in range(m):
            for j in range(n):
                map[mat[i][j]] = [i,j]
        
        row = [0]*m
        col = [0]*n

        for i in range(len(arr)):
            x = map[arr[i]]
            row[x[0]]+=1
            col[x[1]]+=1

            if row[x[0]] == n or col[x[1]] == m:
                return i
        return -1
