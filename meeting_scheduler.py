'''
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
'''

Idea:
Instead of solving the problem in one step, it is easier to solve it in two.

Let's create a list of lists candidates that will contain intersections of slots1 and slots2.
Let's iterate over this list and see if there is an intersection wide enough to fit our duration.
How can we build candidates?
Initialize two pointers a and b to process slots1 and slots2.
An intersection is defined by the max starting point and by the min ending point.
Then move pointers accordingly.

Finally check every element in candidates.


def minAvailableDuration(slots1, slots2, duration):
    if not slots1 or not slots2: return []
    slots1 = sorted(slots1, key = lambda x:x[0])
    slots2 = sorted(slots2, key = lambda x:x[0])
    candidates, res = [], []
    a, b = 0, 0
    while a < len(slots1) and b < len(slots2):
        st = max(slots1[a][0], slots2[b][0])
        end = min(slots1[a][1], slots2[b][1])
        if st <= end:
            candidates.append([st, end])
        if slots1[a][1] < slots2[b][1]:
            a += 1
        else:
            b += 1
    if len(candidates) == 0:
        return res
    for candidate in candidates:
        if candidate[1] - candidate[0] >= duration:
            res.append(candidate[0])
            res.append(candidate[0] + duration)
            break
    return res
----------------------------------------------------------------------------

I wanted to present an alternative take on this. Line sweep can be used to solve any interval problems, but you rarely see solutions. The idea is based off the concept that at any given time, we want to check whether we can fit the duration in. This means we need to check both the ends of the overlap, and see if we can fit it in.

Time complexity: N Log N
Space: O(N), since we store 2N events, for each person. Dict is neglible, since we only have two people.


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        OPEN, CLOSE = 0, 1
        events = []
        
        # we add all intervals from person 1 and person 2, using start/end events
        for start, end in slots1:
            events.append((start, OPEN, 1, end))
            events.append((end, CLOSE, 1, end))
            
        for start, end in slots2:
            events.append((start, OPEN, 2, end))
            events.append((end, CLOSE, 2, end)) 
        
        events.sort()
        seen = {}
        
        """
            for every event, add and remove any interval, based on the open/close events we set above, to our seen dict
            this will produce a window, where at any given point, we can track if intervals overlap
            since we only have two people, we can hard code the dict keys as seen above
        """
        for time, eventType, person, end in events:
            if eventType is OPEN: # this is the start of an interval, add the person to the dict
                seen[person] = (person, end)
            else: # end of a given interval, remove this person
                del seen[person]

            # if we have an overlap, where both persons have intervals that coincide
            if len(seen) > 1:
                # grab the end values for each, since what we care about is whether at any given time point, does time + duration fit?
                person1, person1End = seen.get(1)
                person2, person2End = seen.get(2)
                
                if time + duration <= person1End and time + duration <= person2End:
                    return[time, time + duration]
            
        return []
      
--------------------------------------------------------------------
Algorithm:

Sort both the slots. Assign two pointers to both slots.
whenever start of one is between the start and end of the other, look whether the max(start of both) + duration is less than equal to minimum of end of the both. Then we have our answer.
Else, if end of slot2 is less than end of slot1, then increment the slot2 pointer because there might be a slot in slot2 which intersectes with slot1.
Time: O(MLogM + NLogN)
Space: O(1)
  
  
  class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda z: z[0])
        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(slots1) and ptr2 < len(slots2):
            
            start1, end1 = slots1[ptr1]
            start2, end2 = slots2[ptr2]
            
            if start1<=start2 < end1 or start2<=start1 < end2:
                start = max(start1, start2)
                end = start + duration
                if end <= min(end1, end2):
                    return [start, end]
            
            if end2 < end1:
                ptr2 += 1
            else:
                ptr1 += 1
        
        return []
---------------------------------------------------------------------------------------------

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        q1 = deque(sorted(slots1))
        q2 = deque(sorted(slots2))
        while q1 and q2:
            a1, a2 = q1[0]
            b1, b2 = q2[0]
            if (s := max(a1, b1)) + duration <= (e := min(a2, b2)):
                return [s, s + duration]
            if a2 < b2:
                q1.popleft()
            else:
                q2.popleft()
        return []
--------------------------------------------

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        i, j = 0, 0
        s1_len, s2_len = len(slots1), len(slots2)
        
        slots1.sort()
        slots2.sort()

        while i< s1_len and  j < s2_len:

            max_s = max(slots1[i][0], slots2[j][0])
            min_e = min(slots1[i][1], slots2[j][1])

            if min_e - max_s >= duration:
                return [max_s, max_s + duration]

            if slots2[j][1] - max_s < duration :
                j += 1

            if slots1[i][1] - max_s < duration :
                i += 1

        return []
      
      
  
