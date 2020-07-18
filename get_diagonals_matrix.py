def print_matrix(m):
    for i in range(len(m)):
        print(m[i])
        

def m():
    matrix = list()
    n = int(input())
    for i in range(n):
        row = input().split()
        row = list(map(int, row))
        
        matrix.append(row)

    get_diagonal(matrix)
    
def get_diagonal(m):
    result = list()
    for row in range(len(m)):
        for j in range(len(m[row])):
            if row == j:
                     result.append(m[row][j])
                     
    for i in range(len(result)):
        print(result[i], end = ' ')

m()
