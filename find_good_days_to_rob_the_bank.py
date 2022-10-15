'''
You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.

The ith day is a good day to rob the bank if:

There are at least time days before and after the ith day,
The number of guards at the bank for the time days before i are non-increasing, and
The number of guards at the bank for the time days after i are non-decreasing.
More formally, this means day i is a good day to rob the bank if and only if security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

Return a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in does not matter.
'''

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        # total length of security on duty days
        days = len(security)
        
        ## Base case
        if time == 0:
            
            # Threshold is too small, every day is good day.
            return [ day_i for day_i in range(days) ]
        
        
        elif time > days // 2:
            
            # Threshold is too large, impossible to have good days.
            return []
        
        
        ## General case
        
        # Prefix table, record of length of continuous security guard weakening on index i
        weakenDays = [0] * days
        # Postfix table, record of length of continuous security guard strengthening on index i
        strengthenDays = [0] * days
        
        # Update prefix table and postfix table
        for i in range(1, days):
            
            if security[i] <= security[i-1]:
                weakenDays[i] = weakenDays[i-1] + 1

            if security[-i-1] <= security[-i]:
                strengthenDays[-i-1] =  strengthenDays[-i] + 1

        
        # helper lambda function to judege good day by definition
        is_good_day = lambda i: ( weakenDays[i] >= time ) and ( strengthenDays[i] >= time )

        return [ day_i for day_i in range( days ) if is_good_day(day_i) ]
      
-----------------------------------------------------------------------------------------------------
class Solution:
    def goodDaysToRobBank(self, A, t):
        n = len(A)
        def incGaurd(A):
            arr = [0] * n
            for i in range(1,n):
                if A[i-1] >= A[i]:
                    arr[i] = arr[i-1] + 1
            return arr
        _inc,_dec = incGaurd(A),incGaurd(A[::-1])[::-1]
        ans = []
        for i in range(n):
            if _inc[i] >= t and _dec[i] >= t:
                ans.append(i)
        return ans
