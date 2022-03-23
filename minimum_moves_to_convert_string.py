'''
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.
'''
#my own solution

class Solution:
    def minimumMoves(self, s: str) -> int:
        
        if s.count('X') == 0:
            print('no x found')
            return 0

        i = 0
        c = 0
        while i < len(s):
            print('--------i------', i)
            print()

            if s[i] == 'X':
                i += 3
                c += 1
            else:
                i += 1
        print('count', c)
        print('end')
        return c
      
#another

class Solution:
    def minimumMoves(self, s: str) -> int:
        sl=list(s)
        out=0
        for i in range(0,len(sl)-2):
            if sl[i]=="X":
                sl[i]="O"
                sl[i+1]="O"
                sl[i+2]="O"
                out+=1
            elif sl[i]=="O":
                continue
        if sl[-1]=="X" or sl[-2]=="X":
            out+=1
        return out
      
#another solution 2      
class Solution:
    def minimumMoves(self, s: str) -> int:
        i, m = 0, 0
        l = len(s)

        while i < l:
            if s[i] != 'X':
                i += 1
            elif 'X' not in s[i:i+1]:
                i += 2
            elif 'X' in s[i:i+2]:
                m += 1
                i += 3
        return m  
      
      
class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
		 ans, l = 0, 0
        while l < len(s):
            if s[l] == 'X':
                l+=3
                ans +=1
            else:
                l+=1
        return ans      
