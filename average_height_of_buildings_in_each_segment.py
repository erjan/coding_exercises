'''
A perfectly straight street is represented by a number line. The street has building(s) on it and is represented by a 2D integer array buildings, where buildings[i] = [starti, endi, heighti]. This means that there is a building with heighti in the half-closed segment [starti, endi).

You want to describe the heights of the buildings on the street with the minimum number of non-overlapping segments. The street can be represented by the 2D integer array street where street[j] = [leftj, rightj, averagej] describes a half-closed segment [leftj, rightj) of the road where the average heights of the buildings in the segment is averagej.

For example, if buildings = [[1,5,2],[3,10,4]], the street could be represented by street = [[1,3,2],[3,5,3],[5,10,4]] because:
From 1 to 3, there is only the first building with an average height of 2 / 1 = 2.
From 3 to 5, both the first and the second building are there with an average height of (2+4) / 2 = 3.
From 5 to 10, there is only the second building with an average height of 4 / 1 = 4.
Given buildings, return the 2D integer array street as described above (excluding any areas of the street where there are no buldings). You may return the array in any order.

The average of n elements is the sum of the n elements divided (integer division) by n.

A half-closed segment [a, b) is the section of the number line between points a and b including point a and not including point b.
'''


Explanation
This question is a variation of the typical sweep line question like 253. Meeting Rooms II.
I would recommend to try out 253. Meeting Rooms II first, as the intuition of my solution is coming from the second official solution of it.
Please see more explanation with the code comments below
Time: O(NlogN) because of sorting
Space: O(N) due to the use of entries
Implementation
class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        entries = []
        for s, e, h in buildings:                                # sweep line build
            entries.append((s, h))                               # positive height `h` means starting block of a building
            entries.append((e, -h))                              # negative height `-h` means ending block of a building
        entries.sort()                                           # sort
        entries.append([0, 0])                                   # add a dummy last node for edge case
        n, ans = len(entries), []
        prev, prev_idx = None, None                              # prev: previous average, prev_idx: lower bound index with same average
        i = cur = cnt = 0                                        # i: index of `entries`, cur: prefix sum to `i`, cnt: number of buildings
        while i < n-1:
            while i < n-1 and entries[i][0] == entries[i+1][0]:  # keep reading info at the same index
                idx, h = entries[i]
                cnt += 1 if h > 0 else -1                        # cnt number of building
                cur += h                                         # prefix sum
                i += 1
            else:                                                # always read one step when either (after while loop) or (never going in the while loop)
                idx, h = entries[i]
                cnt += 1 if h > 0 else -1
                cur += h
                i += 1
            if not cnt:                                          # cnt can be `0` when leaving all visited building, e.g. [[1,2,1],[5,6,1]]
                ans.append([prev_idx, idx, prev])                # thus, we will append segment here
                prev = prev_idx = None                           # since we will be starting a new segment, we need to set `prev` and `prev_idx` to None, like the initial condition
                continue                                         # no need going any further when `cnt == 0`
            avg = cur // cnt                                     # calculate average 
            if prev != avg:                                      # when prev != avg, meaning building height differs, we need to record a segment
                if prev:                                         # only if `prev` is not None, to handle scenarios like `prev = None, avg = 1`
                    ans.append([prev_idx, idx, prev])
                prev, prev_idx = avg, idx                        # update `prev` and `prev_idx`
        return ans       
      
------------------------------------------------


The Big Idea: Maintain two pointers into sorted lists of the start and endpoints of the buildings as we move left to right down the 'street'. Merge adjacent segments with the same average height and add new segments as we go.

class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:

        B = len(buildings)
        starts = sorted((s, h) for (s, _, h) in buildings)    
        ends = sorted((e, -h) for (_, e, h) in buildings)
        sp = 0
        ep = 0
        street = []
        seg_start = -1
        total_height = 0
        bldgs = 0
        
        while sp < B:
            
            if starts[sp][0] < ends[ep][0]:
                
                (point, height) = starts[sp]
                sp += 1
                
                if bldgs and point > seg_start:
                    
                    avg = total_height // bldgs
                    
                    if (street and 
                        street[-1][1] == seg_start and 
                        street[-1][2] == avg):
                        street[-1][1] = point
                    else:
                        street.append([seg_start, point, avg])
                    
                bldgs += 1
                
            else:
                
                (point, height) = ends[ep]
                ep += 1
                
                if point > seg_start:
                    
                    avg = total_height // bldgs
                    
                    if (street and 
                        street[-1][1] == seg_start and 
                        street[-1][2] == avg):
                        street[-1][1] = point
                    else:
                        street.append([seg_start, point, avg])
                    
                bldgs -= 1    

            seg_start = point
            total_height += height
        
        # Drain the endpoints list
        
        while ep < B:
            
            (point, height) = ends[ep]
            ep += 1

            if point > seg_start:

                avg = total_height // bldgs

                if (street and 
                    street[-1][1] == seg_start and 
                    street[-1][2] == avg):
                    street[-1][1] = point
                else:
                    street.append([seg_start, point, avg])

            bldgs -= 1    
            seg_start = point
            total_height += height
            
        return street
---------------------------------------------------------------


The algorithm has 3 steps:

Put the lines into a heap
Sweep through the lines and calculate average heights on the fly
Merge the buildings attached to each other if their average heights are the same
class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
		# Step 1
        START, END = 1, 0
        heap = []
        for start, end, height in buildings:
            heap.extend(((start, START, height), (end, END, height)))
        heapq.heapify(heap)
		# Step 2
        res = []
        start, height = -1, 0
        count = 0 # number of overlapped buildings
        while heap:
            line, kind, h = heapq.heappop(heap)
            if kind == START:
                if count > 0 and line > start:
                    res.append((start, line, height // count))
                start = line
                height += h
                count += 1
            else:
                if line > start:
                    res.append((start, line, height // count))
                start = line
                count -= 1    
                height -= h
		# Step 3
        merged = []
		START, END, HEIGHT = 0, 1, 2
        for start, end, height in res:
			if merged and start == merged[-1][END] and height == merged[-1][HEIGHT]:
				merged[-1][HEIGHT] = end
            else:
                merged.append([start, end, height])
        return merged
----------------------------------------------------------

class Solution:
    def averageHeightOfBuildings(self, a: List[List[int]]) -> List[List[int]]:
        
        # cast events to deltas against the total_height & total_count
        events = defaultdict(lambda: [0, 0])
        
        for s,e,h in a:
            events[s] = list(map(add, events[s], [h, 1]))
            events[e] = list(map(add, events[e], [-h, -1]))
        
        events = dict(sorted(events.items()))
        
        
        def average_height(tot, cnt):
            if cnt == 0:
                return 0
            else:
                return tot // cnt
        
        ret = []
        
        # current average height
        tot = 0
        cnt = 0
        pos = -inf
        
        for POS,(dt, dc) in events.items():
            
            TOT = tot + dt
            CNT = cnt + dc
            
            h = average_height(tot, cnt)
            H = average_height(TOT, CNT)
            
            # end of segment
            if h != H:
                
                # mute zero height segments
                if h != 0:
                    ret.append([pos, POS, h])
                
                pos = POS
            
            tot = TOT
            cnt = CNT
        
        return ret
      
      

      
