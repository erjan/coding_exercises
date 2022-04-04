
'''

The profiler will execute your code by executing the command python main.py.

This problem does not require any input data, we will run your code once to 
determine whether the printed result is a multiplication table.

When printing, print the multiplication in the order 
of increasing Multiplier, Print the multiplication formula with 
the same multiplier on the same line, and print the multiplication
in the order of increasing multiplicand on the same line, and separate 
the adjacent multiplicand by a space, but there 
can be no Spaces at the end of the line.

'''

for i in range(1,10):

	for j in range(1,i+1):
		if j != i :
			print("%d*%d=%d" %(j,i,  i*j)  ,sep = ' ',  end = ' ')
		else:
			print("%d*%d=%d" %(j,i,  i*j)   , end = '')
	print()
