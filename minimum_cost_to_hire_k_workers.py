'''
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    def mincostToHireWorkers(self, Q, W, K):
        ans, csum, H = float('inf'), 0, []
        for q, w in sorted(zip(Q, W), key = lambda x: x[1] / x[0]):
            csum += q
            heapq.heappush(H, -q)
            if len(H) > K: csum += heapq.heappop(H)
            if len(H) == K: ans = min(ans, csum * w / q)
        return ans
      
---------------------------------------------------------------------------
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(wage)
        arr=[[wage[i]/quality[i],quality[i]] for i in range(n)]
        arr.sort(key=lambda x:x[0])
        kSmallest=0
        pq=[]
        for i in range(k):
            heapq.heappush(pq,-arr[i][1])
            kSmallest+=arr[i][1]
        minCost=arr[k-1][0]*kSmallest
        for c in range(k,n):
            if pq and abs(pq[0])>arr[c][1]:
                qRem=-heappop(pq)
                kSmallest-=qRem
                kSmallest+=arr[c][1]
                heappush(pq,-arr[c][1])
            minCost=min(minCost,arr[c][0]*kSmallest)
        return minCost
-----------------------------------------------------------

        
        
