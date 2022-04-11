'''
A bottle of wine is 55 yuan, and 55 wine bottles can be exchanged for a bottle of wine. How many bottles of wine can I drink at most for n yuan?
'''

n = int(input())

a=n//5
b=a
while b>=5:
	a += b//5
	b = b%5 + b//5

print(a)
