'''
Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.
'''

class Solution:
    def recursion(self, digits , inc , size , n  , pos):
        ans = 0
        if pos == size:return 0
        if pos in self.dp:return self.dp[pos]
        for i in digits:
            if i < n[pos]:
                val = 1
                for j in range(size-pos):
                    ans+=val
                    val*=inc
            elif i > n[pos]:
                if size == pos + 1:continue
                val = 1
                for j in range(size-pos-1):
                    ans+=val
                    val*=inc
            else:
                ans+=1
                ans+=self.recursion(digits , inc , size , n ,pos+1)
        self.dp[pos]=ans
        return ans
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        self.dp = {}
        return self.recursion(digits , len(digits) , len(n) , n , 0)
-------------------------------------------------------------------------------
#tle

from collections import deque
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        res = 0
        q, visit = deque(), set()
        for num in digits:
            if int(num) <= n:
                res += 1
                q.append(num)
                visit.add(num)

        while q:
            num = len(q)
            for i in range(num):
                val = q.popleft()
                for j in range(len(digits)):
                    new_val = val + digits[j]
                    if int(new_val) <= n and new_val not in visit:
                        res += 1
                        q.append(new_val)
                        visit.add(new_val)

        return res
