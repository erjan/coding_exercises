
def check_empty(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '-':
                return False
    return True




def check_diag(grid):
    
    diag1 = [grid[0][0], grid[1][1], grid[2][2]]
    if diag1 == ['X', 'X', 'X'] :
        #print('diag1')
        print('player a wins ')
        return 'A'
    if diag1 == ['0', '0', '0']:
        #print('diag1')
        #print('player b wins')
        return 'B'
    
    diag2 = [grid[0][2], grid[1][1], grid[2][0] ]
    if diag2  == ['X', 'X', 'X']:
        #print('diag2')
        print('player a wins')
        return 'A'
    if diag2 == ['0', '0', '0']:
        #print('diag2')
        #print(' player b wins')
        return 'B'
    
    #print('no diag detected')
    return 'c'



def check_rows(grid):
    for i in range(3):
        row = grid[i]
        if row == ['X', 'X', 'X']:
            #print('row X %d player a win' % i)
            return 'A'
            
        elif row == ['0', '0', '0']:
            #print('row o %d player b win' % i)
            return 'B'
                
    #print('no win row detected')
    return 'c'
    
            
def check_columns(grid):
    for i in range(3):
        x = 0
        y = 0
        for j in range(3):
            if grid[j][i] == 'X':
                x+=1
            elif grid[j][i] == '0':
                y+=1
        if x == 3:
            #print('column X win detected')
            return 'A'
        elif y == 3:
            #print('column O win detected')
            return 'B'
    #print('no win columns')
    return 'c'
                

def check_all(grid):
    cols = check_columns(grid)
    rows = check_rows(grid)
    diags = check_diag(grid)

    if cols != 'c':
        #print('cols not win')
        return cols
    elif rows != 'c':
        #print('rows not win')
        return rows
    elif diags!= 'c':
        #print('diags not win')
        return diags


def check_draw_pending(grid):
    
    if check_empty(grid):
        print('Draw')
        return 'Draw'
    else:
        print('Pending')
        return 'Pending'
        





def print_grid(grid):
    #print('--------------------------------------------')
    for i in range(3):
        for j in range(3):
            print(grid[i][j], end = ' ')
        print()

        
def f(moves): 
    grid = []
    for i in range(3):
        grid.append(['-'] * 3)

    a_player = True

    for move in moves:
        x = move[0]
        y = move[1]


        if grid[x][y] == '-':
            if a_player:
                grid[x][y] = 'X'
                a_player = False
                if check_all(grid) == 'A':
                    print('A')
                    #print_grid(grid)
                    return 'A'
                

                
            elif not a_player:
                grid[x][y] = '0'
                a_player = True
                if check_all(grid) == 'B':
                    print('B')
                    #print_grid(grid)
                    return 'B'
        #print_grid(grid)



    #print('checking draw pending')
    #print_grid(grid)
    return check_draw_pending(grid)

                
        
            


moves_bwins = [ [1,1], [2,0], [0,0], [2,1], [0,2], [2,2] , [1,0]]

moves_bwins2 = [ [1,1], [0,0], [0,2], [1,0], [1,2], [2,0] ]

moves_bwins3 = [  [2,0], [1,1] , [1,0], [0,0], [2,1] ,[2,2] ]

move_pending = [[0,0],[1,1]]

moves_draw = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]

f(moves_draw)
