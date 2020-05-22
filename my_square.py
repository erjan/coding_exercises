#prints my square of given length and width
'''
o--------o
|        |
|        |
|        |
|        |
|        |
|        |
|        |
|        |
o--------o
'''

def f(x, y):
    for i in range(x):
        for j in range(y):
            if i == 0 and j == 0:
                print('o', end = '')
            elif (i == 0 and j == y-1):
                print('o', end = '')
            elif(i == 0 and j > 0 and j < y-1):
                print('-', end = '')
            elif(i > 0 and j == 0 and i != x-1):
                print('|', end = '')
            elif(i > 0 and j == y-1 and i != x-1):
                print('|', end = '') 
            elif(i == x-1 and j == 0):
                print('o', end = '')
            elif(i == x-1 and j == y -1):
                print('o', end =  '')
                
            elif(i == x-1 and j > 0 and i > 0):
                #print('got here')
                print('-', end = '')
                
            else:
                print(' ', end = '')
        print()


a = 3
b = 5
f(10,10)
