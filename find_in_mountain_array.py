'''
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
'''


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.find_peak(mountain_arr)
        if mountain_arr.get(peak) == target:
            return peak
        ret = self.binary_search(target, mountain_arr, 0, peak + 1, True)
        if ret != -1:
            return ret
        return self.binary_search(target, mountain_arr, peak, mountain_arr.length(), False)
        
    def find_peak(self, mountain_arr: 'MountainArray'):
        l = 0
        r = mountain_arr.length()
        while l < r:
            mid = (l + r) // 2
            if 0 < mid < mountain_arr.length():
                if mountain_arr.get(mid + 1) > mountain_arr.get(mid):
                    l = mid
                elif mountain_arr.get(mid) < mountain_arr.get(mid - 1):
                    r = mid + 1
                else:
                    return mid
                    
    
    def binary_search(self, target: int, mountain_arr: 'MountainArray', l, r, asc):
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < target:
                if asc:
                    l = mid + 1 
                else:
                    r = mid
            elif mountain_arr.get(mid) > target:
                if asc:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target == mountain_arr.get(mid):
                    return mid
                else:
                    break
        return -1
