'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.
'''






'''
it is also given that ''A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.''
here i is current element ,if A[i]-A[i-1] == A[i-1]-A[i-2] then sequence length for current element i.e l[i] will be 1+sequence length of previous element(l[i-1)

TO return the total number of arithmetic slices in the array A return Caluculated Sum of array l
'''




class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        le=len(A)
        l=[0]*(le)
        for i in range(2,le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                l[i]=1+l[i-1]
        return sum(l)
      
------------------------------------------------------------------------------------------
Idea:

If we transform the array to a difference array. (e.g. [1, 5, 9, 13, 6, 8, 10] --> [4, 4, 4, -7, 2, 2]), the question becomes asking how many subarrays of length >=2 that consists of identical elements in the diff_arr (I will call them good subarrays).
To count the total number of good subarrays, we just need to iterate through the array once while keeping track of the current diff and cnt. At each index, we count the number of good subarrays that end at this index and add it to res.
The following is an implementation of the above idea without explicitly constructing the diff array.

Time complexity: O(N), because we iterate through the array once, at each index there are only a constant number of operations.
Space complexity: O(1)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cur_diff, cnt = -1, 0
        res = 0
        for i in range(1, len(nums)):
            new_diff = nums[i] - nums[i-1]
            if new_diff != cur_diff:
                cur_diff, cnt = new_diff, 1
            else:
                res += cnt
                cnt += 1
        return res
