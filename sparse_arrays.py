#There is a collection of 
#input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings

def f():
    
    strings = ['aba', 'baba', 'aba', 'xzxb']
    queries = ['aba', 'xzxb', 'ab']
    
    res = []
    '''
    for q in queries:
        total= 0
        for s in strings:
            if s == q:
                
                total+=1
        res.append(total)
    '''
    for q in queries:
        res.append(len(list(filter(lambda s: s == q, strings))))
        
    print(res)        
    return res


f()

#2nd solution

def matchingStrings(strings, queries):
    res = []

    for q in queries:
        total = 0
        for s in strings:
            if s == q:
                total+=1
        res.append(total)
    return res
