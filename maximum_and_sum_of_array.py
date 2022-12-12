'''
You are given an integer array nums of length n and an integer numSlots such that 2 * numSlots >= n. There are numSlots slots numbered from 1 to numSlots.

You have to place all n integers into the slots such that each slot contains at most two numbers. The AND sum of a given placement is the sum of the bitwise AND of every number with its respective slot number.

For example, the AND sum of placing the numbers [1, 3] into slot 1 and [4, 6] into slot 2 is equal to (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4.
Return the maximum possible AND sum of nums given numSlots slots.
'''

    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def dp(i, mask):
            if i == len(nums):
                return 0
            ans = 0
            for slot in range(numSlots):
                base = 10**slot
                if mask // base % 10 < 2:
                    ans = max(ans, (nums[i] & (slot + 1)) + dp(i + 1, mask + base))
                
            return ans

        return dp(0, 0)
