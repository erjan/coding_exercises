'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
'''

from collections import OrderedDict
class LFUCache:

	def __init__(self, capacity: int):
		self.frequency = OrderedDict()
		self.dict = OrderedDict()
		self.capacity = capacity
		self.small = -1

	def get(self, key: int) -> int:
		if key in self.dict:
			frequency = self.dict[key]
			self.dict[key] += 1
			value = self.frequency[frequency][key]
			del self.frequency[frequency][key]
			if frequency + 1 not in self.frequency:
				self.frequency[frequency+1] = OrderedDict()
			self.frequency[frequency+1][key] = value
			self.frequency[frequency+1].move_to_end(key)
			if frequency == self.small and len(self.frequency[self.small]) == 0:
				self.small = frequency + 1
			return value
		else:
			return -1

	def put(self, key: int, value: int) -> None:
		if key not in self.dict:
			if self.capacity > 0:
				self.dict[key] = 1
				if 1 not in self.frequency:
					self.frequency[1] = OrderedDict()
				self.frequency[1][key] = value
				self.capacity -= 1
				self.small = 1
			else:
				if self.small != -1: 
					temp = self.frequency[self.small].popitem(last=False)
					del self.dict[temp[0]]
					self.small = 1
					self.dict[key] = 1
					if 1 not in self.frequency:
						self.frequency[1] = OrderedDict()
					self.frequency[1][key] = value
		else:
			frequency = self.dict[key]
			del self.frequency[frequency][key]
			if frequency == self.small and len(self.frequency[self.small]) == 0:
				self.small = frequency + 1
			self.dict[key] += 1
			if frequency + 1 not in self.frequency:
				self.frequency[frequency+1] = OrderedDict()
			self.frequency[frequency+1][key] = value
			self.frequency[frequency+1].move_to_end(key)
      
--------------------------------------------------------------------------------------------------------------------------
import heapq

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.map = {}               # key to value
        self.freq_time = {}         # key to (freq, time)
        self.priority_queue = []    # (freq, time, key), only updated when new key is added
        self.update = set()         # keys that have been get/put since last new key was added

        
    def get(self, key):
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)
            return self.map[key]
        
        return -1

    
    def put(self, key, value):
        if self.capacity <= 0:
            return 
        
        self.time += 1
        if not key in self.map:
            
            if len(self.map) >= self.capacity:      # must remove least frequent from cache
                
                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    # whilst (least frequent, oldest) needs to be updated, update it and add back to heap
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)

                # remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)
            
            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))
            
        else:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time) 
            self.update.add(key)

        self.map[key] = value
