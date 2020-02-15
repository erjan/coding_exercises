'''
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube_i is on top of cube_j then cube_j >= cube_i.

When stacking the cubes, you can only pick up either the 
leftmost or the rightmost cube each time. Print "Yes" if it is 
possible to stack the cubes. Otherwise, print "No". 
Do not print the quotation marks.
'''

#time out solution - too long, because O(n^2) for long test cases

def f(r):    
    cur = list()
    found = False
    for i in range(len(r)):
        if len(r)!= 0:
            leftmost = r[0]
            rightmost = r[-1]
            if len(cur) == 0:
                cur.append(r.pop(0))
            else:                
                if max(cur) < leftmost or max(cur) < rightmost:
                    print('No')
                    found = True
                    break
                else:
                    if leftmost >= rightmost:
                        cur.append(r.pop(0))
                    else:
                        cur.append(r.pop(-1))
    if found == False:                        
        print('Yes')
        
        
        
if __name__ == '__main__':    

    n = int(input())
    total_list = list()
    for _ in range(n):
        length = int(input())
        l = list(int(i) for i in input().split(' '))
        total_list.append(l)
        
    for l in total_list:
        f(l)
