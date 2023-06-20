'''
You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].

Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:

if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
Return the sum of integers in the matrix after all queries are applied.
'''

class Solution:
    def matrixSumQueries(self, n, queries):
        ans = 0
        rsum = 0
        csum = 0
        mpr = {}
        mpc = {}
        queries.reverse()
        
        for it in queries:
            if it[0] == 0:
                # row
                r = it[1]
                val = it[2]
                if r not in mpr:
                    rsum += 1
                    mpr[r] = val
                    ans += val * (n - csum)
            else:
                # col
                c = it[1]
                val = it[2]
                if c not in mpc:
                    csum += 1
                    mpc[c] = val
                    ans += val * (n - rsum)
        
        return ans
