'''
We have seen the applications of union, 
intersection, difference and symmetric difference operations, 
but these operations do not make any changes or mutations to the set.
'''


def f():
 
    
    a = int(input())
    s1 = set(map(int, input().split())) # here was a problem - i forgot to change to int, i had set( input().split()) so i got answer {7} and 7!!
    n = int(input())   
    

   
    for _ in range(n):
        
        oper_name,_ = input().split()
        s2 = set(map(int, input().split()))
        
        if oper_name == 'update' or oper_name == '|=':
            #print('update applied')
            s1.update(s2)
            #print(s1)
        elif oper_name == 'intersection_update' or oper_name == '&=' :
            #print('intersctino update applied')
            s1.intersection_update(s2)
            #print(s1)
        elif oper_name == 'difference_update' or oper_name ==  '-=' :
            #print('dif update applied')
            s1.difference_update(s2)
            #print(s1)
        elif oper_name == 'symmetric_difference_update' or oper_name == '^=':
            #print('sym dif update applied')
            s1.symmetric_difference_update(s2)
            #print(s1)

    
    #print(s1)
    print(sum(s1))
    
    

if __name__ == '__main__':


    f()
    
    
    
        
    
