'''
Your code needs to read data n, m and n parameters from the standard input stream (console) in the form of A B C D. You need to calculate a matrix of n * m, the matrix element calculation formula is

M[i][j]= \begin{cases} C[i]& \text{j = 0}\\ (A[i] * M[i][j - 1] + B[i]) \ \%\ D[i] & \text{j != 0} \end{cases}M[i][j]={ 
C[i]
(A[i]∗M[i][j−1]+B[i]) % D[i]
  
j = 0
j != 0

 among them, M[i][j] is the element of i row and j column in the required matrix, A[i], B[i], C[i] and D[i] is the input parameter. After calculating the result, print the matrix to the standard output stream (console).
'''

# write your code here
# read data from console

# output the answer to the console according to the requirements of the question


n = int(input())
m = int(input())

t = list()
for _ in range(n):
	q = list(input().split())
	q = list(map(int, q))
	t.append(q)


M = [ [0 for i in range(m)] for j in range(n) ]


for i in range(n):
	for j in range(m):

		if j == 0:
			M[i][j] = t[i][2]
		else:
			M[i][j] = (t[i][0] * M[i][j-1] + t[i][1])% t[i][3]

#printing the matrix

for r in M:
	print(*r)
