'''
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.
'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        DP = [0 for i in range(N+1)]
        for i in range(N-1, -1, -1):
            p, b = questions[i]
            DP[i] = max(p + DP[min(N, i + b + 1)], DP[i+1])
        return DP[0]
    
    
'''
For those who are still confused about why we should start from the last index instead of the first index

I have been confused by this question for a long time, too, until I realized the magic of the transition function.

Actually, the transition function itself will tell you which direction is right. Since our DP[i] need to be calculated by combination of some DP[i + ?], which means, we need to know the answer of DP[i+?] before DP[i]. So we should iterate from the last index. If your transition function give you DP[i] = combination of some DP[i-?], then you should start from the first index. If you got 
both directions? It will be very tricky and need to do some advanced transformation first, otherwise, it can't be solved by DP.      
'''
      

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions) # total number of questions
        memo = [-1] * n # memo array of size n. 
		# If memo[i] is not computed then its value must be -1 and we need to find memo[i]
		# If memo[i] != -1, this means we have already calculated this and we dont need to recompute it
        def rec_func(index, current_val) -> int: # index is the current question number to process and current_val is the max marks upto this question
            if index >= n: # It means that we have gone through all the questions thus return the current_val
                return current_val
            if memo[index] == -1: # memo[i] == -1, not computed before and so we need to solve it
                points = questions[index][0] # points for current question
                brainpower = questions[index][1] # brainpower for current question
                a = rec_func(index + brainpower + 1, points) # Recursive call considering we solve the current question
                b = rec_func(index + 1, 0) # Recursive call considering we skip the current question
                memo[index] = max(a, b) # choose which ever choice yields us the best result
            return current_val+memo[index]
        return rec_func(0, 0)
--------------------------------------------------------------------------------------------------------------------
'''
First create recursive solution :
Recursive solution has two parts:

Base part
Choices (which makes this problem recursive) can be also called as recurrence relation
Base
We reach the end so we cannot go any further so we return 0
Choices
Either we do not select this question the we move by one step.
Or we select the solution and move question[i][1] i.e number of brainpower.
Since the solution wants the maximum point we use max()
Using memoization technique to store already handled cases.
'''


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
		N = len(questions)
        
        memo = [-1 for x in range(N+2)]
        def solve(n):
            if n>=N:
                return 0
            if memo[n]!=-1:
                return memo[n]
            memo[n] = max(solve(n+1),solve(n+questions[n][1]+1)+questions[n][0])
            return memo[n]
        return solve(0)
      
