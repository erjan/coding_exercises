
'''
You are given a 0-indexed integer array nums.

The low score of nums is the minimum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.
The high score of nums is the maximum value of |nums[i] - nums[j]| over all 0 <= i < j < nums.length.
The score of nums is the sum of the high and low scores of nums.
To minimize the score of nums, we can change the value of at most two elements of nums.

Return the minimum possible score after changing the value of at most two elements of nums.

Note that |x| denotes the absolute value of x.
'''




'''
Approach
This question reduces to minimizing the range of nums by changing 2 elements in nums. We can minimize the range by doing one of 3 options:

Increase the smallest two numbers. Therefore, the range in this option will be largest - third smallest.
Increase the smallest number and decrease the largest number. Therefore, the range in this option will be second largest - second smallest.
Decrease the largest two numbers. Therefore, the range in this option will be third largest - smallest.
We return the minimum of these three options to find the minimum score possible.

Code
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1]-nums[2],nums[-2]-nums[1],nums[-3]-nums[0])   
'''









'''
Sort nums to s_nums for random access to maxes and mins.

If there were 0 changes allowed:
There's nothing to do.
The best we can do is: s_nums[n - 1] - s_nums[0].

Note: Abbriviating s_num[a] - s_num[b] as |a, b| from henceforth.
Hence the above becomes |n - 1, 0|

If there were 1 change allowed:
We can change the first or the last number to the adjacent one.
The best we can do is:
min(|n - 1, 1| (changing the first), |n - 2, 0| (changing the last).

If there were 2 change allowed:
The best we can do is:
min(|n - 1, 2|, |n - 2, 1|, |n - 3, 0|)

Extending the same, If there were k changes allowed:
The best we can do is:
min(|n - 1, k|, |n - 2, k - 1|, ...., |n - k - 1, 0|)
'''


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        s_nums = sorted(nums)
        k = 2
        return min(
            s_nums[i] - s_nums[j]
            for i, j in zip(range(-1, -k - 2, -1), range(k, -1, -1))
        )




