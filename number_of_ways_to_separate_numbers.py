'''
You wrote down many positive integers in a string called num. However, you realized that you forgot to add commas to seperate the different numbers. You remember that the list of integers was non-decreasing and that no integer had leading zeros.

Return the number of possible lists of integers that you could have written down to get the string num. Since the answer may be large, return it modulo 109 + 7.
'''

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        
        # counts[i][j] is what is the count for number starts at i and end at j-1
        n = len(num)
        counts = [[0] * (n+1) for _ in range(n)]
        for i in range(n):
            # the last number starting at i
            counts[i][n] = 1 if num[i] != '0' else 0
        
        def less(i, j, L):
            return num[i:i+L] <= num[j:j+L]
        
        ans = counts[0][n]
        for j in range(n-1, 0, -1): # start of the next number
            k, total = n, 0 # total will accumulate the sum from j=>[j,k)
            start = max(0, 2*j-k) # ignore all the previous starting number that cause range [i:j) > [j:k)
            for i in range(start, j): # start of the current number
                if num[i] != '0':
                    # ensure the number from [i,j) < [j,k)
                    while k-j > j-i or (k-j == j-i and less(i,j,j-i)):
                        total += counts[j][k]
                        total %= MOD
                        k -= 1
                        
                    counts[i][j] = total
                    
            ans += counts[0][j]
            ans %= MOD
            
        return ans
