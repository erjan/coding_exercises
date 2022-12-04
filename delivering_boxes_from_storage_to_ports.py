'''
You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a limit on the number of boxes and the total weight that it can carry.

You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three integers portsCount, maxBoxes, and maxWeight.

ports​​i is the port where you need to deliver the ith box and weightsi is the weight of the ith box.
portsCount is the number of ports.
maxBoxes and maxWeight are the respective box and weight limits of the ship.
The boxes need to be delivered in the order they are given. The ship will follow these steps:

The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and maxWeight constraints.
For each loaded box in order, the ship will make a trip to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no trip is needed, and the box can immediately be delivered.
The ship then makes a return trip to storage to take more boxes from the queue.
The ship must end at storage after all the boxes have been delivered.

Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.
'''


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        dp = [0] + [inf]*len(boxes)
        trips = 2
        ii = 0
        for i in range(len(boxes)):
            maxWeight -= boxes[i][1]
            if i and boxes[i-1][0] != boxes[i][0]: trips += 1
            while maxBoxes < i - ii + 1 or maxWeight < 0 or ii < i and dp[ii] == dp[ii+1]:
                maxWeight += boxes[ii][1]
                if boxes[ii][0] != boxes[ii+1][0]: trips-=1
                ii += 1
            dp[i+1] = dp[ii] + trips
        return dp[-1] 
      
-----------------------------------------------------------------------------------------------------------------
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        left = 0  # idx of the box to be delivered first during the next run -> left idx in sliding window
        ports_on_route = 0
        weight_on_ship = 0
        dp = [0]
        for right in range(len(boxes)):
            while weight_on_ship + boxes[right][1] > maxWeight or right - left == maxBoxes:
                # ship is full --> deliver boxes until there is enough space for the new box
                weight_on_ship -= boxes[left][1]
                ports_on_route -= boxes[left][0] != boxes[left + 1][0]
                left += 1
                
            while left < right and dp[left] == dp[left + 1]:
			    # if some additional boxes can be delivered for free, deliver them as well
			    # (there can't be a cheaper than free deliveray, plus we clear additional space on the boat)
                weight_on_ship -= boxes[left][1]
                ports_on_route -= boxes[left][0] != boxes[left + 1][0]
                left += 1

            # load next box
            weight_on_ship += boxes[right][1]
            if right == 0 or boxes[right - 1][0] != boxes[right][0]:
                ports_on_route += 1
            dp.append(dp[left] + ports_on_route + 1)
            
        return dp[-1]
