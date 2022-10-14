'''
You are given an m x n integer matrix mat and an integer target.

Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.

Return the minimum absolute difference.

The absolute difference between two numbers a and b is the absolute value of a - b.
'''


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        possibleSum = set([0])
        for m in mat:
            temp = set()
            for y in possibleSum:
                for x in sorted(set(m)):
                    temp.add(x+y)
                    if x+y>target:
                        break
            possibleSum = temp
        return min(abs(s-target) for s in possibleSum)
