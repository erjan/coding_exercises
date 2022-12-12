'''
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.
'''

class Solution:
    def mostBooked(self, n, A):
        rooms = [0] * n
        A.sort()
        heap = []
        avail = [i for i in range(n)]

        for [i, j] in A:
            while heap and heap[0][0] <= i:
                heapq.heappush(avail, heapq.heappop(heap)[1])

            if not avail:
                [k, idx] = heapq.heappop(heap)
                i, j = k, j + k - i
                heapq.heappush(avail, idx)
                    
            ready = heapq.heappop(avail)
            heapq.heappush(heap, [j, ready])
            rooms[ready] += 1

        return rooms.index(max(rooms))
      
--------------------------------------------------------------------------------
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        currentMeetHeap = []
        numOfMeet = n * [0]
        currentMeet = n * [False]
        meetings.sort()
        
        # Removes ended meetings from the heap.
        def clearEnded(cutoff): 
            while len(currentMeetHeap)>0 and cutoff>=currentMeetHeap[0][0]:
                ended = heapq.heappop(currentMeetHeap)
                currentMeet[ended[1]] = False
            
        def addMeeting(room, end):
            currentMeet[room] = True
            numOfMeet[room] += 1
            heapq.heappush(currentMeetHeap, [end,room])
        
        def getFirstMax():
            maxMeet = 0
            maxMeetRoom = 0
            for i in range(len(numOfMeet)): 
                meets = numOfMeet[i]
                if meets > maxMeet: 
                    maxMeet = meets
                    maxMeetRoom = i
            return maxMeetRoom
            
            
        for meeting in meetings:
            # First check if theres any empty rooms at the start of the current meeting.
            # If so, use this room.
            clearEnded(meeting[0])
            added = False
            for i in range(n):
                if not currentMeet[i]:
                    addMeeting(i, meeting[1])
                    added = True
                    break
            if (added):
                continue
				
            # If no meeting rooms initially available, pull a meeting from the heap. 
            # We need to adjust the end time to account for the wait. 
            firstAvailable = heapq.heappop(currentMeetHeap)
            addMeeting(firstAvailable[1], meeting[1]+(firstAvailable[0]-meeting[0]))
        
        return getFirstMax()
