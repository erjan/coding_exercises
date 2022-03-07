'''
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
'''

#my own solution

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)

        s = list()
        s.append(nums[0])

        for i in range(1, len(nums)):
            print()
            if sum(s) > sum(nums[(i):]):
                print('good')
                print(s)
                return s
                break
            else:
                print('not big enough yet')
                print(s)
                s.append(nums[i])
        print('after all ')
        print(s)
        return s
