'''
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.
'''

    def minimizeXor(self, num1, num2):
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if cmp(a, b) == cmp((1 << i) & num1, 0.5):
                res ^= 1 << i
                a -= cmp(a, b)
        return res
      
---------------------------------------------------------------------
def minimizeXor(self, num1, num2):
	ans = num1

	req = num2.bit_count()
	cur = num1.bit_count()

	v = 1
	while req > cur:
		if ans & v == 0:
			ans |= v
			cur += 1
		v <<= 1
	v = 1
	while req < cur:
		if ans & v:
			ans &= ~v
			cur -= 1
		v <<= 1

	return ans
