'''
There are two types of persons:

The good person: The person who always tells the truth.
The bad person: The person who might tell the truth and might lie.
You are given a 0-indexed 2D integer array statements of size n x n that represents the statements made by n people about each other. More specifically, statements[i][j] could be one of the following:

0 which represents a statement made by person i that person j is a bad person.
1 which represents a statement made by person i that person j is a good person.
2 represents that no statement is made by person i about person j.
Additionally, no person ever makes a statement about themselves. Formally, we have that statements[i][i] = 2 for all 0 <= i < n.

Return the maximum number of people who can be good based on the statements made by the n people.
'''

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        BAD, GOOD, NO_STATEMENT = 0, 1, 2
        N = len(statements)
        
        def hasContradiction(persons):
            for i in range(N):
                for j in range(N):
                    if statements[i][j] == NO_STATEMENT:
                        continue
                    if persons[i] == GOOD:
                        if statements[i][j] != persons[j]:
                            return True
            return False
        
        ans = 0
        def dfs(persons):
            nonlocal ans
            if len(persons) == N:
                if not hasContradiction(persons):
                    ans = max(ans, persons.count(GOOD))
            else:
                dfs(persons+[GOOD])
                dfs(persons+[BAD])
                
        dfs([])
        return ans
