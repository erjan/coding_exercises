#Reverse a 3-digit integer.

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverse_integer(self, number: int) -> int:
        # write your code here

        number = str(number)[::-1]
        return int(number)
