'''
You are given a 0-indexed string street. Each character in street is either 'H' representing a house or '.' representing an empty space.

You can place buckets on the empty spaces to collect rainwater that falls from the adjacent houses. The rainwater from a house at index i is collected if a bucket is placed at index i - 1 and/or index i + 1. A single bucket, if placed adjacent to two houses, can collect the rainwater from both houses.

Return the minimum number of buckets needed so that for every house, there is at least one bucket collecting rainwater from it, or -1 if it is impossible.



Explanation
If s == 'H', return -1
If s starts with HH', return -1
If s ends with HH', return -1
If s has 'HHH', return -1

Each house H needs one bucket,
that's s.count('H')
Each 'H.H' can save one bucket by sharing one in the middle,
that's s.count('H.H') (greedy count without overlap)
So return s.count('H') - s.count('H.H')


Key Point
I'm not greedy,
Python count is greedy for me,


Complexity
Time O(n)
Space O(1)


'''
    def minimumBuckets(self, s):
        return -1 if 'HHH' in s or s[:2] == 'HH' or s[-2:] == 'HH' or s == 'H' else s.count('H') - s.count('H.H')
-------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        buckets = 0
        prevBucket = -2
        for i, c in enumerate(street):
            if c == '.' or prevBucket == i - 1:
                continue
            
            buckets += 1
            if i != n - 1 and street[i + 1] == '.':
                prevBucket = i + 1
            elif not i or street[i - 1] == 'H':
                return -1
        
        return buckets
    
