'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
		# Edge Condition
        if len(nums)<3: return len(nums)
        
		# Main Logic
		
        ind = 2  # Pointer from where we need to replace elements
        for i in range(2, len(nums)):
            if nums[i]!=nums[ind-2]:
                nums[ind] = nums[i]
                ind+=1
        return ind
      
-----------------------------------------------------------------------------------
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n < 3:
            return n
        
        i , j = 1, 2
        
        while j < n:
            if nums[i-1] != nums[j]:
                i += 1
            
            
            nums[i] = nums[j]
            j+= 1
        
        return i+1
      
--------------------------------------------------------------------------------------------
def removeDuplicates(self, nums):
        if len(nums) < 3: 
            return len(nums)
        pos = 1
        for i in range(1, len(nums)-1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1
