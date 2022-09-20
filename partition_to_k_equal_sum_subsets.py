'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
		target_sum, remainder = divmod(s, k)
        if remainder != 0:
            return False
        n = len(nums)

        def loop(num_buckets_remaining: int, used: Bits, current_sum: int, start: int) -> bool:
            # Since number of buckets is only reduced when the previous bucket has been filled,
            # we only need to check if all elements have been used. No need to check current sum.
            if num_buckets_remaining == 0:
                return used.is_all_set()
            if current_sum == target_sum:
                # Fill remaining buckets.
                return loop(num_buckets_remaining - 1, used, 0, 0)
            # Find all unused numbers that can be added to the current bucket.
            for i in range(start, n):
                x = current_sum + nums[i]
                if used.is_unset(i) and x <= target_sum:
                    used.set(i)
                    if loop(num_buckets_remaining, used, current_sum + nums[i], i + 1):
                        return True
                    used.clear(i)

            return False

        return loop(k, Bits(n), 0, 0)
    
class Bits:
    def __init__(self, n: int) -> None:
        self.mask = 0

    def is_unset(self, i: int) -> bool:
        # (1 << i) = All bits cleared except the i-th bit
        return self.mask & (1 << i) == 0

    def set(self, i: int) -> None:
        # (1 << i) = All bits cleared except the i-th bit
        self.mask |= (1 << i)

    def clear(self, i: int) -> None:
        # ~(1 << i) = All bits set except the i-th bit
        self.mask &= ~(1 << i)

    def is_all_set(self) -> bool:
        if self.mask == 0:
            return False
        # If all bits of a number are set, then adding 1 to it produces a number that is a perfect power of 2.
        # AND-ing it with the number clears all bits of the number.
        return (self.mask & (self.mask + 1)) == 0
      
---------------------------------------------------------------------------------------------------------------------------
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(cur_sum, k):
            # terminal case
            if k == 0:
                return True
            if cur_sum == target:
                return backtrack(0, k-1)
            
            #backtrack
            for i in range(len(nums)):
                if not visited[i]:
                    if nums[i] > target:
                        return False
                    if cur_sum + nums[i] <= target:
                        visited[i] = True
                        if backtrack(cur_sum+nums[i], k):
                            return True
                        else:
                            visited[i] = False
            return False
            
        if sum(nums) % k: return False
        target = sum(nums) / k
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        return backtrack(0, k)
      
-----------------------------------------------------------------------------------------------------
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    ts = sum(nums)
    if ts % k != 0:
        return False
    its = int(ts/k)
    used = [False] * len(nums)
    nums.sort(reverse=True)
    def helper(t, k, idx):
        if k == 0:
            return True
        if t == 0:
            return helper(its, k - 1, 0)
        else:
            for i in range(idx, len(nums)):
                if not used[i] and t - nums[i] >= 0:
                    used[i] = True
                    if helper(t - nums[i], k, i + 1):
                        return True
                    used[i] = False
                
    return helper(its, k, 0)
        
