def generate(k):
    
    if k <=33:
        if k == 0:
            print('zero ')
            print([1])
            return [1]
        
        print(generate_helper(k)[k])
        return generate_helper(k)[k]
    else:
        return None


def generate_helper(numRows):
    res = []
    res.append([1]) 
    if numRows == 0:
        return []
        
    for i in range(1,numRows+1):
        prev = res[i-1]
     
        t = []
        for i in range(len(prev)-1):
            temp = prev[i] + prev[i+1]
            t.append(temp)
        t.insert(0,1)
        t.insert( len(t),1)

        res.append(t)
    #print(res)
    return res

generate(0)
