'''
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.
'''


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedSet
        if not nums or t < 0: return False     # Handle special cases
        ss, n = SortedSet(), 0                 # Create SortedSet. `n` is the size of sortedset, max value of `n` is `k` from input
        for i, num in enumerate(nums):
            ceiling_idx = ss.bisect_left(num)  # index whose value is greater than or equal to `num`
            floor_idx = ceiling_idx - 1        # index whose value is smaller than `num`
            if ceiling_idx < n and abs(ss[ceiling_idx]-num) <= t: return True  # check right neighbour 
            if 0 <= floor_idx and abs(ss[floor_idx]-num) <= t: return True     # check left neighbour
            ss.add(num)
            n += 1
            if i - k >= 0:  # maintain the size of sortedset by finding & removing the earliest number in sortedset
                ss.remove(nums[i-k])
                n -= 1
        return False
      
---------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # O(N) one-pass solution based on buckets with size t + 1
        if k <= 0 or t < 0:
            return False
        from collections import deque
        bucket_cache = deque([],k)
        bucket_dict = {}
        # O(N) one pass
        for i in range(len(nums)):
            # We calculate a bucket index containing nums[i]
            remainder = nums[i] % (t + 1)
            bucket = (nums[i] - remainder) / (t+1)
            # Checking cache for duplicates
            if bucket in bucket_dict:
                return True # We found two values in the same bucket
            if bucket - 1 in bucket_dict and abs(nums[i] - bucket_dict[bucket - 1]) <= t:
                return True # Two values in adjacent buckets and nearby values
            if bucket + 1 in bucket_dict and abs(nums[i] - bucket_dict[bucket + 1]) <= t:
                return True # Two values in adjacent buckets and nearby values
            # Adding new bucket to cache
            if i >= k: # Maximal cache size is equal to k
                bucket_to_remove = bucket_cache.popleft()
                del bucket_dict[bucket_to_remove]
            bucket_cache.append(bucket)
            bucket_dict[bucket] = nums[i]
        return False
