class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit+1):     
            for j in range(limit+1):
                if 0<= n-i-j<=limit:
                    res+=1
                
        return res

----------------------
#true brute force

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        res += 1
        return res
