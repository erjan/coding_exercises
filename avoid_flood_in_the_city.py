'''
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.
'''

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        pq = []
        fill = set()
        d = collections.defaultdict(list)
        ans = []
        
        for i, rain in enumerate(rains):
            d[rain].append(i)
        
        for rain in rains:
            if rain > 0:
                if rain in fill:
                    return []
                fill.add(rain)
                d[rain].pop(0)
                if d[rain]:
                    heapq.heappush(pq, d[rain][0])
                ans.append(-1)
            else:
                if pq:
                    ind = heapq.heappop(pq)
                    ans.append(rains[ind])
                    fill.remove(rains[ind])
                else:
                    ans.append(1)
        
        return ans
