'''

You are given an integer n. A perfectly straight street is represented by a number line ranging from 0 to n - 1. You are given a 2D integer array lights representing the street lamp(s) on the street. Each lights[i] = [positioni, rangei] indicates that there is a street lamp at position positioni that lights up the area from [max(0, positioni - rangei), min(n - 1, positioni + rangei)] (inclusive).

The brightness of a position p is defined as the number of street lamps that light up the position p. You are given a 0-indexed integer array requirement of size n where requirement[i] is the minimum brightness of the ith position on the street.

Return the number of positions i on the street between 0 and n - 1 that have a brightness of at least requirement[i].

'''


'''
Instead of thinking about it as "the light is at index i and has a radius of r" -- once you calculate where the light starts and ends from those positions -- you can reframe it as "the light starts at position start and ends at position end.

Therefore, you can just create an array that keeps track of where the intensity increases (+1) and decreases (-1), and then do a prefix sum over that array and crossreference it with the requirements array after.
'''

class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        helper = [0] * (n + 1)
        for pos, _range in lights:
            helper[max(0, pos - _range)] += 1
            helper[min(n, pos + 1 + _range)] -= 1
        
        counter = 0
        res = 0
        for i in range(n):
            counter += helper[i]
            if counter >= requirement[i]:
                res += 1
        
        return res
        
        
        
-----------------
class Solution:
	def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
		lightsRange = [0] * (n + 1)
		res = 0
		for pos, ran in lights:
			lightsRange[max(0, pos - ran)] += 1
			lightsRange[min(n - 1, pos + ran) + 1] -= 1
		for i in range(n):
			lightsRange[i + 1] += lightsRange[i]
			if lightsRange[i] >= requirement[i]:
				res += 1
		return res
