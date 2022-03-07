'''
Given a 0-indexed integer array nums of size n, find the maximum difference 
between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
'''

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi = -1

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                diff = nums[j] - nums[i]
                if diff > maxi and nums[i] < nums[j]:
                    print('found %d' % diff)
                    print('indices are %d %d' % (i, j))
                    print(nums[j], nums[i])
                    maxi = diff

        print('maxi diff is %d' % maxi)
        return maxi
    
#another solution 1 pass    
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxdiff = -1

        min_num = nums[0]
        
        for i in range(len(nums)):
            maxdiff = max(maxdiff, nums[i] - min_num)
            min_num = min(nums[i], min_num)
        return maxdiff if maxdiff != 0 else -1    
