'''
You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

Here's the function signature:

def word_search(matrix, word):
  # Fill this in.
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print word_search(matrix, 'FOAM')
# True
'''

import random
def check_verticals(m,target):    
    for row in range(len(m[0])):
        cur_row = []
        for j in range(len(m[0])):
            cur_row.append(m[j][row])
        cur_row = ''.join(cur_row)
        if target in cur_row:
            return True
            break
        
def check_rows(m,target):
    for row in m:
        row_str = ''.join(row)
        if target in row_str:
            return True
            break
    
def generate_matrix(l):
    m = list()
    
    for i in range(4):
        d = random.choice(l)
        m.append(list(d))

    return m

if __name__ == '__main__':
    t = ['fing','sorn','rita', 'foam','zing','xing', 'jack', 'john', 'laud', 'born', 'jane']
    m = generate_matrix(t)
    target = 'h'
    if (check_verticals(m,target) or check_rows(m, target)):
        print(True)
    else:
        print(False)
    
        
    
