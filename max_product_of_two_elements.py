'''
Given the array of integers nums, you will choose 
two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        m1 = nums[-1]
        m2 = nums[-2]
        print('1st max %d' % m1)
        print('2nd max %d ' % m2)
        res = (m1-1)*(m2-1)
        print('result is %d ' % res)
        return res

        

        result = (nums[ind_max]-1) * (nums[local_m_index]-1)
        print(result)
        return result

