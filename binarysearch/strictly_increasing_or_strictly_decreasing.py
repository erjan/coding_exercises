
#Given a list of integers nums, return whether the list is strictly increasing or strictly decreasing.

class Solution:
    def solve(self, nums):

        if len(nums) < 2:
            return True

        if nums[0] == nums[1]:
            return False

        if nums[0] < nums[1]:
            increasing = True

            for i in range(len(nums)-1):

                if nums[i] >= nums[i+1]:
                    return False
            return True

        else:
            increasing = False

            for i in range(len(nums)-1):

                if nums[i] <= nums[i+1]:
                    return False
            return True


#another

class Solution:
    def solve(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                break
        else:
            return True
        for i in range(1, len(nums)):
            if nums[i - 1] <= nums[i]:
                break
        else:
            return True
        return False


#another

class Solution:
    def solve(self, nums):
        if len(nums) == 1:
            return True
        desc = nums[0] > nums[1]
        for i in range(0, len(nums) - 1):
            if (desc and nums[i] <= nums[i + 1]) or (not desc and nums[i] >= nums[i + 1]):
                return False
        return True


        
        




        
        
