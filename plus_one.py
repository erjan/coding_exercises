'''
Given a non-empty array of digits representing a 
non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the 
head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        
        number = int(s) +1
        res = list()
        number = str(number)
        for i in number:
            res.append( int(i))
        return res
