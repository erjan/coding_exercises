'''
On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m.

You are given an array workers of length n where workers[i] = [xi, yi] is the position of the ith worker. You are also given an array bikes of length m where bikes[j] = [xj, yj] is the position of the jth bike. All the given positions are unique.

Assign a bike to each worker. Among the available bikes and workers, we choose the (workeri, bikej) pair with the shortest Manhattan distance between each other and assign the bike to that worker.

If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. If there are multiple ways to do that, we choose the pair with the smallest bike index. Repeat this process until there are no available workers.

Return an array answer of length n, where answer[i] is the index (0-indexed) of the bike that the ith worker is assigned to.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
'''

First step: claculate distances of all (worker, bike) pairs and make a dictionary using them. Distances are the keys in this dictionay. The dictionary will look like this:
distances = {dist_val1: [[w1,b1],[w2,b3]], dist_val2: [[w0,b1],[w1,b2]], ...}
Second, start from the minimum value in the dictionary and loop through the (worker, bike) pairs for that distance, if the bike has not been assigned yet and the worker doesn't have a bike yet, assign the bike to that worker. Since we created this dictionary, going through workers and bikes in ascending order, we don't need to sort the list of each distance[k].
If n is the total number of pairs between workers and bikes, making the dictionary if of O(n). Also, worst case scenario, each entry in the dictionary belongs to one pair of worker and bike which makes filling ans to be of O(n) and the overall solution is of O(n).

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        ans = [-1]*len(workers)
        distances = collections.defaultdict(list)
        set_bikes = set()
        
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances[abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])].append([i,j])
        
        for k in sorted(distances.keys()):
            for i in range(len(distances[k])):
                if ans[distances[k][i][0]] == -1 and distances[k][i][1] not in set_bikes:
                    ans[distances[k][i][0]] = distances[k][i][1]
                    set_bikes.add(distances[k][i][1])
                
        
        return ans
----------------------------------------

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distance = []
        for i, w in enumerate(workers):
            distance.append([])
            for j, b in enumerate(bikes):
                distance[-1].append([abs(w[0]-b[0]) + abs(w[1]-b[1]), i, j])
            heapq.heapify(distance[-1])
        ans = [-1] * len(workers)
        used_bikes = set()
        heap = [heapq.heappop(d) for d in distance]
        heapq.heapify(heap)
        while len(used_bikes) < len(workers):
            _, w, b = heapq.heappop(heap)
            if b in used_bikes:
                heapq.heappush(heap, heapq.heappop(distance[w]))
            else:
                used_bikes.add(b)
                ans[w] = b
        return ans 
-------------------------------------------------

Create N list of heaps with distances (row[i]-> worker[i] to bikes distances)
Create additional heap of N closest paths: for each worker pop min distance from heap (step1) and put it to closest paths heap.
Create dict worker idx = bike idx + set of bike in use
Loop through closest paths heap while all workes have bikes:
if bike is not in use and worker doesn't have a bike -> assign bike to worker
else pop next element from worker[i] to distance heaps (from step1)
Output
Runtime: 568 ms, faster than 98.62% of Python3 online submissions for Campus Bikes.
Memory Usage: 146.2 MB, less than 100.00% of Python3 online submissions for Campus Bikes.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        distances = [None for _ in range(len(workers))]

        for w, w_cords in enumerate(workers):
            queue = []
            for b, b_cords in enumerate(bikes):
                distance = abs(w_cords[0] - b_cords[0]) + abs(w_cords[1] - b_cords[1])
                queue.append((distance, w, b))
            heapq.heapify(queue)
            distances[w] = queue

        worker_to_bike = {}
        used_bikes = set()
        closest_paths = [heapq.heappop(distance) for distance in distances]
        heapq.heapify(closest_paths)

        while len(used_bikes) < len(workers):
            distance, w, b = heapq.heappop(closest_paths)
            if w not in worker_to_bike and b not in used_bikes:
                worker_to_bike[w] = b
                used_bikes.add(b)
            else:
                heapq.heappush(closest_paths, heapq.heappop(distances[w]))

        return [worker_to_bike[b] for b in sorted(worker_to_bike)]

---------------------------------------------------------------------------------------

class Solution(object):
    def assignBikes(self, workers, bikes):
        
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])
        
        
        N = len(workers)
        M = len(bikes)
        distances = []
        
        for i in range(N):
            for j in range(M):
                distances.append((dist(workers[i], bikes[j]), i, j))
                
        distances.sort()        
        assigned = set()
        
        result = {}
        for dist, worker, bike in distances:
            if bike not in assigned:
                if worker not in result:
                    result[worker] = bike
                    assigned.add(bike)
            
        result = {k: result[k] for k in sorted(result)}        
        return result.values()
-------------------------------------------------------------------------------------

First we build the heap by pairing each worker with the closest bike through closest_bike, and added to a min heap. (the same bike may be paired with the same worker)

Then we go through the min heap with a while loop:

Bike has not been paired: we assign the worker to the bike through assignment[w_id] = b_id. We then add the bike id b_id to the set seen and delete the b_id from the available bikes pool del bikes[b_id]. This ensures that the bike will not be paired again to another worker and any future calls to closest_bike will not take into consideration the current b_id.

Bike has already been paired: to a worker b_id in seen we call closest_bike again to find the next closest bike to the worker and add it to the heap.

This continues until every worker is assigned a bike.

from heapq import *

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def closest_bike(w_row, w_col):
            min_distance = 2001
            min_b_id = None
            
            for b_id, (b_row, b_col) in bikes.items():
                distance = abs(w_row - b_row) + abs(w_col - b_col)
                
                if distance < min_distance:
                    min_distance = distance
                    min_b_id = b_id
                    
            return min_distance, min_b_id
        
        bikes = dict(enumerate(bikes))
        seen = set()
        assignment = [None] * len(workers)
        heap = []
        
        for w_id, (w_row, w_col) in enumerate(workers):
            distance, b_id = closest_bike(w_row, w_col)
            heappush(heap, (distance, w_id, b_id))
            
        while len(seen) < len(workers):
            _, w_id, b_id = heappop(heap)
            
            if b_id in seen:
                w_row, w_col = workers[w_id]
                distance, b_id = closest_bike(w_row, w_col)
                heappush(heap, (distance, w_id, b_id))
                
            else:
                assignment[w_id] = b_id
                seen.add(b_id)
                del bikes[b_id]
                
        return assignment
      
      
      
      
      
      
