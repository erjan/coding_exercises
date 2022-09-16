'''
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.
'''

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
    	M = 0
    	for c in [[1,1],[1,-1],[-1,1],[-1,-1]]:
    		m = float('inf')
    		for i in [arr1[i]*c[0]+arr2[i]*c[1]+i for i in range(len(arr1))]:
    			if i < m: m = i
    			if i - m > M: M = i - m
    	return M
------------------------------------------------------------------------------------

class Solution:
    def helper(self,sign1, sign2, arr1, arr2):
        m1, m2 = -10**7, 10**7

        for i in range(len(arr1)):
            t = sign1*arr1[i] + sign2*arr2[i] + i
            m1 = max(m1,t)
            m2 = min(m2,t)

        return m1 - m2

    def maxAbsValExpr(self, arr1, arr2):
        res = 0

        res = max(res,self.helper(1,1,arr1,arr2))
        res = max(res,self.helper(-1,1,arr1,arr2))
        res = max(res,self.helper(1,-1,arr1,arr2))
        res = max(res,self.helper(-1,-1,arr1,arr2))

        return res
