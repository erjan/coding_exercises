'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the 
count-and-say sequence. You can do so recursively, in other words from 
the previous member read off the digits, counting the number of 
digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
'''


from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(self,s):
            s = str(s)

            res = []
            t = list(''.join(group) for key, group in groupby(s))
            for i in range(len(t)):
                res.append( str(len(t[i])) +  t[i][0])

            res = ''.join(res)
            return res
        
        def f(self,n, prev, l):
            if n == 1:
                l.insert(0,1)
                return str(l[-1])
            else:
                prev = helper(self,prev)
                l.append(prev)
                return f(self,n-1, prev,l)
        
        return f(self,n,1,[])
