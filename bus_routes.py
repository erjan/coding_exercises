'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
'''


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        adj = collections.defaultdict(list)
        for bus, route in enumerate(routes):
            for j in range(len(route)):
                adj[route[j]].append(bus)
            # if len(route) > 1:
            #     for j in range(len(route)):
            #         if j < len(route) - 1:
            #             adj[route[j]].append((route[j+1], bus))
            #         else:
            #             adj[route[j]].append((route[0], bus))

        sourceQueue = [] 
        targetQueue = []
        sourceBus = set()
        targetBus = set()
        
        for bus in adj[source]:
            sourceQueue.append(bus)
            sourceBus.add(bus)
        for bus in adj[target]:
            targetQueue.append(bus)
            targetBus.add(bus) 
        
        if len(sourceBus.intersection(targetBus)) > 0 :
            return 1

        count = 1
        while(sourceQueue or targetQueue):
            if sourceQueue:
                for i in range(len(sourceQueue)):
                    bus = sourceQueue.pop(0)
                    for stop in routes[bus]:
                        for busOfStop in adj[stop]:
                            if busOfStop not in sourceBus:
                                sourceQueue.append(busOfStop)
                                sourceBus.add(busOfStop)
                                if busOfStop in targetBus:
                                    return count + 1
                count += 1

            if targetQueue:
                for i in range(len(targetQueue)):
                    bus = targetQueue.pop(0)
                    for stop in routes[bus]:
                        for busOfStop in adj[stop]:
                            if busOfStop not in targetBus:
                                targetQueue.append(busOfStop)
                                targetBus.add(busOfStop)
                                if busOfStop in sourceBus:
                                    return count + 1
                count += 1
        return -1
---------------------------------------------------------------------------------------------------
        

            
          
