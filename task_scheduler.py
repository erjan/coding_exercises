'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''

import collections, heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        d = collections.defaultdict(int)
        
        for t in tasks:
            d[t] += 1
        
        h = []
        # get the most frequent items to heap top
        for k, v in d.items():
            heapq.heappush(h, (-1*v, k))
        
        c = 0
        while h:
            tmp = []
    
            # iterate by min distance between repeating chars
            # e.g. n = 2, then two spaces are needed after A _ _ A 
            for _ in range(n+1):
                c += 1
                if h:    
                    p, key = heapq.heappop(h)
                    # only add back to heap if > 1 chars remain
                    if p != -1:
                        tmp += [(p+1, key)]
                    
                # if no heap, and no addition to heap, count is complete
                if not h and not tmp:
                    return c
                
            # add back to heap    
            for t in tmp:
                heapq.heappush(h, t)
            
        return c
