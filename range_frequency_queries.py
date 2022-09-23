'''
Design a data structure to find the frequency of a given value in a given subarray.

The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the RangeFreqQuery class:

RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).

 
 '''

class RangeFreqQuery(object):
    def __init__(self, arr):
        self.data = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.data[n].append(i)
        

    def query(self, left, right, value):
        return bisect.bisect_right(self.data[value], right) - bisect.bisect_left(self.data[value], left)
      
----------------------------------------------------------------------------------------------------------------
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.seen = defaultdict(list)
        for i, num in enumerate(arr):
            self.seen[num].append(i)        

    def query(self, left: int, right: int, value: int) -> int:
        arr = self.seen[value]
        # binary search for left and right
        # need to know the implement of bisect_left and bisect_right

        left_idx = self.bsect_left(arr, left)
        right_idx = self.bsect_right(arr, right)
        
        return right_idx - left_idx
        
    def bsect_right(self, arr, target):
        l, h = 0, len(arr) - 1
        
        while l <= h:
            mid = l + (h - l) // 2
            if arr[mid] == target:
                l = mid + 1
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                h = mid - 1
        return l
    
    def bsect_left(self, arr, target):
        l, h = 0, len(arr) - 1
        
        while l <= h:
            mid = l + (h - l) // 2
            if arr[mid] == target:
                h = mid - 1
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                h = mid - 1
        return l
