'''
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
You can only choose one of the actions per day.

Given the integer n, return the minimum number of days to eat n oranges.
'''

class Solution:
    def minDays(self, n):
        @lru_cache(None)
        def dfs(n):
            if n<=1:
                return n
                
            opt1, opt2, opt3 = float("inf"), float("inf"), float("inf")

            if n%3 == 0:
                opt3 = dfs(n//3)
            if n%2 == 0:
                opt2 = dfs(n//2)
            if n%2 or n%3:
                opt1 = dfs(n-1)

            return min(opt1,opt2,opt3) + 1

        return dfs(n)

---------------------------------------------------------------------------------------------------------
class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        q = [n]
        visit = set()
        visit.add(n)
        while q:
            for i in range(len(q)):
                num = q.pop(0)
                if num == 0:
                    return ans
                if num and (num-1) not in visit:
                    visit.add(num-1)
                    q.append(num-1)
                if num % 2 == 0 and num-(num//2) not in visit:
                    visit.add(num-(num//2))
                    q.append(num-(num//2))
                if num % 3 == 0 and num-2*(num//3) not in visit:
                    visit.add(num-2*(num//3))
                    q.append(num-2*(num//3))
            ans += 1
 

          
