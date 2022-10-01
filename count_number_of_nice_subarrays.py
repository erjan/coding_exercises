'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        right ,left = 0,0
        ans = 0 
        odd_cnt = 0
        ans = 0
        cur_sub_cnt = 0
        for right in range(len(nums)):
            
            if nums[right]%2 == 1:
                odd_cnt += 1
                cur_sub_cnt = 0
                
            while odd_cnt == k:
                if nums[left]%2 == 1:
                    odd_cnt -= 1
                cur_sub_cnt += 1
                left += 1
                
            ans += cur_sub_cnt
            
        return ans  
