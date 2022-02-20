'''
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record.
'''

#my own solution

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        score = list()

        for i in range(len(ops)):
            print('-----------------')
            print(score)
            operation = ops[i]
            print('curr operation: %s' % operation)
            if operation.isnumeric() or operation[0] == '-':
                score.append(int(operation))
            elif operation == 'C':
                score.pop()
            elif operation == 'D':
                temp = score[-1]*2
                score.append(temp)
            elif operation == '+':
                temp = score[-1] + score[-2]
                score.append(temp)
        print()
        print(score)
        
        return sum(score)
