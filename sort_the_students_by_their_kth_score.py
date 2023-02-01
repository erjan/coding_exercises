'''
There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.
'''


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> list[list[int]]:
        
        return sorted(score, key = lambda x: -x[k])
