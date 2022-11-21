'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
'''


class Solution:
    def maxCoins(self, nums):

        nums = [1]+[n for n in nums if n!=0]+[1]
        regional_max_coins = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for balloons_to_burst in range(1, len(nums)-1): # number of balloons in (l,r) region
            for l in range(0, len(nums)-balloons_to_burst-1): # for m and r to be assigned legally
                r = l+balloons_to_burst+1
                for m in range(l+1,r):
                    regional_max_coins[l][r] = max(regional_max_coins[l][r], regional_max_coins[l][m]+regional_max_coins[m][r]+nums[l]*nums[m]*nums[r])
        return regional_max_coins[0][-1]
