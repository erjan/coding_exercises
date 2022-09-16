'''
You are given two positive integers left and right with left <= right. Calculate the product of all integers in the inclusive range [left, right].

Since the product may be very large, you will abbreviate it following these steps:

Count all trailing zeros in the product and remove them. Let us denote this count as C.
For example, there are 3 trailing zeros in 1000, and there are 0 trailing zeros in 546.
Denote the remaining number of digits in the product as d. If d > 10, then express the product as <pre>...<suf> where <pre> denotes the first 5 digits of the product, and <suf> denotes the last 5 digits of the product after removing all trailing zeros. If d <= 10, we keep it unchanged.
For example, we express 1234567654321 as 12345...54321, but 1234567 is represented as 1234567.
Finally, represent the product as a string "<pre>...<suf>eC".
For example, 12345678987600000 will be represented as "12345...89876e5".
Return a string denoting the abbreviated product of all integers in the inclusive range [left, right].
'''

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        num = 1
        while left<=right:
            num *= left
            left+= 1
        a = str(num)
        b = a.rstrip("0")
        e = len(a)-len(b)
        if len(b) > 10:
            b = b[:5]+"..."+b[-5:]
        return b+"e"+str(e)
      
----------------------------------------------------------------
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        mod = 1
        zeros = 0
        div = False
        for x in range(left, right + 1):
            mod *= x
            while not mod % 10:
                mod //= 10
                zeros += 1
            d, mod = divmod(mod, 10000000000)
            if d:
                div = True
        if not div:
            return f'{str(mod)}e{zeros}'
        else:
            log_sum = sum(math.log10(i) for i in range(left, right + 1))
            s = str(10 ** (log_sum % 1))
            leading = s[0] + s[2:6]
            return f'{leading}...{str(mod % 10 ** 5).zfill(5)}e{zeros}'
