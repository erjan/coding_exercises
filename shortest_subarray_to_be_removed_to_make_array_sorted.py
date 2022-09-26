'''
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.
'''

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # case(0): no need to remove
        # case(1): remove left part
        # case(2): remove right part
        # case(3): remove mid part
        
        # case(1)
        left, right = 0, len(arr)-1
        while left < len(arr)-1:
            if arr[left+1] >= arr[left]:
                left += 1
            else:
                break
        
        # case(0)
        if left == len(arr)-1:
            return 0
        
        while right > 0:
            if arr[right-1] <= arr[right]:
                right -= 1
            else:
                break
        
        # compare case(1) and case(2)
        ans = min(right, len(arr)-1-left)
        
        # case(3)
        for i in range(left+1):
            if arr[i] <= arr[right]:
                ans = min(ans, right-i-1)
            elif right < len(arr)-1:
                right += 1
            else:
                break
        return ans
      
---------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        def lowerbound(left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                
                if arr[mid] == target:
                    right = mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
                
            return left
        
        
        N = len(arr)
        
        # find the longest ascending array on the left side
        i = 0
        while i + 1 < N and arr[i] <= arr[i+1]:
            i += 1
        
        if i == N - 1:
            # it is already in ascending order
            return 0
        
        # find the longest ascending array on the right side
        j = N - 1
        while j - 1 >= 0 and arr[j] >= arr[j-1]:
            j -= 1
        
        if j == 0:
            # the entire array is in decending order
            return N - 1
        
        # keep ascending array on right side or left side
        result = min(N - (N - j), N - i -1)
        
        
        # find the shortest unordered subarray in the middle 
        for k in range(i+1):
            l = lowerbound(j, len(arr), arr[k])
            result = min(result, l - (k + 1))
        
        
        return result
