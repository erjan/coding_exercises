'''
Given two integers num and k, consider a set of positive integers with the following properties:

The units digit of each integer is k.
The sum of the integers is num.
Return the minimum possible size of such a set, or -1 if no such set exists.

Note:

The set can contain multiple instances of the same integer, and the sum of an empty set is considered 0.
The units digit of a number is the rightmost digit of the number.
'''


Explanation
if num == 0, then empty set valid, return 0.

Then we enumerate the size of set from 1 to 10 and check the conditions:

The units digit of each integer is k.
The sum of the integers is num.
These two condistion equals to

size * k <= num
size * k % 10 == num % 10
Return the minimum valid size.

    def minimumNumbers(self, num, k):
        if num == 0: return 0
        for i in range(1, 11):
            if k * i % 10 == num % 10 and i * k <= num:
                return i
        return -1
      
------------------------------------------------------------------------------------
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            if num%10 == 0:
                return 1
            return -1
        count = 1
        while num%10 != k and num > 0:
            num -= k
            count += 1
        if num > 0 and num %10 == k:
            return count
        return -1
