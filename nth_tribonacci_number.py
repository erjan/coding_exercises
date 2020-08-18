'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        res = list()
        t0 = 0
        t1 = 1
        t2 = 1
        res.append(t0)
        res.append(t1)
        res.append(t2)


        for i in range(3,n+1):
            res.append(res[i-3] + res[i-2] + res[i-1])
        print(res[-1])
        return res[-1]
