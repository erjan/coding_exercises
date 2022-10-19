'''
You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.
'''


class Solution:
    def smallestNumber(self, num: int) -> int:
        
        
        s = list(str(num))
        if num < 0:
            s = s[1:]
            s = sorted(s, reverse=True)

            s.insert(0, '-')
            s = int("".join(s))
            print(s)
            return s

        else:
            s = sorted(s)
            s = list(map(int, s))
            firstnonzero = 0

            for i in range(len(s)):
                if s[i] != 0:
                    firstnonzero = s[i]
                    ind = i
                    break

            s.pop(i)
            s = list(map(str, s))
            s = "".join(s)
            res = ''
            res += str(firstnonzero)
            s = "".join(s)
            res += s
            return res
          
-------------------------------------------------------------------------

    def smallestNumber(self, a):
        s = sorted(str(abs(a)))
        if a <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))
      
----------------------------------------------------------------

class Solution:
    def smallestNumber(self, num: int) -> int:
        lst=[i for i in str(num)]
        if num<0:
            return ''.join(['-'] + sorted(lst[1:],reverse=True))
        lst=sorted(lst)
        if '0' in lst:
            itr=0
            while itr<len(lst) and lst[itr]=='0':
                itr+=1
            if itr==len(lst):       #All zeroes
                return ''.join(lst)
            return ''.join([lst[itr]]+lst[:itr]+lst[itr+1:])
        return ''.join(lst)
      
-------------------------------------------------------------------------------------------------------      

