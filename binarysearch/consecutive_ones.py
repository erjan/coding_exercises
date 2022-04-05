'''

You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.

'''


class Solution:
    def solve(self, nums):
        if nums.count(1) == 1:
            return True

        else:
            c1 = nums.count(1)

            ind1 = nums.index(1)

            allones = nums[ind1 : ind1+ c1]
            if len(set(allones)) > 1:
                return False
            return True

        
        
#another

class Solution:
    def solve(self, nums):
        alreadyseen = 0
        """
        0 means never seen
        1 means currently seeing
        2 means has finished seeing
        """
        for x in nums:
            if x == 1:
                if alreadyseen == 2:
                    return False
                alreadyseen = 1
            elif alreadyseen:
                alreadyseen = 2
        return True
