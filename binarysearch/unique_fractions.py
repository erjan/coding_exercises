'''


You are given a list of lists fractions where each list contains [numerator, denominator] which represents the number numerator / denominator.

Return a new list of lists such that the numbers in fractions are:

In their most reduced terms. E.g. 8 / 6 becomes 4 / 3.
Any duplicate fractions that represent the same value are removed.
Sorted in ascending order by their value.
If the number is negative, the - sign should go to the numerator (the input also follows this).

'''

class Solution:
    def GCD(self, x, y):
        if y == 0:
            return x
        return self.GCD(y, x % y)

    def solve(self, fractions):
        s = set()
        vals = []
        for num in fractions:
            n = num[0]
            d = num[1]
            if n / d not in s:
                s.add(n / d)
                vals.append(num)
        vals = sorted(vals, key=lambda frac: frac[0] / frac[1])
        for ind in range(len(vals)):
            num = vals[ind]
            gcd = self.GCD(num[0], num[1])
            vals[ind][0] = num[0] // gcd
            vals[ind][1] = num[1] // gcd
        return vals
