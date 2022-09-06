'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
'''

def nextPermutation(self, nums):
    i = j = len(nums)-1
    #find the first non-increasing element starting from the end
    while i > 0 and nums[i-1] >=nums[i]:
        i = i-1
    
    #special case - if nums is all decreasing - reverse the nums
    if i == 0:
        nums.reverse()
        return
    # find the first number > nums[k] starting from end
    k = i-1

    while nums[j] <=nums[k]:
        j = j-1
    #swap these 2 numbers
    nums[k], nums[j] = nums[j],nums[k]
    #erverse the 2nd part
    l = k+1
    r = len(nums)-1
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l = l+1
        r = r-1
