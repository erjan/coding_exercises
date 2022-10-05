'''
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

 
 '''

def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    l = []
    for i in range(len(nums)):
        cum = 0
        for j in range(i,len(nums)):
            cum+=nums[j]
            l.append(cum)
    l.sort()
    return sum(l[left-1:right])%(10**9+7)
  
-----------------------------------------------------------------------------------------
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10 ** 9 + 7
        # Return how many subarrays are <= target and their sum
        def caterpillar(target):
            i = 0
            rank = 0
            total = 0
            
            rev = 0
            elements = 0
            running = 0
            
            for j in range(len(nums)):
                elements += 1
                rev += elements * nums[j]
                running += nums[j]
                while running > target:
                    rev -= running
                    running -= nums[i]
                    elements -= 1
                    i += 1
                rank += elements
                total += rev
            return rank, total
        
        max_sum = sum(nums)
        
        def bi_search(rank):
            if not rank:
                return 0
            low = 1
            high = max_sum
            memo = [(0, 0), None]
            while low != high:
                mid = (low + high) // 2
                r, total = caterpillar(mid)
                if r < rank:
                    low = mid + 1
                    memo[0] = (r, total)
                else:
                    high = mid
                    memo[1] = (r, total)
            if memo[1] is None:
                memo[1] = caterpillar(high)
            if memo[1][0] == rank:
                return memo[1][1]
            else:
                (r0, t0), (r1, t1) = memo
                delta = (t1 - t0) // (r1 - r0)
                return t0 + (rank - r0) * delta
        return (bi_search(right) - bi_search(left - 1)) % mod
