 '''
 You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

 
 '''
 
 
 class Solution(object):
 	def splitIntoFibonacci(self, S):
 		"""
 		:type S: str
 		:rtype: List[int]
 		"""
 		def helper(S, temp):
 			if self.res:
 				return
 			if not S and len(temp)>2:
 				self.res =  temp
 				return
 			for i in range(len(S)):
 				if S.startswith('0') and i > 0:
 					break
 				if int(S[:i+1]) > 2**31-1:
 					break
 				if len(temp) < 2 or (len(temp) >= 2 and int(S[:i+1]) == int(temp[-1])+int(temp[-2])):
 					temp.append(S[:i+1])
 					helper(S[i+1:], temp[:])
 					temp = temp[:-1]


 		if not S:
 			return None

 		self.res = None
 		helper(S, [])

 		return self.res
