'''
You are given a positive integer n, that is initially placed on a board. Every day, for 109 days, you perform the following procedure:

For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
Then, place those numbers on the board.
Return the number of distinct integers present on the board after 109 days have elapsed.
'''


class Solution:
    def distinctIntegers(self, n: int) -> int:
        board = set()
        board.add(n)
        remaining = set()
        for i in range(2,n):
            remaining.add(i)
        day = 1
        while len(remaining) > 0 and day < pow(10,9):
            removing = set()
            for candidate in remaining:
                for num in board:
                    if num%candidate == 1:
                        board.add(candidate)
                        removing.add(candidate)
                        break
            for num in removing:
                remaining.remove(num)
            day += 1
        return len(board)
