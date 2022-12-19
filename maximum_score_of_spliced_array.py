'''
You are given two 0-indexed integer arrays nums1 and nums2, both of length n.

You can choose two integers left and right where 0 <= left <= right < n and swap the subarray nums1[left...right] with the subarray nums2[left...right].

For example, if nums1 = [1,2,3,4,5] and nums2 = [11,12,13,14,15] and you choose left = 1 and right = 2, nums1 becomes [1,12,13,4,5] and nums2 becomes [11,2,3,14,15].
You may choose to apply the mentioned operation once or not do anything.

The score of the arrays is the maximum of sum(nums1) and sum(nums2), where sum(arr) is the sum of all the elements in the array arr.

Return the maximum possible score.

A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).
'''

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        # create a difference array between nums1 and nums2
        # idea: find two subarray(elements are contiguous) in the diff
        # one is the subarray that have the minimum negative sum
        # another one is the subarray that have the maximum positive sum
        # so there are four candidates for maximum score:
        # 1. original_sum1 
        # 2. original_sum 
        # 3. original_sum1 - min_negative_sum
        # 4. original_sum2 + max_positive_sum
        
        original_sum1 = sum(nums1)
        original_sum2 = sum(nums2)
        diff = [num1 - num2 for num1, num2 in zip(nums1, nums2)]
        min_negative_sum = float('inf')
        max_positive_sum = - float('inf')
        cur_negative_sum = 0
        cur_positive_sum = 0
        
        for val in diff:
            cur_negative_sum += val

            if cur_negative_sum > 0:
                cur_negative_sum = 0
            
            cur_positive_sum += val
            
            if cur_positive_sum < 0:
                cur_positive_sum = 0
                    
            min_negative_sum = min(min_negative_sum, cur_negative_sum)
            max_positive_sum = max(max_positive_sum, cur_positive_sum)

        return max(original_sum1 - min_negative_sum, original_sum2 + max_positive_sum, original_sum2, original_sum1)
