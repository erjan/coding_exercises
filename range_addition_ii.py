'''
You are given an m x n matrix M initialized with all 0's and an array of operations ops, 
where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations.
'''


#TLE solution!!

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        glob_l = list()

        for i in range(m):
            cur_list = list()
            for j in range(n):
                cur_list.append(0)
            glob_l.append(cur_list)

        m = glob_l

        for i in range(len(ops)):

            operation = ops[i]

            x = operation[0]
            y = operation[1]

            for j in range(x):
                for q in range(y):
                    m[j][q] += 1

        maxi = 0
        c = 0

        print(m)
        m1 = len(m)
        n1 = len(m[0])


        for i in range(m1):
            for j in range(n1):

                if m[i][j] >= maxi:
                    maxi = m[i][j]
                    c += 1
        print(c)
        return c
