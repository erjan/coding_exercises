'''

Given an integer n, return the nth (0-indexed) row of Pascal's triangle.

Pascal's triangle can be created as follows: In the top row, there
is an array of 1. Each subsequent row is created by adding the number above 
and to the left with the number above and to the right, treating empty elements as 0.

'''
class Solution:
    def solve(self, n):
        def helper(self,d):
            res = []
            for i in range(len(d)-1):
                temp = d[i] + d[i+1]
                res.append(temp)
            res.insert(0,1)
            res.insert( len(res),1)
            return res
        
        numRows = n
      
        res = []
        res.append([1])
                
        if numRows == 0:
            return [1]
        
        for i in range(1,numRows+1):
            prev = res[i-1]
            temp = helper(self,prev)
            res.append(temp)
        print(res)
        res = res[n]
        return res
      
      
#another solution

class Solution:
    def solve(self, n):
        res = [1]
        for k in range(1, n + 1):
            res.append(res[-1] * (n + 1 - k) / k)
        return res
      
      
#another

from math import comb  # import choose notation function


class Solution:
    def solve(self, n):
        row = []
        for i in range(0, n + 1):  # loop through all values in row
            row.append(comb(n, i))  # calculate row column value
        return row
