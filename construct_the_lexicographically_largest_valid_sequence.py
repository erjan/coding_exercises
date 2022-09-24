'''
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 
 '''

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
            m = 2*n-1
            A, V = [0] * m, [False] * (n+1)
            def dfs(i):
                if i == m:
                    return all(A)
                if A[i]:
                    return dfs(i+1)
                for x in range(n, 0, -1):
                    j = i if x == 1 else i+x    # This is only to combine some lines of code.
                    if not V[x] and j < m and not A[j]:
                        A[i], A[j], V[x] = x, x, True
                        if dfs(i+1):
                            return True
                        A[i], A[j], V[x] = 0, 0, False
                return False
            dfs(0)
            return A
