'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
'''

'''
Create a sliding window: [nums[l], nums[l + 1], ..., num].
For each number in the nums array, we check if this num is already present in the window. We can use a set to lookup in O(1).
If the number is present in the window, we keep shrinking the window from the left until there's no repetition.
We update the set by adding num and repeat the above process.
'''


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        curr_sum, max_sum, l = 0, 0, 0
        for num in nums:
            while num in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            curr_sum += num
            seen.add(num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
      
--------------------------------------------------------------------
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prev = [-1] * 10001
        curr_sum, max_sum, l = 0, 0, 0
        for r, num in enumerate(nums):
            if prev[num] >= l:
                curr_sum -= sum(nums[l : prev[num] + 1])
                l = prev[num] + 1
            curr_sum += num
            prev[num] = r
            max_sum = max(max_sum, curr_sum)

        return max_sum
