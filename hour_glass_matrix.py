#hour glass matrix is of the form:
a b c
  e
f g h

def printer(hg):
    print('---------------')
    top = hg[0]
    middle = hg[1]
    bottom = hg[2]
    print(top)
    print('    %d' % middle)
    print(bottom)
    
def f(m):
    max_sum = []
    for i in range(len(m)-2):
        for j in range(len(m[0])-2):
            if i <= len(m):
                if j <= len(m[0]):
                    top = m[i][j:j+3]
                    middle = m[i+1][j+1]
                    bottom = m[i+2][j:j+3]
                    cur_max = sum(top) + middle + sum(bottom)
                    max_sum.append(cur_max)                    

                    
                    printer([top, middle, bottom])
    print(max(max_sum))
    return max_sum
                    

m = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
    ]


m = [[1,2,3],[4,5,6],[7,8,9]]



m =[
 [-9, -9, -9,  1,1,1 ],
 [0, -9,  0,  4, 3, 2],
 [-9, -9, -9,  1, 2, 3],
 [0 , 0 , 8 , 6, 6, 0],
 [0,  0,  0, -2, 0, 0],
 [0,  0 , 1,  2 ,4, 0]
 ]

m = [
[-1 ,-1, 0 ,-9 ,-2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]
]




f(m)
                    
