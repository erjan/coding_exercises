'''
We have two arrays arr1 and arr2 which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:

arr1 contains uniqueCnt1 distinct positive integers, each of which is not divisible by divisor1.
arr2 contains uniqueCnt2 distinct positive integers, each of which is not divisible by divisor2.
No integer is present in both arr1 and arr2.
Given divisor1, divisor2, uniqueCnt1, and uniqueCnt2, return the minimum possible maximum integer that can be present in either array.
'''


class Solution: 
	def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int: 
		lo, hi = 0, 1<<32-1
		mult = lcm(divisor1, divisor2)
		while lo < hi: 
			mid = lo + hi >> 1
			if uniqueCnt1 <= mid - mid//divisor1 and uniqueCnt2 <= mid - mid//divisor2 and uniqueCnt1+uniqueCnt2 <= mid - mid//mult: hi = mid
			else: lo = mid+1
		return lo 
  
---------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l,  r = 0, 1 << 32 - 1

        lcm = math.lcm(divisor1, divisor2)
        def valid(num):
            div1 = num - num // divisor1
            if div1 < uniqueCnt1: 
                # there isn't enough number between 1 to num that are not divisible by divisor1
                return False
            div2 = num - num // divisor2 
            if div2 < uniqueCnt2: 
                # there isn't enough number between 1 to num that are not divisible by divisor2
                return False
            union = num - num // lcm
            #  num // lcm: none wowrks, num: total, union: total - none works
            if union < (uniqueCnt1 + uniqueCnt2):
                # Numbers from the range [1,L] that are multiples of both C1 and C2 (thus, multiples of lcm(D1,D2)) should be skipped, thus, increasing the candidate value by 1.
                return False
            return True

        while l + 1 != r:
            m = (l + r) // 2
            if (valid(m)):
                r = m 
            else:
                l = m
        return r
            
