'''
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.
'''


	def minimizeArrayValue(self, A: List[int]) -> int:
        return max((a + i) // (i + 1) for i,a in enumerate(accumulate(A)))
    
---------------------------------------------------------------------------------------------------------------------

from math import ceil
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minimizeArrayValue(self, nums: List[int]) -> int:
        cum_sum = maximum = 0

        for i, num in enumerate(nums, start=1):
            cum_sum += num
			# At each step, we can try to minimize the element by evenly placing
			# the excess between the previous elements.
            maximum = max(ceil(cum_sum / i), maximum)

        return maximum
      
-------------------------------------------------------------------------------------------------------------------------------------
Let's assume nums includes two numbers only: [num1, num2]. According to the problem description, there is no way to decrease num1. So manipulations are possible only with num2. 3 possible cases can be considered:

num1 > num2: nothing can be done to decrease max(nums), num1 shall be returned;
num1 = num2: same as above;
num1 < num2: we can decrease num2 increasing num1 so both are equal (or almost equal). If (num1 + num2) % 2 == 0 the resulting maximum value is (num1 + num2) // 2, otherwise 1 should be added to the average.
Now let's assume nums = [num1, num2, num3] and we already equalized num1, num2. We can only decrease num3 thus increasing num1 and num2, but this action does not make any sence if num3 is less or equal to max(nums1, nums2). If num3 is the maximum we can equalize these 3 numbers making them as close to sum(num1, num2, num3)/3 as possible.

So the algoritghm is to iterate over nums elements calculating the average and updating the maximum value if current average > current max.

Time complexity: O(n)
Space complexity: O(1)

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_ = sum_ = 0
		
        for i, num in enumerate(nums, start = 1):
            sum_ += num
            ave, modulo = divmod(sum_, i)
            if modulo: ave += 1
            max_ = max(ave, max_)

        return max_
    # end minimizeArrayValue()
