'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """There should be no more than one zero in sliding window"""
        start = 0  # left pointer
        end = 0  # right pointer
        count_zeros = 0  # total count of zeros
        max_len = 0

        while end <= len(nums) - 1:  # python offset -1 for index
            if nums[end] == 0:
                count_zeros += 1

            while count_zeros > 1:
                if nums[start] == 0:
                    count_zeros -= 1
                start += 1

            max_len = max(max_len, end - start)
            end += 1

        return max_len

---------------------------------------------------------------------------------------------------------

def print_pointers(nums, l, r):

    for i in range(len(nums)):
        if i == l and i == r:
            print('V')
            print('V')
        elif i == l or i == r:
            print("V", end=" ")
        else:
            print(" ", end=" ")
    print()
    for i in range(len(nums)):
        print(nums[i], end=" ")
    print()


def f(nums) -> None:
    n = len(nums)
    l = 0
    r = 0
    res = 0

    count = 0

    while r < len(nums):
        print("----------------------------")
        print_pointers(nums, l, r)
        print()

        if nums[r] == 0:
            count += 1
            print("found 0, increase count, count now is %d" % count)

        while count > 1:
            print("***********")

            if nums[l] == 0:
                count -= 1
                print("left was 0, decrease count, count now is %d" % count)
            print("moving left pointer")
            l += 1
            print_pointers(nums, l, r)

        res = max(res, r - l + 1 - count)
        print("moving right pointer")
        r += 1

    res = res - 1 if res == n else res
    print("max window is %d" % res)
    return res


