'''

Given a positive integer n, with n 
as the side length, please output the sequence
number from left to right and top to bottom through 
the output statement to form a square matrix, the sequence 
number starts from 1, and the two sequence numbers are separated 
by a space , No spaces are added at the end of each line.

'''

n = int(input())

res = list()
c = 1
for i in range((n)):

	temp = list()

	for j in range((n)):

		temp.append(c)
		c+=1
	res.append(temp)

for i in range(n):
	for j in range(n):
		if j != n-1:
			print(res[i][j], sep = ' ',  end = ' ')
		else:
			print(res[i][j], sep = ' ',  end = '')
	print()


----------------------------------
n = int(input())
for i in range(n):
    l = []
    for j in range(1,n+1):
        l.append(str(i*n+j))
    print(' '.join(l))
