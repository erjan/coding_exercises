import itertools
def f(num,d):
    
    
    strings = []
    for n in num:
        strings.append( d[n])
    res = []
    for el in itertools.product(*strings):
        print(el)

    #alternative
    results = [[]]
    for i in range(len(strings)):
        temp = []
        for res in results:
          for element in strings[i]:
            temp.append(res+[element])
        results = temp
    print(results)
        

d = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '7':['y', 't', 'w','z']}

f('23',d)
