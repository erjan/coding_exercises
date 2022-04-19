'''
A stepping number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.

For example, 321 is a stepping number while 421 is not.
Given two integers low and high, return a sorted list of all the stepping numbers in the inclusive range [low, high].
 
'''


DFS
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        def dfs(n):
            if n > high: 
                return 
            if n >= low:
                q.add(n)
            d = n % 10
            if d == 0:
                dfs(n * 10 + 1)
            elif d == 9:
                dfs(n * 10 + 8)
            else:
                dfs(n * 10 + d + 1) 
                dfs(n * 10 + d - 1)
        q = set()
        for i in range(10):
            dfs(i)
        return sorted(q)
Queue
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q1, q2 = set(), collections.deque(range(10))
        while q2:
            n = q2.popleft()
            if low <= n <= high:
                q1.add(n)
            if n < high:
                d = n % 10
                if d == 0:
                    q2.append(n * 10 + 1)
                elif d == 9:
                    q2.append(n * 10 + 8)
                else:
                    q2.append(n * 10 + d + 1)
                    q2.append(n * 10 + d - 1)
        return sorted(q1)
--------------------------------------------------------------------------------
Commentary
The idea is to start with all the numbers in [1, 9] and compute new numbers from them and check if they're between low and high. For any number n, we can create new numbers by taking the right most digit, i.e. mod 10 and check if we can increase the last digit increase 1 or if we can decrease the last digit by 1. We can only increase the last digit if the last digit isn't 9. Same for decreasing if the last digit isn't 0. The reason we don't include 0 in the initial range is because we would double count for all of 0's children.

Analysis
To analyze the runtime, notice with this method we are essentially doing BFS on a tree with numbers in the range [1, high]. The amount of levels the tree has is ~log(high) and each node in our tree has 2 children (except when least significant digit is 0 or 9). This gives us O(2^(log(n))) runtime if n is high.

Solution
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        
        def bfs(low, high, res):
            q = collections.deque(range(1,10))
            while q:
                n = q.popleft()
                if low <= n <= high:
                    res.append(n)
                if n < high:
                    r = n % 10
                    n *= 10
                    if r != 0:
                        q.append(n+r-1)
                    if r != 9:
                        q.append(n+r+1)
                        
        res = []
        if low == 0:
            res.append(0)
        bfs(low, high, res)
        return res
        
----------------------------------------------------------------------------------------------
Approach1 : DFS Backtracking + Sorting - Time - O(n) Space - O(h)

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        maxlen = len(str(high))
        self.res = []
        
        def solve(now):
            if int(now) >= low and int(now) <= high: 
                self.res.append(int(now))
            if len(now) == maxlen:
                return
            lastdigit = int(now[-1])
            minus = lastdigit-1
            plus = lastdigit+1
            if minus >= 0:
                solve(now+str(minus))
            if int(plus) <10 :
                solve(now+str(plus))

        for i in range(1,10):
            solve(str(i))
        
        append = [] if low > 0 else [0]
        return sorted(append+self.res)
Approach 2 : BFS without any sorting - Time - O(n) Space - O(n)

from collections import deque
class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        maxlen = len(str(high))
        self.res = []
        q = deque([])
        for i in range(1,10):
            q.append(str(i))
        while q:
            now = q.popleft()
            if int(now) >= low and int(now) <= high: 
                self.res.append(int(now))
            if len(now) < maxlen:
                lastdigit = int(now[-1])
                minus = lastdigit-1
                plus = lastdigit+1
                if minus >= 0:
                    q.append(now+str(minus))
                if int(plus) <10 :
                    q.append(now+str(plus))
        append = [] if low > 0 else [0]
        return append+self.res
        
        
