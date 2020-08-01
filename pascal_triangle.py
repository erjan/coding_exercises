#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

def helper(d):

    res = []
    for i in range(len(d)-1):
        temp = d[i] + d[i+1]
        res.append(temp)
    res.insert(0,1)
    res.insert( len(res),1)
    
    return res


def main(n):
    res = []
    res.append([1])
    for i in range(1,n):
        prev = res[i-1]
        temp = helper(prev)
        res.append(temp)
    print(res)
        
main(5) 
#prints: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

