
from itertools import groupby
def helper(s):
    s = ''.join(s)

    res = []
    t = list(''.join(group) for key, group in groupby(s))
    for i in range(len(t)):
        res.append(  t[i][0] + str(len(t[i])) )

    for i in range(len(res)):
        letter = res[i][0]
        num = int(res[i][1:])
        if num == 1:
            res[i] = letter


    final = list()
    for i in range(len(res)):
        letter = res[i][0]
        num = res[i][1:]
       
        final.append(letter)
        if num :
            final.extend(list(num))

    print(len(final))
    print(final)
    return (final)

e = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
e = ["a","a","b","b","c","c","c"]
#e = ['a']
helper(e)
