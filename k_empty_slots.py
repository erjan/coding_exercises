'''

You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are on after n days.

You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.
'''


I really struggled to wrap my head around this. So here's to head unwrapping.

Let's keep track of a sorted list called timePassed. Every day, we'll insert a single value to this list. What value? It'll be the bulb that we're turning on for today. Every time we insert a value at position cur, we'll check its neighboring bulbs (at positions cur-1 and cur+1). If either neighbor is K apart from the current, then we return today as our answer.

Question: How do we check if either neighboring bulb is K apart from the bulb turned on today? We use abs(timePassed[cur] - timePassed[cur-1]) == K+1, abs(timePassed[cur] - timePassed[cur+1]) == K+1

Example: Our input bulbs = [1,3,2], K=1. Note that this means the indexes have to be K+1 apart.

On day 1: timePassed = [1]. This means bulb 1 is turned on on day 1.
On day 2, timePassed = [1,3]. This means bulb 3 is turned on on day 2. What's the neighbor of bulb 3 in timePassed? It's bulb 1. And how far apart are they? 3 - 1 =K+1. So we return day 2.
Code

import bisect
class Solution(object):
    def kEmptySlots(self, bulbs, K):

        timePassed = []
        for i, bulb in enumerate(bulbs):
            # Where do we insert today's bulb?
            insertLoc = bisect.bisect_left(timePassed, bulb)
            timePassed.insert(insertLoc, bulb)
            v1, v2 = 0, 0
            # Location of our neighboring bulbs
            prevLoc, nextLoc = insertLoc - 1, insertLoc + 1
            # Check if either neighbor is K apart from the bulb turned on today
            if prevLoc >= 0:
                if abs(timePassed[prevLoc] - timePassed[insertLoc]) == K + 1:
                    v1 = max(bulbs[timePassed[prevLoc]-1], bulbs[timePassed[insertLoc]-1])
            if nextLoc < len(timePassed):
                if abs(timePassed[insertionPoint] - timePassed[nextLoc]) == K + 1:
                    v2 = max(bulbs[timePassed[insertLoc]-1], bulbs[timePassed[nextLoc]-1])
            if v1 or v2:
                return len(timePassed)

        return -1
      
      
----------------------------

class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        
        def get_bucket(bulb):
            return (bulb - 1) // (K + 1)
        
        bucket_len = get_bucket(max(bulbs)) + 1
        buckets = [{} for _ in range(bucket_len)]
        
        for iday, bulb in enumerate(bulbs):
            ibucket = get_bucket(bulb)
            
            if not buckets[ibucket] or bulb > buckets[ibucket]['max']:
                if ibucket + 1 < bucket_len and buckets[ibucket + 1]:
                    if buckets[ibucket + 1]['min'] - bulb == K + 1:
                        return iday + 1
            if not buckets[ibucket] or bulb < buckets[ibucket]['min']:
                if ibucket - 1 >= 0 and buckets[ibucket - 1]:
                    if bulb - buckets[ibucket - 1]['max'] == K + 1:
                        return iday + 1
            
            buckets[ibucket]['min'] = min(buckets[ibucket].get('min', float('inf')), bulb)
            buckets[ibucket]['max'] = max(buckets[ibucket].get('max', -float('inf')), bulb)
        
        return -1
