'''
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
'''

class Solution:
    def checkRecord(self, n: int) -> int:
    	C, m = [1,1,0,1,0,0], 10**9 + 7
    	for i in range(n-1):
    		a, b = sum(C[:3]) % m, sum(C[3:]) % m
    		C = [a, C[0], C[1], a + b, C[3], C[4]]
    	return (sum(C) % m)
		
    
