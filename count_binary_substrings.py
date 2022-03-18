
'''
give a binary string s, return the number 
of non-empty substrings that have the same number of 0's and 1's, and 
all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
'''

#stupid TLE
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def check(s):  
            same_number = s.count('0') == s.count('1')
            if not same_number:
                return False

            zeroes, ones = [], []

            for i in range(len(s)):
                if s[i] == '0':
                    zeroes.append(i)
                else:
                    ones.append(i)

            if s[0] == '0':
                if zeroes[-1] > ones[0]:
                    return False
                else:
                    return True

            if s[0] == '1':
                if ones[-1] > zeroes[0]:
                    return False
                else:
                    return True
        c = 0
        for i in range(len(s)):

            for j in range(i+1, len(s)+1):

                sub = s[i:(j)]
                # print(sub)
                if len(sub) % 2 == 0:
                    if check(sub):
                        c += 1
        print('count total', c)
        return c
