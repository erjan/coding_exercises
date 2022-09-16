'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)
      
-------------------------------------------------------------------

The pattern:

Many greedy problems require sorting and processing things in order while checking if the current item overlaps/dissolves into its predecessor (the previous item).

This is usually needed to determine the most optimimum (max/min) number of something (for example a resource, as in how many rooms needed given this timeline of meetings). Usually the problem gives us criteria upon which we can group some of these items. The grouping/clustering nature is what allows us to obtain the optimum result (for ex: the minimum number of rooms needed, or the the number of fleets)

This problem fits the pattern of what I like to call "allocating resources to overlapping events"

In this kind of problems, its usually the case that you have to sort the items with respect to some feature and process them one at at time while constantly checking the previous items by popping from a stack.

Problems that follow a somewhat simialr pattern:

Merge Intervals
Non-overlapping Intervals
Minimum Number of Arrows to Burst Balloons
Meeting Rooms
Meeting Rooms II
My Calendar I
My Calendar II
My Calendar III (Meeting rooms II)
Course Schedule III
Car Pooling (Meeting Rooms II with a twist)
.
.
Sketches:
image
..
image

Code:
inspired by @infinute

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
 
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: (x[0], x[1]), reverse=True) # desc order : closer to traget comes first
        stack = []
        for x, v in cars:
            dist = target - x # remaning distance to tagret
            if not stack:
                stack.append(dist/v) # arrivalTime = dist/v
            elif dist/v > stack[-1]: # car arrives late -> thus does not join previous fleet and forms its own fleet
                stack.append(dist/v)
            # if curr arrivalTime is <= prev arrivalTime -> then curr car joins prev fleet and gets discolved into it (aka we don't need to do anything)
        return len(stack)
      
      
---------------------------------------------------------------------------------
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the time will be collected to 'time' array, 
		# but first let's put the dist and speed to keep track of correct speed for dist
		# after we sort
        time = []
        
        for i in range(len(position)):
            time.append((position[i], speed[i]))
        time.sort(key=lambda x: x[0])
    
        # let's calculate the time keeping the decimal points in place
        for idx, distSpeed in enumerate(time):
            time[idx] = float(target - distSpeed[0]) / distSpeed[1]
        
        # We know that if the car behind takes more time to reach the target
        # then, that means the two car is separated, so we will increase the fleet count
        fleetCount = 0
        
        # fleetLeaderTime represent, whenever we find new fleet,
        # we want every car in the fleet to take less time than the
        # head(lead) of the fleet's time taken
        fleetLeaderTime = 0
        
        for i in range(len(time) - 1, -1, -1):
            curr = time[i]
            # if currCar's time need to achieve the target is less than
            # the head of fleet, then the car is part of the fleet
            # otherwise, we found separate fleet, so increment, and update the
            # 'fleetLeaderTime'
            if curr > fleetLeaderTime:
                fleetCount += 1
                fleetLeaderTime = curr
        
        return fleetCount
