'''
Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.
'''

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n = num
        original = n
        reversed1 = int(str(n)[::-1])
        reversed2 = int(str(reversed1)[::-1])


        return n == reversed2
      
#clever solution      
class Solution(object):
    def isSameAfterReversals(self, num):
		# All you have to do is check the Trailing zeros
        return num == 0 or num % 10  # num % 10 means num % 10 != 0      
