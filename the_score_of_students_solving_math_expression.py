'''
You are given a string s that contains digits 0-9, addition symbols '+', and multiplication symbols '*' only, representing a valid math expression of single digit numbers (e.g., 3+5*2). This expression was given to n elementary school students. The students were instructed to get the answer of the expression by following this order of operations:

Compute multiplication, reading from left to right; Then,
Compute addition, reading from left to right.
You are given an integer array answers of length n, which are the submitted answers of the students in no particular order. You are asked to grade the answers, by following these rules:

If an answer equals the correct answer of the expression, this student will be rewarded 5 points;
Otherwise, if the answer could be interpreted as if the student applied the operators in the wrong order but had correct arithmetic, this student will be rewarded 2 points;
Otherwise, this student will be rewarded 0 points.
Return the sum of the points of the students.
'''

class Solution:
    def scoreOfStudents(self, s, answers):

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return {int(s[i])}
            res = {}
            for m in range(i + 1, j, 2):
                for a in dp(i, m - 1):
                    for b in dp(m + 1, j):
                        cur = a * b if s[m] == '*' else a + b
                        if cur <= 1000:  # opt with 0 <= answers[i] <= 1000
                            res[cur] = 2
            return res

        res = {**dp(0, len(s) - 1), **{eval(s): 5}}
        return sum(res.get(a, 0) for a in answers)
