'''
A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit '0' with the letter 'O', and the digit '1' with the letter 'I'. Such a representation is valid if and only if it consists only of the letters in the set {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}.

Given a string num representing a decimal integer n, return the Hexspeak representation of n if it is valid, otherwise return "ERROR".
'''


class Solution:
    def toHexspeak(self, num: str) -> str:
        dict_ = {'0' : 'O', '1' : 'I'}
        string = hex(int(num))[2:].upper()
        res = []
        for c in string:
            temp = c if c not in dict_ else dict_[c]
            if temp.isdigit():
                return 'ERROR'
            res.append(temp)
        return ''.join(res)
       
