import random

def generate_num_1_10():
        return random.randrange(0,10,1)

def generate_row():
        row = []
        for i in range(10):
                row.append(generate_num_1_10())
        return row

def generate_matrix():
        matrix = list()
        for i in range(10):
                matrix.append(generate_row())
        return matrix

def print_matrix(m):
        for row in range(len(m)):
                print()
                print(m[row])



def get_back_diagonal(m):
        sum_diag = 0 
        for row in range(len(m)):
                count = len(m)-1 - row
                #print(count)
                for j in range(len(m[row])):
                        #print(m[row][count], end = ' ')
                        sum_diag += m[row][count]
                        count -=1
                        break
        return sum_diag
                               
def get_diagonal(m):
        sum_diag = 0
        for row in range(len(m)):
                #print(row)
                for j in range(len(m[row])):
                        if row == j:
                                #print(m[row][j],end = ' ')
                                sum_diag += m[row][j]
        return sum_diag
                        
                        
if __name__ == '__main__':
        matrix = []
        n = int(input())
        for row in range(n):
                cur_row = [ int(i) for i in input().split(' ')]
                matrix.append(cur_row)

        d1 = get_diagonal(matrix)
        d2 = get_back_diagonal(matrix)
        print( abs(d1-d2))

        #print_matrix(matrix)
        '''
        m = generate_matrix()
        print_matrix(m)
        print()
        print()
        d1 = print_diagonal(m)
        d2 = print_back_diagonal(m)
        print(d1)
        print(d2)
        print( abs(d1-d2))
        '''
        
