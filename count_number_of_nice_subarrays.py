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
    
-------------------------------------------------------------------------------------------
def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    
    # This is just converting the even number to 0 and odd numbers to 1 in the array
    for i in range(len(nums)):
        
        if nums[i] % 2 == 0:
            nums[i] = 0
        else:
            nums[i] = 1
            
    # Then doing exactly the same thing as subarray sum equal k problem
            
    currsum = 0
    subarray = 0
    hashmap = {}
    
    for num in nums:
        currsum += num
        
        if currsum == k:
            subarray += 1
        
        if currsum - k in hashmap:
            subarray += hashmap[currsum - k]
        
        if currsum in hashmap:
            hashmap[currsum] += 1
        
        else:
            hashmap[currsum] = 1
    
    return subarray
