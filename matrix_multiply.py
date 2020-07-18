def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end = ' ')
        print()
        

def record_matrix(n):
    matrix = list()
    
    for i in range(n):
        row = input().split()
        row = list(map(int, row))
        
        matrix.append(row)
    #print_matrix(matrix)
    return matrix

def main():
    
    dimensions1 = input().split()
    dimensions1 = list(map(int, dimensions1))

    n = dimensions1[0]
    m = dimensions1[1]
    
    matrix1 = record_matrix(n)


    dimensions2 = input().split()
    dimensions2 = list(map(int, dimensions2))

    m2 = dimensions2[0]
    l = dimensions2[1]

    
    matrix2 = record_matrix(m2)



    result = list()
    for i in range(n):
        row = list()
        for j in range(l):
            row.append(0)
        result.append(row)
    
    for i in range(n):
        for j in range(l):
            for k in range(m2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    print_matrix(result)

main()
