'''
You are given a 0-indexed 2D integer array peaks where peaks[i] = [xi, yi] states that mountain i has a peak at coordinates (xi, yi). A mountain can be described as a right-angled isosceles triangle, with its base along the x-axis and a right angle at its peak. More formally, the gradients of ascending and descending the mountain are 1 and -1 respectively.

A mountain is considered visible if its peak does not lie within another mountain (including the border of other mountains).

Return the number of visible mountains.
'''


Observation: If one point A is within point B, then the entire triangle (mountain) of point A is within the triangle of point B
Below is an implementation of the hint section
Get rid of all repeat points as they won't be visible
Sort by x-axis
Once x-axis is sorted, we will use mono-stack to keep track of visible points. One point is visible if it's not covered by the last point in the mono-stack
If current point is visible
Pop all previous points that are within the current point
Append current point to the mono-stack
If current point is not visible, ignore it
See below scenarios
Scenario 1 (previous points are within the current point):
peaks = [[2,1], [3, 1], [4, 36]], note that the first 2 points are within the last point; for the mono-stack, we will only keep the last point
stack = [[2,1]]
stack = [[2,1], [3, 1]]
stack = [[4, 36]] because first two points are within [4, 36], thus they've been popped out.
Scenario 2 (current point is not visible):
peaks = [[2,10], [3, 1]], note that the 2nd point will not be included to the stack since it's within the first point
stack = [[2,10]]
stack = [[2, 10]], since [3,1] will be ignored, as it's within [2, 10]
Otherwise, we will append the current point to the mono-stack
Time: O(nlgn), n = len(peaks) due to the sorting algorithm
Implementation
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        c = collections.Counter()                           # count frequency for each point
        for x, y in peaks:
            c[(x, y)] += 1
        peaks = sorted(c.keys())                            
        if not peaks: return 0
        def within(pa, pb):                                 # return True if `pb` is within `pa`
            x1, y1 = pa
            x2, y2 = pb 
            b1 = y1 - x1
            b2 = y1 + x1
            return y2 <= x2 + b1 and y2 <= -x2 + b2
        n = len(peaks)
        stack = [tuple(peaks[0])]
        for x, y in peaks[1:]:
            while stack and within([x, y], stack[-1]):      # while previous point is `within` the current point 
                stack.pop()
            if not stack or not within(stack[-1], [x, y]):  # if current point is `within` the previous point
                stack.append((x, y))
        return len([p for p in stack if c[p] == 1])         # eliminate repeats and sort    
