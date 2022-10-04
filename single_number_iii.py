'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
'''

to solve this problem:

Find the xor of the two numbers a and b that only occur once by xor-ing the entire array. Property 3
The two numbers a and b must differ by at least one bit, otherwise their xor would've been 0. Lets say b is the number that has the lowest set bit and a has the lowest unset bit.

Find a by xor-ing all those numbers that have the lowest unset bit. Property 4

Once you have a we can find b by xor-ing with xor of the entire array. Property 2

Implementation
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        zor = reduce(xor, nums)
        res = reduce(xor, filter(lambda i: i & (zor ^ (zor & (zor - 1))), nums))
        return [res,res^zor]
      
------------------------------------------------------------------------------------
def singleNumber(self, nums):
    # "xor" all the nums 
    tmp = 0
    for num in nums:
        tmp ^= num
    # find the rightmost "1" bit
    i = 0
    while tmp & 1 == 0:
        tmp >>= 1
        i += 1
    tmp = 1 << i
    # compute in two seperate groups
    first, second = 0, 0
    for num in nums:
        if num & tmp:
            first ^= num
        else:
            second ^= num
    return [first, second]
