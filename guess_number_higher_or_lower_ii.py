'''
We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
'''


def getMoneyAmount(self, n):
    class Need(dict):
        def __missing__(self, (lo, hi)):
            if lo >= hi:
                return 0
            ret = self[lo, hi] = min(x + max(self[lo, x-1], self[x+1, hi])
                                     for x in range(lo, hi))
            return ret
    return Need()[1, n]
-------------------------------------------------------------------    

import functools
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def get_amount(left: int, right: int) -> int:
            if left >= right: return 0
            return min(i + max(get_amount(left, i - 1), get_amount(i + 1, right)) for i in range(left, right + 1))
        return get_amount(1, n)
      
--------------------------------------------
def getMoneyAmount(self, n):
    need = [[0] * (n+1) for _ in range(n+1)]
    for lo in range(n, 0, -1):
        for hi in range(lo+1, n+1):
            need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                               for x in range(lo, hi))
    return need[1][n]
