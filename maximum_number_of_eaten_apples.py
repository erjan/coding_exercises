'''
There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.
'''

from heapq import heappush, heappop
class Solution:
    def eatenApples(self, A: List[int], D: List[int]) -> int:
        ans, i, N = 0, 0, len(A)
        h = []
        while i < N or h:
            # only push to heap when you have a valid i, and the apple has atleast one day to stay fresh.
            if i<N and A[i] > 0:
                heappush(h, [i+D[i], A[i]])
            # remove the rotten apples batches and the batches with no apples left (which might have got consumed).
            while h and (h[0][0] <= i or h[0][1] <= 0):
                heappop(h)
            # only if there is batch in heap after removing all the rotten ones, you can eat. else wait for the subsequent days for new apple batch by incrementing i.
            if h:
                h[0][1]-=1
                ans+=1
            i+=1
        return ans 
      
--------------------------------------------
import heapq
def eatenApples(self, A, D) -> int:
    fin, i = 0, 0
    q = []
    while i<len(A) or q:
        if i<len(A) and A[i]>0:
            heapq.heappush(q, [i+D[i],A[i]])
        while q and (q[0][0]<=i or q[0][1]==0):
            heapq.heappop(q)
        if q:
            q[0][1] -= 1
            fin += 1
        i += 1
    return fin
