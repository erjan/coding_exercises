'''
hackerrank
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits ( - ).
It should only contain alphanumeric characters (a-z ,A - Z  & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''

def checker(uid_code):  
    
    length_condition = len(uid_code) == 10
    alpha_num = uid_code.isalnum()
    has_repeating = len(set(uid_code)) == len(uid_code)
    min2_upper_case = len(list(filter(lambda x: x.isupper(), uid_code))) >=2
    min3digits = len(list(filter(lambda x: x.isdigit(), uid_code))) >=3

    if length_condition and alpha_num and has_repeating and min2_upper_case and min3digits:
        return ('Valid')
    else:
        return ('Invalid')
    
      

T = int(input())
for _ in range(T):
    
        
    uid_code = input()
    print(checker(uid_code))

