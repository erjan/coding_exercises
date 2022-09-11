'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            
            mid = (l+r)//2
            
            if  nums[mid] < nums[mid+1]:
                l = mid+1
            
            else:
                r = mid
        return l
        
-----------------------------------------------------
public class Solution {
    public int findPeakElement(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1])
                return i;
        }
        return nums.length - 1;
    }
}
