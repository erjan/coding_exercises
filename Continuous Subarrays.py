'''
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


------------------
#this is not my solution - just copied it
from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()  # To maintain the current window's sorted elements
        start = 0
        total_subarrays = 0
        
        for end in range(n):
            # Add the current element to the sorted window
            sorted_window.add(nums[end])
            
            # Ensure the window is valid
            while sorted_window[-1] - sorted_window[0] > 2:
                # Remove the leftmost element from the window
                sorted_window.remove(nums[start])
                start += 1
            
            # Count valid subarrays ending at 'end'
            total_subarrays += end - start + 1
        
        return total_subarrays

---------------------------
'''
my vs code to print out everything
notice, how i print out the content of sorted window [2,4,5] but the original array at this moment is [5,4,2] so i remove the nums[start] from the sorted array!

'''
from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums) -> int:
        res = 0

        sorted_window = SortedList()
        n = len(nums)
        start = 0
        total = 0
        print(f'original array: {nums}')
        print()
        for end in range(n):
            print('---------------------------------------')
            print(f'start: {start}, end: {end}')
            sorted_window.add(nums[end])
            print('sorted window:')
            print(sorted_window)

            while sorted_window[-1]-sorted_window[0]>2:
                print()
                print(' ' *30  + 'invalid window, start pointer +1')
                print(f'start: {start}, end: {end}')
                print(f'nums[start]: {nums[start]}')
                sorted_window.remove(nums[start])
                print(' ' *30  + 'sorted window after removing nums[start]')
                print(sorted_window)
                start+=1
            else:
                print('window is valid , continue adding')
            
            print()
            print(f'adding total: {total}')
            total+= end -start+1

        return total            




s = Solution()
nums = [5,4,2,4]

s.continuousSubarrays(nums)





