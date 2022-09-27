'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.
'''

class Solution:
    def find_next_palindrome(self, n, additive):
        l = len(n)
        if l == 0:
            return 0
        first_half = str(int(n[:l // 2 + l % 2]) + additive)
        return int(first_half + first_half[(-1 - l%2)::-1])
            
    def nearestPalindromic(self, n: str) -> str:
        m = int(n)
        candidates = [self.find_next_palindrome(n, additive) for additive in range(-1, 2)] # Cases 1, 2, and 3
        candidates.append(self.find_next_palindrome("9"*(len(n)-1), 0)) # Case 4
        candidates.append(self.find_next_palindrome("1" + "0"*len(n), 0)) # Case 5

        ans = None
        for t in candidates:
            if t == m:
                continue
            if ans is None or abs(ans - m) > abs(t - m) or (abs(ans - m) == abs(t - m) and t < m):
                ans = t
        return str(ans)
