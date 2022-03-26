'''
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index
'''

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        s = nums
    
        found = False
        for middle in range(len(s)+1):
            left_sum = s[:middle]
            rite_sum = s[middle:len(s)]
            if sum(left_sum) == sum(rite_sum[1:]):
                if middle < len(s):
                    print('yes found',middle)
                    found = True
                    return middle
            print(left_sum, rite_sum)

        if not found:
            print('not found')
            return -1
