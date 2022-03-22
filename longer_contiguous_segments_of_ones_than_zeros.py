'''
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.
'''

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        res = [list(g) for c, g in itertools.groupby(s)]

        ones = 0
        zeros = 0

        for i in range(len(res)):
            if res[i][0] == '1':

                res[i] = ['1', len(res[i])]
            else:
                res[i] = ['0', len(res[i])]

        for i in range(len(res)):
            if res[i][0] == '1':
                if res[i][1] > ones:
                    ones = res[i][1]
            else:
                if res[i][1] > zeros:
                    zeros = res[i][1]

        print('ones', ones)
        print('zeros', zeros)

        return ones > zeros
    
    
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s1 = s.split('0')
        s0 = s.split('1')
        r1 = max([len(i) for i in s1])
        r0 = max([len(i) for i in s0])
        return r1>r0   
