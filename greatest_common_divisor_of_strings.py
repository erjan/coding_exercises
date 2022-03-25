'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        s1 = str1
        s2 = str2
        if len(s1) >= len(s2):
            s1, s2 = s2, s1
        print(s1)
        print(s2)

        div = math.gcd(len(s1), len(s2))

        print('gcd', div)

        if div == len(s1) == len(s2):
            if s1 != s2:
                print('not equal')
                return ''

        repeating_for_s1 = len(s1) // div
        print('repeating_for_s1', repeating_for_s1)

        repeating_for_s2 = len(s2)//div
        print('repeating_for_s2', repeating_for_s2)

        check = s1[:div]
        print('check', check)

        r1 = check * repeating_for_s1
        r2 = check * repeating_for_s2
        print(r1)
        print(r2)

        if r1 == s1 and r2 == s2:
            print('good')
            return check

        else:
            print('bad')
            return ''
