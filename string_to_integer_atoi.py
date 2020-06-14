'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary 
until the first non-whitespace character is found. Then, starting from 
this character, takes an optional initial plus or minus sign followed by 
as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the 
integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral 
number, or if no such sequence exists because either str is empty or it contains 
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
'''



class Solution:
    def myAtoi(self, str: str) -> int:            
        s = str.strip(' ')
        if len(s) == 0:
            return 0
        neg_sign = False
        if s[0] == '-':
            neg_sign = True
            loop = s[1:]
        else:
            loop = s
        actual_num = ''
        if s[0] == '+':
            #print('s : ' + s)
            loop = s[1:]
        for char in loop:
            print(char)
            if char.isdigit():
                actual_num+= char
            else:
                break
        if len(actual_num) == 0:
            #print(0)
            return 0
        if neg_sign:
            actual_num_int = -int(actual_num)    
        else:
            actual_num_int = int(actual_num)
        if actual_num_int > 2**31-1:
            return 2**31-1
        elif actual_num_int < -(2**31):
            return -(2**31)
        return actual_num_int


