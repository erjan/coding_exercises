'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
'''


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = dict()
        a = A
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]] = 1
            else:
                return a[i]
