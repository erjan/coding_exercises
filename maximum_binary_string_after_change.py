'''
You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

Operation 1: If the number contains the substring "00", you can replace it with "10".
For example, "00010" -> "10010"
Operation 2: If the number contains the substring "10", you can replace it with "01".
For example, "00010" -> "00001"
Return the maximum binary string you can obtain after any 
number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.




Intution here is to find the first index of zero.

All the ones on the left of first zero are already at most optimal position and need not be changed.
Example - 11100101
Now using the first rule ( '10' -> '01' ) all the zeroes can be shifted to the right of binary.
This gives us 11100011
Now, n zeroes can be converted to (n-1) ones and 1 zero using second rule ( '00' -> '10' ).
This gives us 11111011 which is the max binary string after changes.
'''

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Find the first zero
        first_zero = binary.find('0')
		# If there are no zeroes then no optimization is needed
        if(first_zero == -1):
            return binary
		# Counting number of zeros
        count_zeroes = binary.count('0', first_zero)

        return '1' * (first_zero) + '1' * (count_zeroes-1) + '0' + '1' * (len(binary) - first_zero - count_zeroes)
