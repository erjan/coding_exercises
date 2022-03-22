'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
'''

#my own solution

class Solution:
    def thousandSeparator(self, n: int) -> str:
                n = str(n)

                q, r = divmod(len(n), 3)
                print(q, r)

                res = ''

                res = n[:r]
                print(res)
                remainder = n[r:]
                print(res)
                if r != 0:
                    res = n[:r] + '.'
                for i in range(0, len(remainder), 3):
                    res += remainder[i:i+3] + '.'
                res = res[:-1]
                print(res)
                return res
              
#another solution

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        s=s[::-1]
        res = '.'.join(s[i:i + 3] for i in range(0, len(s), 3))
        return res[::-1]
