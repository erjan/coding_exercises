'''
  You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

Return the number of non-empty subarrays in nums that have a median equal to k.

Note:

The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
A subarray is a contiguous part of an array.
'''
  
  
  def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum_of_balance = Counter([0]) # Dummy value of 0's frequency is 1.
        running_balance = ans = 0
        found = False
        for num in nums:
            if num < k:
                running_balance -= 1
            elif num > k:
                running_balance += 1
            else:
                found = True
            if found:
                ans += prefix_sum_of_balance[running_balance] + prefix_sum_of_balance[running_balance - 1]    
            else:
                prefix_sum_of_balance[running_balance] += 1
        return ans
