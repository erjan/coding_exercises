'''
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
'''

class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        l, r = 0, 0
        ans = 1
        if n == 1:
            return 1
        
        while r < n:
            while l < n - 1 and arr[l] == arr[l+1]: # to handle duplicates
                l += 1
            while r < n - 1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
            ans=max(ans, r - l + 1)
            l = r
            r += 1
        return ans
