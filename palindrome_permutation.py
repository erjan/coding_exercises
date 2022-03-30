'''
Given a string s, return true if a permutation of the string could form a palindrome.

'''

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
            s = dict(Counter(s))
            print(s)

            s_val = list(s.values())

            count_odds = 0
            for i in range(len(s_val)):

                if s_val[i] % 2 == 1:
                    count_odds += 1
            print(count_odds)
            if count_odds > 1:
                return False
            return True
