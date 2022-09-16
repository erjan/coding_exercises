'''
A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 '''

class ComplexNumber:
        def __init__(self, string):
            real, imaginary = string.split('+')
            self.real = int(real)
            self.imaginary = int(imaginary[:-1])
            
        def __mul__(self, other):
            if type(other) is not ComplexNumber:
                raise NotImplementedError
            real = self.real*other.real+self.imaginary*other.imaginary*-1
            imaginary = self.real*other.imaginary+self.imaginary*other.real
            return ComplexNumber(f'{real}+{imaginary}i')
			
		__rmul__ = __mul__
        
        def __str__(self):
            return f'{self.real}+{self.imaginary}i'
            
class Solution:
                
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        return str(ComplexNumber(num1)*ComplexNumber(num2))
      
----------------------------------------------------------------
class Solution(object):
	def complexNumberMultiply(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""

		a_re, a_im = a.split('+')
		b_re, b_im = b.split('+')
		a_im, b_im = a_im[:-1], b_im[:-1]

		res_re = int(a_re)*int(b_re)-int(a_im)*int(b_im)
		res_im = int(a_re)*int(b_im)+int(a_im)*int(b_re)

		return str(res_re)+'+'+str(res_im)+'i'
