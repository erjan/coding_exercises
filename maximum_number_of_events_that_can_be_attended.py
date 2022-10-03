'''
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.
'''

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(end for start, end in events)
        day = 0
        event_id = 0
        num_events_attended = 0
        min_heap = []
        
        for day in range(1, total_days+1):
            # Add all the events that start today
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1
            
            # Remove all the events whose end date was before today
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
            # if any event that can be attended today, let's attend it
            
            if  min_heap:
                heappop(min_heap)
                num_events_attended += 1
                
        return num_events_attended
