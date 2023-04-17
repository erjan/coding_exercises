'''
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.

Return an array containing the index of the row, and the number of ones in it.
'''


#this is bs and hard to grokk!
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:    
        ones = 0 
        index = 0
        for it, row in enumerate(mat):
            c = row.count(1)
            if ones < c:
                ones = c
                index = it
        
        return [index,ones]

------------------------------------------------------------------------------
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        resi = 0
        rescnt = 0
        for i,row in enumerate(mat):
            cnt = row.count(1)
            if cnt > rescnt:
                resi = i
                rescnt = cnt
        return resi, rescnt
