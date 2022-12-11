'''
You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.
'''

# Runtime: 4264 ms
class Fenwick(object):
    def __init__(self, arr):
        self.arr = [0] + arr
        self.fen = self.arr[:]
        self.construct()
    
    def construct(self):
        for i in range(len(self.fen)):
            j = i + self.lsb(i)
            if j < len(self.fen):
                self.fen[j] += self.fen[i]
            
    def lsb(self, n):
        '''return the least significant bit of n'''
        return -n&n
    
    def presum(self, i):
        '''return sum of array from 0:i'''
        res = 0
        while i:
            res += self.fen[i]
            i -= self.lsb(i)
        return res
    
    def range_sum(self, i, j):
        '''return sum of array from i: j inclusive'''
        i, j = i+1, j+1
        return self.presum(j) - self.presum(i-1)
    
    def update(self, i, val):
        '''change value at arr[i] to val ; i.e. arr[i] = 1 if server busy and arr[i] = 0 if free'''
        i += 1
        diff = val - self.arr[i]
        self.arr[i] = val
        while i < len(self.fen):
            self.fen[i] += diff
            i += self.lsb(i)
    
    def free_server_in_range(self, i, j):
        '''returns True if there is a free server in the range [i,j] inclusive'''
        return self.range_sum(i-1, j-1) < (j - i + 1)
    
    def binary_search(self, low, high):
        '''Finds the left-most server that is free in the range low, high inclusive'''
        first_free = float('inf')
        if self.free_server_in_range(low, high):
            while low <= high:
                j = (low + high) // 2
                if self.free_server_in_range(low, j):
                    first_free = min(j, first_free)
                    high = j - 1
                else:
                    low = j + 1
        return first_free
    
    def find_first_free_server(self, i):
        '''Returns the index of the first free server to the right of server i (wrapping around to server 0 if needed)'''
        first_free = self.binary_search(i, len(self.arr) - 1)
        return (first_free - 1) if (first_free != float('inf')) else (self.binary_search(1, i-1) - 1)

    
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        if k >= len(arrival):          # If we have more servers than jobs then
            return range(len(arrival)) # the first n servers will all receive 1 job
        
        end = [a + c for a,c in zip(arrival, load)]                                  # end[i] is the time at which the (i)th job will finished
        requests_handled = collections.defaultdict(lambda: 1)                        # All servers get one job to start with
        t_naught = arrival[k]                                                        # Arrival time of the (k)th job
        free_servers = Fenwick([int(end[i] > t_naught) for i in range(k)])           # All servers that finish their job before t_naught are free
        not_in_use = set(i for i in range(k) if end[i] <= t_naught)                  # Set of servers that are free
        servers = [(arrival[i] + load[i], i) for i in range(k) if end[i] > t_naught] # active server heap (end_time, server_id)
        heapq.heapify(servers)
        
        for i in range(k, len(arrival)):
            t = arrival[i]
            e = end[i]
            i = i % k
            
            while servers and servers[0][0] <= t:  # Remove all servers that have completed their job from the server heap
                s = heapq.heappop(servers)[1]
                free_servers.update(s, 0)          # 0 means the server is now free
                not_in_use.add(s)
            
            if len(servers) < k - 1:
                target_server = free_servers.find_first_free_server(i+1) if free_servers.arr[i+1] else i
                not_in_use.remove(target_server)             # mark server as not free
                free_servers.update(target_server, 1)        # 1 means the server is now busy
                heapq.heappush(servers, (e, target_server))  # add server to server heap
                requests_handled[target_server] += 1         # Record that server handled 1 request
            elif len(servers) == k - 1:
                target_server = not_in_use.pop()             # There is only one server available to use
                free_servers.update(target_server, 1)        # mark server as busy
                heapq.heappush(servers, (e, target_server))  # add server to server heap
                requests_handled[target_server] += 1         # Record that server handled 1 request
                
        maxi = max(requests_handled.values())
        return (server for server in requests_handled if requests_handled[server] == maxi)
      
      
----------------------------------------------------------------------------------------------------------
import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # map server to its handle count
        server_busy_count = [0] * k
        
        # init heap
        busy_servers_heap = []
        
        # init available servers sortedlist -> klogk
        available_servers = SortedList([idx for idx in range(k)])
        
        # iterate arrivals
        for req_idx, (curr_arrival, curr_load) in enumerate(zip(arrival, load)):
            # pop all available servers from heap
            while busy_servers_heap and curr_arrival >= busy_servers_heap[0][0]:
                _, server_idx = heapq.heappop(busy_servers_heap)
    
                # add servers to available sorted list
                available_servers.add(server_idx)
            
            # all servers are busy -> drop request
            if not available_servers: continue
            
            # binary search on available list to find the correct available server
            desired_server_idx = req_idx % k
            next_idx = available_servers.bisect_left(desired_server_idx)
            
            # no bigger idx found, use the first available server
            if next_idx == len(available_servers):
                next_idx = 0
            
            # select server by the next_idx calculated
            selected_server = available_servers[next_idx]
            
            # increase selected server handle count
            server_busy_count[selected_server] += 1
            
            # add selected server with end time to the heap
            heapq.heappush(busy_servers_heap, (curr_arrival + curr_load, selected_server))
            
            # pop selected servers from the available list
            available_servers.remove(selected_server)
            
        # return all servers the handled the max request count
        max_busy = max(server_busy_count)
        return [idx for idx in range(k) if server_busy_count[idx] == max_busy]           
