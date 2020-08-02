'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
'''


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = dict()
        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = 1
            else:
                return A[i]
