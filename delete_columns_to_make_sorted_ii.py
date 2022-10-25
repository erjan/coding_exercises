'''
You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.
'''


    def minDeletionSize(self, A):
        res, n, m = 0, len(A), len(A[0])
        is_sorted = [0] * (n - 1)
        for j in range(m):
            is_sorted2 = is_sorted[:]
            for i in range(n - 1):
                if A[i][j] > A[i + 1][j] and is_sorted[i] == 0:
                    res += 1
                    break
                is_sorted2[i] |= A[i][j] < A[i + 1][j]
            else:
                is_sorted = is_sorted2
        return res
      
      
