'''
You are given an array nums of non-negative integers. nums is considered special 
if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
'''

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums)+1):
            print('value x is %d' % x)
            check = len(list(filter(lambda z: z >= x, nums)))
            print('count of elements is %d ' %
                  check)

            if x == check:
                print(x)
                return x
        print('-1')
        return -1
