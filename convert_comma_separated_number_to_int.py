'''
from exponential program - kazak devs - Elzhan Zeinulla, 22 oct 2022

convert  number to int. the number has commas separating every 3 digits:

1,700 = 1700
1,900,456 = 1900456

1 bln = 1000000000
1 trln = 1000000000000
'''

def f(s):

    s = s.split(',')
    temp = 0

    pow = 0

    s = s[::-1]  # O(n)
    for i in range(len(s)):
        temp += (10**pow) * int(s[i])
        pow += 3

    print(temp)


if __name__ == '__main__':

    s = '1,070'
    s = '1,567,003'
    s = '3,100,567,003'

    f(s)
