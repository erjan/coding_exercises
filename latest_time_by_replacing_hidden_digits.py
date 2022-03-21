'''
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.
'''

class Solution:
    def maximumTime(self, time: str) -> str:
        x = list(time)
        if x[0] == '?':
            if x[1] <= '3':
                x[0] = '2'
            elif x[1] == '?':
                x[0] = '2'
            else:
                x[0] = '1'
        if x[1] == '?':
            if x[0] == '2':
                x[1] = '3'
            elif x[0] == '?':
                x[1] = '3'
            else:
                x[1] = '9'
        if x[3] == '?':
            x[3] = '5'
        if x[4] == '?':
            x[4] = '9'
        return (''.join(x))
