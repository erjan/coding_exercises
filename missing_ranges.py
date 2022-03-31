'''
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = list()
        if len(nums)== 0:
            if upper == lower:
                    return [str(upper)]
            return [str(lower) + "->" + str(upper)]
        # corner case at the start
        if nums[0] > lower:
            res.append(str(lower) + "->" + str(nums[0]-1))

        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff > 1:
                print('found diff', diff)
                new_range = [nums[i]+1, nums[i+1]-1]
                print(new_range)
                res.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))

         # corner case in the end
        if nums[-1] < upper:
            res.append(str(nums[-1]+1) + "->" + str(upper))
        # removing bad ranges!

        for i in range(len(res)):

            x = res[i].split("->")
            if x[0] == x[1]:
                res[i] = str(x[0])
        print(res)
        return res
      
      
#another solution from the discussions
def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    res = []
    
    prev = lower - 1 # so that I can handle case when nums is empty
    for i in range(len(nums)+1):
        current = nums[i] if i < len(nums) else upper+1

        # means, not a continuos range where current number
        # is 1 greater than the last number in the list
        if current > prev+1:
            # now my missing intervals will have number prev+1, current-1
            # I can't take the number already present in the list
            # that means, prev and current can't be part of my answer
            if prev+1 < current-1:
                res.append(str(prev+1) + "->" + str(current-1))
            else:
                res.append(str(prev+1))
        
        prev = current
    
    return res
