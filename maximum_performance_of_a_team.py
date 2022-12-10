'''
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.
'''

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers, res, speed, minHeap = sorted(list(zip(efficiency, speed)), reverse = True), 0, 0, []
        for e, s in engineers:
            if len(minHeap) == k: # try next engineers
                speed -= heappop(minHeap) # get lowest speed
            speed += s # keep update of speed
            heappush(minHeap, s) # try all speed
            res = max(res, e * speed)
        return res % (10 ** 9 + 7)

        
--------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        res=[]
        for i in range(n):
            res.append([speed[i],efficiency[i]])
        res.sort(key=lambda x:x[1], reverse=True)
        speedsum,performance=0,0
        m=[]
        heapq.heapify(m)
        for i in range(len(res)):
            currspeed=res[i][0]
            curreff=res[i][1]
            while len(m)>=k:
                a=heapq.heappop(m)
                speedsum-=a
            heapq.heappush(m,currspeed)
            speedsum+=currspeed
            performance=max(performance,speedsum*curreff)
        return performance%(10**9+7)
-----------------------------------------------------------------------------------------------------------        
        
        
