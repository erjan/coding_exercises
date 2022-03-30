'''
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return true if it is a confusing number, or false otherwise.
'''


class Solution:
    def confusingNumber(self, n: int) -> bool:
            old_n = n

            n = str(n)

            if '2' in n or '3' in n or '4' in n or '5' in n or '7' in n:
                print('invalid')
                return False

            n = list(n)
            res = [0] * len(n)

            for i in range(len(n)):
                if n[i] == '9':
                    res[i] = '6'

                elif n[i] == '8':
                    res[i] = '8'

                elif n[i] == '1':
                    res[i] = '1'

                elif n[i] == '0':
                    res[i] = '0'

                elif n[i] == '6':
                    res[i] = '9'

            res = ''.join(res)

            res = res[::-1]
            res = int(res)
            old_n = int(old_n)
            print(old_n, type(old_n))
            print(res, type(res))

            if old_n != res:
                print('confusing number')
                return True
            return False
          
          
          
#another

def confusingNumber(N):
	x, y, cmap = N, 0, {0:0,1:1,6:9,8:8,9:6}
	while N:
		n, m = divmod(N, 10)
		if m not in cmap: return False
		N, y = n, y*10 + cmap[m]
	return x != y

#another

class Solution:
    def confusingNumber(self, N: int) -> bool:
        flipped = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        N_flipped = 0
        n = N
        while n:
            n, digit = divmod(n, 10)
            if digit not in flipped:
                return False
            N_flipped = 10 * N_flipped + flipped[digit]
        
        return N != N_flipped
      
      
#another

class Solution:
    def confusingNumber(self, N: int) -> bool:
        s = str(N)
        turned = s[::-1].translate(s.maketrans('0123456789', '01----9-86'))
        return '-' not in turned and s != turned
