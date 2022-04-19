'''
A perfectly straight street is represented by a number line. The street has street lamp(s) on it and is represented by a 2D integer array lights. Each lights[i] = [positioni, rangei] indicates that there is a street lamp at position positioni that lights up the area from [positioni - rangei, positioni + rangei] (inclusive).

The brightness of a position p is defined as the number of street lamp that light up the position p.

Given lights, return the brightest position on the street. If there are multiple brightest positions, return the smallest one.
'''


Explanation
Sweep line probelm. Try 253. Meeting Room II if you haven't.
The brightest will be on end of a light's coverage. We only need to consider the end (left & right).
Procedures:
Take a dictionary
For left edge index, +1 on index, meaning starting from this index, light starts covering
For right edge index, -1 on index + 1, because right end is also covered by current light, the next index (index+1) won't be covered.
Iterate the sorted dictionary entries
Keep counting current covered lights and save the brightest (with largest count cur) light
Time Complexity: O(NlogN) because of sorting
Space Complexity: O(N) for saving ends of each light
Implementation
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for i, dis in lights:
            d[i-dis] += 1                             # index at left-end starts covering
            d[i+dis+1] -= 1                           # next index of right-end stops covering
        cur, max_idx, max_val = 0, -1, -sys.maxsize
        for idx, val in sorted(d.items()):            # sort by key would be sufficient
            cur += val
            if cur > max_val:                         # count maximum brightness
                max_val, max_idx = cur, idx
        return max_idx
      
------------------------------------------------------------------------------------------------------
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
		# light range array
        light_r = []
        for p,r in lights:
            light_r.append((p-r,'start'))
            light_r.append((p+r+1,'end'))
        light_r.sort(key = lambda x:x[0])
        # focus on the boundary of light range 
		
        bright = collections.defaultdict(int)
        power = 0
        for l in light_r:
            if 'start' in l:
                power += 1
            else:
                power -= 1
            bright[l[0]] = power
                
        list_bright = list(bright.values())
        list_position = list(bright.keys())
        
        max_bright = max(list_bright)
        max_bright_index = list_bright.index(max_bright)
        
        return list_position[max_bright_index]
----------------------------------------------------------------------------------------------------
Key observation:

The brightest position will be on the end of a light's coverage. Therefore, we only need to consider the ends (Kudos to @idontknoooo)
We use a min-heap to store the positions for both the left ends and right ends of each light's coverage. Specifically, we pair each left end with +1 in a tuple, and pair each right end with -1 in a tuple, and push them into the SAME min-heap. We then take the minimum position from the heap and update brightness by adding the corresponding +1/-1 to keep track of the number of ongoing intervals at each position. We also use maxBright to keep track he the brightest position on the street, which is the desired output of this problem.

One subtlety in this problem is that if we encounter ties with respect to the positions in the min-heap, we need to perform "+1" (left end) first before "-1" (right end) in order to obtain the maximum brightness. This is because the right end of a light is also considered as covered for that position. Therefore, we extend the tuple from (position, +1) and (position, -1) to (position, 'L', +1) and (position, 'R', -1), respectively, since 'L' appears lexicologically ahead of 'R'.

Time complexity O(n log n), space complexity O(n).
This approach can be easily generalized to interval-type of problems, e.g. LC 253 (Meeting Rooms II) and LC 1094 (Car Pooling).
Please upvote if you find this solution helpful.

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # Heap solution (equivalent to sorting), time complexity O(nlogn), space complexity O(n)
        heap = []
        for light in lights:
            heappush(heap, (light[0] - light[1], 'L', 1))
            heappush(heap, (light[0] + light[1], 'R', -1))
        brightness = 0
        maxBright = 0
        while heap:
            brightness += heap[0][2]
            if brightness > maxBright:
                maxBright = brightness
                position = heap[0][0]
            heappop(heap)
        return position
Below is an equivalent solution based on sorted array.

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # Sorting solution, time complexity O(nlogn), space complexity O(n)
        arr = []
        for light in lights:
            arr.append((light[0] - light[1], 1))
            arr.append((light[0] + light[1], -1))
        arr.sort(key=lambda x: (x[0], -x[1]))
        brightness = 0
        maxBright = 0
        for i in range(len(arr)):
            brightness += arr[i][1]
            if brightness > maxBright:
                maxBright = brightness
                position = arr[i][0]
        return position
      
---------------------------------------------------------------------------------
The same with 253 meeting rooms II: https://leetcode.com/problems/meeting-rooms-ii/
Convert each light to [startpos,endpos], separate them, then sort startpos list and endpos list.
Then use line sweep, use pointer p1 point to startpos, val = sq[p1] is the left border of a light, plus one to "current light strength".
Then check if this position (val) is already outside of a previous light right border eq[p2]. If yes, then minus one from current light strength, move pointer2 to the next rightborder; if not, then ignore this part. Find the maxval and maxidx.
'''

    sq,eq = [],[]
    for mid,rad in lights:
        sq.append(mid-rad)
        eq.append(mid+rad)
    sq.sort()
    eq.sort()
    p1,p2 = 0,0
    cur = 0
    maxval = 0
    while p1<len(sq):
        val1 = sq[p1]
        cur += 1
        if(val1>eq[p2]):
            cur -= 1
            p2 += 1
        if cur>maxval:
            maxval = cur
            maxidx = sq[p1]
        p1 += 1
    return maxidx
--------------------------------------------------------------------------------
Heap schedule solution:

def brightestPosition(lights: List[List[int]]) -> int:
    ll = sorted([(p - r, p + r) for p, r in lights], key=lambda x: x[0])
    max_brightness, pos, heap = 1, ll[0][0], []
    heapq.heappush(heap, ll[0][1])

    for start, end in ll[1:]:
        if start <= heap[0]:
            heapq.heappush(heap, end)
        else:
            heapq.heappushpop(heap, end)

        if max_brightness < len(heap):
            pos = start
            max_brightness = len(heap)

    return pos
Hash map solution:

def brightestPosition(lights: List[List[int]]) -> int:
    light_diff = defaultdict(int)

    for pos, rng in lights:
        light_diff[pos - rng] += 1
        light_diff[pos + rng + 1] -= 1

    current_brightness = max_brightness = 0
    min_pos = math.inf

    for pos in sorted(light_diff.keys()):
        current_brightness += light_diff[pos]
        if current_brightness > max_brightness:
            max_brightness, min_pos = current_brightness, pos

    return min_pos
    
      
      
