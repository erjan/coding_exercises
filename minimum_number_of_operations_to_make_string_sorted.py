'''
You are given a string s (0-indexed You are asked to perform the following operation on s until you get a sorted string:

Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
Swap the two characters at indices i - 1 and j
Reverse the suffix starting at index i
Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.
'''

class Solution:
    def makeStringSorted(self, s: str) -> int:
        
        cnt, ans, tot, comb_tot = [0]*26, 0, 0, 1           # cnt - counter of the letters, tot - number of letters onward, comb_tot - see in the explanation 
        for cur_letter in s[::-1]:                          # Loop over all the letters from the end
            num = ord(cur_letter) - ord('a')                # Convert letter to number
            cnt[num] += 1                                   # Increment the counter for the current letter
            tot += 1                                        # Increment the number of letters from the current one onward
            comb_tot = (comb_tot * tot) // cnt[num]         # Iteratively update comb_tot
            ans = ans + (comb_tot * sum(cnt[:num]))//tot    # Add the number of combinations for all letters that are smaller than the current one
        return ans % 1_000_000_007
      
-----------------------------------------------------------
class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9+7
        count = [0] * 26
        res = 0
        base = 1
        divide = 1
        for i, ch in enumerate(reversed(s)):
            ind = ord(ch) - ord('a')
            count[ind] += 1
            base *= max(1, i)
            divide *= count[ind]
            m = math.gcd(base, divide)
            base //= m
            divide //= m
            res = (res + sum(count[:ind]) * base // divide) % MOD
        return res
