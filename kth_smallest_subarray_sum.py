'''
Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.

A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.

 

Example 1:

Input: nums = [2,1,3], k = 4
Output: 3
Explanation: The subarrays of [2,1,3] are:
- [2] with sum 2
- [1] with sum 1
- [3] with sum 3
- [2,1] with sum 3
- [1,3] with sum 4
- [2,1,3] with sum 6 
Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.
Example 2:

Input: nums = [3,3,5,5], k = 7
Output: 10
Explanation: The subarrays of [3,3,5,5] are:
- [3] with sum 3
- [3] with sum 3
- [5] with sum 5
- [5] with sum 5
- [3,3] with sum 6
- [3,5] with sum 8
- [5,5] with sum 10
- [3,3,5], with sum 11
- [3,5,5] with sum 13
- [3,3,5,5] with sum 16
Ordering the sums from smallest to largest gives 3, 3, 5, 5, 6, 8, 10, 11, 13, 16. The 7th smallest is 10.
 
 '''

Explanation
Based on the hint section, we can find number of subarray-sum less than x, so that local the kth smallest number among all subarrays using binary search.
Imagine we find all subarray-sum for some array and sort them, the kth smallest subarray-sum, will lay between the minimum sum and the maximum sum.
We don't necessarily need to find all subarray-sum, nor sort them
Instead, since we know the range, we can use binary search to locate the kth smallest
Essentially, using a binary search is to eliminate the subarray-sums which contains more than k values
At the of the binary search, the lower & upper bound will crossover.
The lower bound tells us, there are k sums that less than this lower bound, which makes this lower bound the kth smallest value, or the largest among these k sums.
To find number of subarray-sum less than x, we can iterate the array while maintaining two pointers to count how many valid subarrays are there. The time complexity of this process is O(n) because each element is visited twice at max. (n is the length of the array)
Time complexity: O(Nlog(N)), where N is the length of the array. Binary search takes O(log(N*(N+1)/2)) = O(log(N^2)) = O(2logN) = O(logN). Finding subarray-sum less than x takes O(N) as mentioned before.
Space Complexity: O(1)
  
  class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def number_of_subarray_sum_less_than_x(x):
            cnt = cur = j = 0
            for i in range(n):
                cur += nums[i]
                while cur > x:
                    cur -= nums[j]
                    j += 1
                cnt += i - j + 1
            return cnt
        n, low, high = len(nums), min(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if k <= number_of_subarray_sum_less_than_x(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
      
---------------------------------------------------------------      

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        
        def fn(x):
            """Return number of subarrays sums <= x."""
            ans = rsm = ii = 0 
            for i in range(len(nums)): 
                rsm += nums[i]
                while rsm > x: # sliding window 
                    rsm -= nums[ii]
                    ii += 1
                ans += i - ii + 1
            return ans 
        
        lo, hi = 0, sum(nums)
        while lo < hi: 
            mid = lo + hi >> 1
            if fn(mid) < k: lo = mid + 1
            else: hi = mid
        return lo 
      
-----------------------------------------------------------------------      


This problem took me some time to understand and I wanted to share my thoughts on it.

At its core, the trick to this problem is:

Being able to compute the number of subarrays for nums less than a given value x
Recognizing we can binary search over values min(nums) and sum(nums) to find an x that matches our answer
Trick 1
We compute the number of subarrays for nums less than a given value x.

As it turns out, the trick only requires an approximation.

Most solutions to "computing the number of subarrays less than a given value" are close to the following:

def num_subarrays_lte(self, nums: List[int], x: int) -> int:
    total_num = 0
    running_sum = 0
    start_idx = 0

    # Create a sliding window and increase our count as we greedily
    # expand (w/ contractions if needed) our window.
    for end_idx in range(len(nums)):
        running_sum += nums[end_idx]
        while running_sum > x:
            running_sum -= nums[start_idx]
            start_idx += 1
        total_num += (end_idx - start_idx) + 1

    return total_num
NOTE: This does not give us an exact answer however:

# Returns 4, however answer should be 5
# {[1], [1], [2], [2], [1, 1]}
Solution().num_subarrays_lte(nums=[1,2,1,2], x=2)
Regardless this apparently gives us a good enough bound to answer the question.

Trick 2
We do a binary search over a search space. Our search space is between:

min(nums), in this case we take just the smallest number possible
sum(nums), in this case we take all the numbers
Our search creates a lower and upper bound on num_subarrays_lte(nums, lower_bound) <= k <= num_subarrays_lte(nums, upper_bound), such that lower_bound is as large as possible, upper_bound is as small as possible, and lower_bound <= upper_bound.

Note that in actuality lower_bound and upper_bound during our search not even be possible subarray sums.

When our binary search is done, we hit the condition:

num_subarrays_lte(nums, lower_bound - 1) < k and num_subarrays_lte(nums, lower_bound) <= k
upon which lower_bound is equal to the kth subarray sum and that is what we return.

def kth_smallest_subarray_sum(self, nums: List[int], k: int) -> int:
    lower_bound = min(nums)
    upper_bound = sum(nums)

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if k < self.num_subarrays_lte(nums=nums, x=mid):
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    return lower_bound
Solution
class Solution:
    def num_subarrays_lte(self, nums: List[int], x: int) -> int:
        total_num = 0
        running_sum = 0
        start_idx = 0

        # Create a sliding window and increase our count as we greedily
        # expand (w/ contractions if needed) our window.
        for end_idx in range(len(nums)):
            running_sum += nums[end_idx]
            while running_sum > x:
                running_sum -= nums[start_idx]
                start_idx += 1
            total_num += (end_idx - start_idx) + 1

        return total_num
    
    def kth_smallest_subarray_sum(self, nums: List[int], k: int) -> int:
        lower_bound = min(nums)
        upper_bound = sum(nums)

        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if k <= self.num_subarrays_lte(nums=nums, x=mid):
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        return lower_bound
    
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        return self.kth_smallest_subarray_sum(nums=nums, k=k)
Apparently this passes. However I'm not really convinced this will always give the correct answer since num_subarrays_lte doesn't always give us the exact answer.

