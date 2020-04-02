def shift(a):
    last = a[-1]
    a.insert(0, last)
    a.pop()
    return a


def f(a,b):
    a = list(a)
    b = list(b)

    for i in range(len(a)):
        a = shift(a)
        if a == b:
            return True
        
    return False    


f('abcde', 'abced')
