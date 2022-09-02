'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be 
derived from an array by deleting some or no elements without changing
the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
      
      
----------------------------------------------------------------------------------
def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums:
        return 0
    self.res = 0
    self.dfs(nums, 0, -sys.maxsize, 0)
    return self.res 

def dfs(self, nums, i, pre, cur_len):
    if i == len(nums):
        self.res = max(self.res, cur_len)
        return
    self.dfs(nums, i + 1, pre, cur_len)
    if nums[i] > pre:
        self.dfs(nums, i + 1, nums[i], cur_len + 1)

        
----------------------------------------------------------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        result = 0
        
        for num in nums:
            
            left_index, right_index = 0, result
            while left_index != right_index:
                
                middle_index = left_index + (right_index - left_index) // 2
                
                if tails[middle_index] < num:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index
            result = max(result, left_index + 1)
            tails[left_index] = num
        return result
        
---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    n = len(nums)
    print('array')
    print(nums)
    dp = [1] * n
    print('before')
    print(dp)
    print()

    for i in range(1, n):
        print('--------current i:%d, d[i]: %d ---------------' % (i, nums[i]))
        for j in range(i):
            print(f' compare {nums[i]} vs {nums[j]}, j: {j}')
            if nums[i] > nums[j]:
                print('found')
                print(f'{nums[i]} > {nums[j]}')
                dp[i] = max(dp[i], 1 + dp[j])
                print(f'dp[i] {dp[i]} now: %d' % dp[i])
                print('dp now')
                print(dp)

    print(max(dp))
