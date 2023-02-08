'''
There are k workers who want to move n boxes from an old warehouse to a new one. You are given the two integers n and k, and a 2D integer array time of size k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].

The warehouses are separated by a river and connected by a bridge. The old warehouse is on the right bank of the river, and the new warehouse is on the left bank of the river. Initially, all k workers are waiting on the left side of the bridge. To move the boxes, the ith worker (0-indexed) can :

Cross the bridge from the left bank (new warehouse) to the right bank (old warehouse) in leftToRighti minutes.
Pick a box from the old warehouse and return to the bridge in pickOldi minutes. Different workers can pick up their boxes simultaneously.
Cross the bridge from the right bank (old warehouse) to the left bank (new warehouse) in rightToLefti minutes.
Put the box in the new warehouse and return to the bridge in putNewi minutes. Different workers can put their boxes simultaneously.
A worker i is less efficient than a worker j if either condition is met:

leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j
The following rules regulate the movement of the workers through the bridge :

If a worker x reaches the bridge while another worker y is crossing the bridge, x waits at their side of the bridge.
If the bridge is free, the worker waiting on the right side of the bridge gets to cross the bridge. If more than one worker is waiting on the right side, the one with the lowest efficiency crosses first.
If the bridge is free and no worker is waiting on the right side, and at least one box remains at the old warehouse, the worker on the left side of the river gets to cross the bridge. If more than one worker is waiting on the left side, the one with the lowest efficiency crosses first.
Return the instance of time at which the last worker reaches the left bank of the river after all n boxes have been put in the new warehouse.
'''


Intuition/Ideas
Simulate with 3 queues:

Time-series queue (based on timestamp)
Bridge left and right side waiting queue (based on their efficiency)
Define 4 events

waitL: complete putNew and join bridge left side queue
waitR: complete pickOld and join bridge right side queue
reachL: complete rightToLeft and start putNew
reachR: complete leftToRight and start pick old
Process each event accordingly, needs to be careful that when processing the time series, we need to process all the events happened at the same timestamp at once.

Code
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        priority = [(time[i][0] + time[i][2], i) for i in range(k)]
        priority.sort()
        efficiency = [0] * k
        for i in range(k):
            efficiency[priority[i][1]] = -i
        
        left_queue, right_queue = [], []
        for i in range(k):
            heappush(left_queue, (efficiency[i], i))
        
        # Events: "waitL, waitR, reachL, reachR"
        time_series = []
        collected_box = [0, 0] # pending_box, total_box counts
        occupied = False
        timing = 0
                
        def process_bridge(timing):
            occupied = True
            if right_queue:
                _, worker = heappop(right_queue)
                heappush(time_series, (timing + time[worker][2], 2, worker))
            elif left_queue and collected_box[0] < n:
                collected_box[0] += 1
                _, worker = heappop(left_queue)
                heappush(time_series, (timing + time[worker][0], 3, worker))
            else:
                occupied = False
            return occupied
                
        def process_time_series(timing, events, worker, occupied):
            # print(timing, "waitL, waitR, reachL, reachR".split(', ')[events], worker)
            if events == 0:
                heappush(left_queue, (efficiency[worker], worker))
            elif events == 1:
                heappush(right_queue, (efficiency[worker], worker))
            elif events == 2:
                collected_box[1] += 1
                if collected_box[1] == n:
                    return True, occupied
                heappush(time_series, (timing + time[worker][3], 0, worker))
            else:
                heappush(time_series, (timing + time[worker][1], 1, worker))
            if events >= 2:
                occupied = process_bridge(timing)
            return False, occupied
        
        while True:
            if not occupied:
                occupied = process_bridge(timing)

            if time_series:
                timing, events, worker = heappop(time_series)
                complete, occupied = process_time_series(timing, events, worker, occupied)
                if complete:
                    return timing
                while time_series:
                    ctiming, events, worker = heappop(time_series)
                    if ctiming == timing:
                        complete, occupied = process_time_series(timing, events, worker, occupied)
                        if complete:
                            return timing
                    else:
                        heappush(time_series, (ctiming, events, worker))
                        break
            
        return -1
