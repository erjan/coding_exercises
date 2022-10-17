'''
You are given a string num, representing a large integer, and an integer k.

We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

For example, when num = "5489355142":
The 1st smallest wonderful integer is "5489355214".
The 2nd smallest wonderful integer is "5489355241".
The 3rd smallest wonderful integer is "5489355412".
The 4th smallest wonderful integer is "5489355421".
Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.

The tests are generated in such a way that kth smallest wonderful integer exists.
'''


This is a difficult question so lets understand it in parts:

Finding the next permutation: Its explained over here: https://leetcode.com/problems/next-permutation/discuss/2602889/Simple-python-solution-with-comments-or-O(n)-or-Explained

Finding the number of swaps: Once we get the proper permutation, we compare every index between the original and the permuation. If we find any mismatch in a given index, we try to make the permutation equal to the original, so we find the index in the permutation where the original number exists at a given position and pop it and insert it in the current index. The difference between this found index and the current index is the number of swaps needed, so we add it to the answer. We repeat it untill we get back the original string.

Upvote if you understood the logic :)

class Solution:
    def getMinSwaps(self, orig: str, k: int) -> int:
        def nextPermutation(nums):
            i = len(nums) - 2

            while i > -1 and nums[i] >= nums[i + 1]:
                i -= 1

            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = reversed(nums[i + 1:])
            return nums

        nums = list(orig)
        res = None

        for _ in range(k):
            res = nextPermutation(nums)

        ans = i = 0
		# finding the number of swaps needed
        while i < len(res) - 1:
            if res[i] != orig[i]:
                index = res.index(orig[i], i + 1)
                res.insert(i, res.pop(index))
                ans += index - i

            i += 1

        return ans
