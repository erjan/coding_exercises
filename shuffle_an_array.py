'''
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.rangex = len(nums)

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        ans = self.original[:]
        for i in range(len(ans)):
            swp_num = random.randrange(i, len(ans))  # Fisher-Yates Algorithm
            ans[i], ans[swp_num] = ans[swp_num], ans[i]
        
        return ans
