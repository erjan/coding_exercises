'''
You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.

You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.

When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.

More formally when a bus arrives, either:

If capacity or fewer passengers are waiting for a bus, they will all get on the bus, or
The capacity passengers with the earliest arrival times will get on the bus.
Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.

Note: The arrays buses and passengers are not necessarily sorted.
'''

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        cur = 0

        for time in sorted(buses):
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        best = time if cap > 0 else passengers[cur - 1]

        passengers = set(passengers)
        while best in passengers:
            best -= 1
        return best
      
----------------------------------------------------------------------------------------
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        np=0                                                             #maintains the index of next passenger
        for b in buses:
            last=False                                                   #bus is not initially full so last is intialized with False
            cb=capacity
            while cb!=0 and np<len(passengers) and passengers[np]<=b:    #for every bus fill passengers in it till conditions are satisfied
                np+=1
                cb-=1
            if cb==0:                                                    #when capacity is full last becomes true
                last=True
            
        if last==True:                                      #if last is true means all buses are full so take time of last passenger encounterd
            avail=passengers[np-1]
        else:                                               #if last is full means some buses have capacity left. So come as late as possible
            avail=buses[-1]
            
        for i in range(avail,0,-1):                         #from avail iterate backwards till first available time encounters
            if not i in passengers:
                return i
