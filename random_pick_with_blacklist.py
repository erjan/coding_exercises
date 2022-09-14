'''
You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

Implement the Solution class:

Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.
 
 '''


import random

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        if len(blacklist) > n//3:
            self.whitelist = list(set(range(0, n)) - set(blacklist))
        else:
            self.blacklist = set(blacklist)

    def pick(self) -> int:
        if hasattr(self, 'whitelist'):
            return random.choice(self.whitelist)
        while (rand:= random.randint(0, self.n - 1)) in self.blacklist:
            continue
        return rand
------------------------------------------------------------------------------------
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.max = n - len(blacklist)

    def pick(self) -> int:
        v = random.randint(0, self.max-1)
        l, r = 0, len(self.blacklist) - 1
        while l <= r:
            m = (l+r)//2
            if self.blacklist[m] <= v+m:
                l = m+1
            else:
                r = m-1
        return v + r + 1
