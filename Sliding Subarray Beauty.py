'''
Given an integer array nums containing n integers, find the beauty of each subarray of size k.

The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

A subarray is a contiguous non-empty sequence of elements within an array.
'''



class Solution:
    def find_x_smallest(self, count_map, x):
        count = 0
        for num in range(-50, 0, 1):
            if count_map.get(num, 0) != 0:
                count += count_map[num]
                if count >= x:
                    return num
                
        return 0

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        start = 0
        neg = 0
        count_map = {}
    
        ans = []
            
        for end in range(len(nums)):
            # Remove contribution of start element if its negative.
            if start > len(nums)-k+1:
                break
            if nums[end] < 0:
                neg += 1
                count_map[nums[end]] = count_map.get(nums[end], 0) + 1
            
            window_size = end - start + 1
            if window_size == k:
                temp = 0
                if neg >= x: 
                    temp = self.find_x_smallest(count_map, x)
                if nums[start] < 0:
                    neg -= 1
                    count_map[nums[start]] -= 1
                start += 1
                ans.append(temp)
            
        return ans
