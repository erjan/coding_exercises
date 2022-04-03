'''

Given a number n, return a list of all prime numbers smaller than or equal to n in ascending order.

'''


class Solution:
    def solve(self, n):

        res = list()

        for i in range(1, n + 1):
            if i > 1:
                for j in range(2, i):
                    if (i % j) == 0:
                        break
                else:
                    res.append(i)
        return res
      
      
#another

class Solution:
    def solve(self, n):
        prime = [True] * (n + 1)
        p = 2
        while p ** 2 <= n:

            if prime[p] == True:
                for i in range(p ** 2, n + 1, p):
                    prime[i] = False
            p += 1
        final = []
        for p in range(2, n + 1):
            if prime[p] == True:
                final.append(p)
        return final
