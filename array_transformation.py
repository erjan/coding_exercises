'''
Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.
'''


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            prev = deepcopy(arr)
            for i in range(1,len(arr)-1):
                arr[i] -= prev[i-1] < prev[i] > prev[i+1]
                arr[i] += prev[i-1] > prev[i] < prev[i+1]
            if prev == arr:
                return arr
