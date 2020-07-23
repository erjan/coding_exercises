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
    print_matrix(matrix)
    return matrix

def main():
    
    dimensions = input().split()
    dimensions = list(map(int, dimensions))

    n = dimensions[0]
    m = dimensions[1]
    
    matrix = record_matrix(n)

    result_coordinates = list()

    l = list()
    for i in range(n):
        for j in range(m):
            l.append(matrix[i][j])
    matrix_min = min(l)


    for i in range(n):
        for j in range(m):
            if matrix[i][j] == matrix_min:
                result_coordinates.append((i+1,j+1))
    print(result_coordinates)
    
    

main()
