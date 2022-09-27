'''
You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 <= m <= n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

Given an integer array machines representing the number of dresses in each washing machine from left to right on the line, return the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.
'''

from itertools import accumulate
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        summation = sum(machines)
        if summation%n:
            return -1
        avg = summation//n
        left = list(accumulate(machines))
        result = 0
        for i in range(n):
            move_to_right = max(left[i] - (i+1)*avg, 0) 
            move_to_left = max(left[-1]-(left[i-1] if i!=0 else 0) - (n-i)*avg, 0)
            result = max(result, move_to_right + move_to_left)
        return result
