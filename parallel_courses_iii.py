'''
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:

You may start taking a course at any time if the prerequisites are met.
Any number of courses can be taken at the same time.
Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).
'''

from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqGraph = defaultdict(list)

        timeCompleted = (n + 1) * [0]

        time = [0] + time

        for prevCourse, nextCourse in relations:
            prereqGraph[nextCourse].append(prevCourse)
            
        def dfs(src):
            if timeCompleted[src] > 0:
                return timeCompleted[src]
            
            timeCompleted[src] = 0

            for nxt in prereqGraph[src]:
                if timeCompleted[nxt] == 0:
                    dfs(nxt)
                
                timeCompleted[src] = max(timeCompleted[src], timeCompleted[nxt])
            
            timeCompleted[src] += time[src]
        

        for src in range(1, n + 1):
            if timeCompleted[src] == 0:
                dfs(src)
        
        
        return max(timeCompleted)
      
------------------------------------------------------------------------------------
import heapq
from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        pre=[0 for i in range(n+1)]
        T=[0 for i in range(n+1)]
        D=defaultdict(list)
        for i in relations:
            D[i[0]].append(i[1])
            pre[i[1]]+=1

        stc=[]
        heapq.heapify(stc)
        for i in range(1,n+1):
            if pre[i]==0:
                heapq.heappush(stc,i)
        maxx=-1
        while stc:
            k=stc.pop()
            T[k]+=time[k-1]
            maxx=max(maxx,T[k])
            for j in D[k]:
                pre[j]-=1
                T[j]=max(T[j],T[k])
                if pre[j]==0:
                    heapq.heappush(stc,j)
        return maxx
