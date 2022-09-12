'''
You are given an array of integers nums represents the numbers written on a chalkboard.

Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return true if and only if Alice wins the game, assuming both players play optimally.
'''


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return not reduce(lambda a,b: a^b, nums) or not len(nums)%2
      
------------------------------------------------------------------------
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        test, i = 0, 0
        for n in nums:
            test = test ^ n
            i += 1
        return True if test == 0 else i % 2 == 0
