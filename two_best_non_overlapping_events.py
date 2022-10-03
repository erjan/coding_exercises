'''
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.
'''


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def binarySearch(low, high, key):
            if low <= high:
                mid = (low+high)//2
                if events[mid][1] >= key:
                    return binarySearch(low, mid-1, key)
                else:
                    return binarySearch(mid+1, high, key)
            return high
        
        events.sort(key=lambda x: x[1])
        dp = [0 for _ in range(len(events))]
        dp[0] = events[0][2]
        for i in range(1, len(events)):
            dp[i] = max(dp[i-1], events[i][2]) # maximum values if only one selection was allowed         
        
        maxi = events[0][2]
        
        for i in range(1, len(events)):
            cur = events[i][2]
            prev =  binarySearch(0, len(events), events[i][0]) # previos non-overlapping index
            maxi = max(maxi, cur+dp[prev]) if prev != -1 else max(maxi, cur)
        return maxi
      
-----------------------------------------------
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        heap = []; events.sort()
        result, maxVal = 0, 0
        for i in range(len(events)):
            while heap and heap[0][0] < events[i][0]:
                maxVal = max(maxVal, heappop(heap)[1])
            result = max(result, maxVal + events[i][2])
            heappush(heap, (events[i][1], events[i][2]))
        return result
      
----------------------------------------------------------------
class Solution(object):
    def maxTwoEvents(self, events):
        events.sort()
        heap=[]
        heappush(heap,events[0][1:3])
        maximum,ans=0,0
        
        for event in events:
            ans=max(ans, event[2])
                
        for event in events[1:]:           
            while heap and heap[0][0]<event[0]:
                maximum=max(maximum, heap[0][1])
                heappop(heap)            
            ans=max(ans,maximum+event[2])                
            heappush(heap,event[1:3])                       
        return ans
