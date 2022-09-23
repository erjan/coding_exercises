'''
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
 
 '''

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1Count = collections.Counter(nums1)
        self.nums2Count = collections.Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2Count[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2Count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for num, count in self.nums1Count.items():
            res += count * self.nums2Count[tot - num]
        return res
