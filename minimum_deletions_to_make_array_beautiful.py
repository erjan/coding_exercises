'''
You are given a 0-indexed integer array nums. The array nums is beautiful if:

nums.length is even.
nums[i] != nums[i + 1] for all i % 2 == 0.
Note that an empty array is considered beautiful.

You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

Return the minimum number of elements to delete from nums to make it beautiful.
'''

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        # Greedy !
        # we first only consider requirement 2: nums[i] != nums[i + 1] for all i % 2 == 0
        # at the begining, we consider the num on the even index
        # when we delete a num, we need consider the num on the odd index
        # then repeat this process
        # at the end we check the requirement 1: nums.length is even or not
        
        n = len(nums)
        count = 0
        # flag is true then check the even index
        # flag is false then check the odd index
        flag = True
        
        for i in range(n):
            # check the even index
            if flag:
                if i % 2 == 0 and i != n -1 and nums[i] == nums[i + 1]:
                    count += 1
                    flag = False
            # check the odd index
            elif not flag:
                if i % 2 == 1 and i != n -1 and nums[i] == nums[i + 1]:
                    count += 1
                    flag = True
        
        curLength = n - count
        
        return count if curLength % 2 == 0 else count + 1
