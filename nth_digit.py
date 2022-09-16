'''
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
'''

def findNthDigit(self, n: int) -> int:
	temp = 0
	i = 1
	while(temp + i*(10**i - 10**(i-1)) < n):
		temp += i*(10**i - 10**(i-1))
		i += 1
	d = i
	n -= temp
	num = n//d
	done = str(10**(d-1)-1 + num + int(n%d > 0))
	if(n % d):
		return done[n%d - 1]
	return done[-1]
