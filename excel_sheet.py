#Given a positive integer, return its corresponding column title as appear in an Excel sheet.

'''
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB

'''


import string
def f(n):
    x = string.ascii_lowercase.upper()
    res = dict(list(enumerate(x, start = 1)))
    #print(res)
    result = ''


    if n < 27:
        print('basic case hit')
        print(res[n])
        return res[n]
    while True:
        if n < 26:
            result += res[n]
            result = result[::-1]
            print(result)

            return result
        remainder = n % 26
        print('remainder %d ' % remainder)
        if remainder == 0:
            remainder = 26
        result += res[remainder]
        n = n//26

#d = dict(list(enumerate(string.ascii_lowercase.upper(),start=1)))
        
def helper(n, res):
    if n < 26:
        res += d[n]
        return res[::-1]
    res += d[n%26]
    return helper(n//26, res)
    
def rec(n):
    d = dict(list(enumerate(string.ascii_lowercase.upper(),start=1)))
    print(d)
    r = helper(n,'')
    print(r)
    return r
        

f(28)
