
'''
You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.
'''


import re


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def countTime(self, time: str) -> int:
        pattern = time.replace('?', '.')
        return sum(
            re.fullmatch(pattern, f'{hour:02}:{minute:02}') is not None
            for hour in range(24)
            for minute in range(60)
        )
      
-------------------------------------------------------------------------------------      

class Solution:
    def countTime(self, time: str) -> int:
        res = 1
		# split hour and minute digits
        h1, h2, _ ,  m1, m2 = time
        
        if h1 == "?" and h2 == "?":
            res*=24
        elif h1 == "?":
            if int(h2) >=4:
                res*=2
            else:
                res*=3
                
        elif h2 == "?":
            if int(h1) <= 1:
                res*=10
            elif h1 == "2":
                res*=4
                
        if m1 == "?" and m2 == "?":
            res*=60
        elif m1 == "?":
            res*=6
        elif m2 == "?":
            res*=10
        
        return res
