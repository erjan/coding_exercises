'''
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.
'''

class Solution:
	def closestDivisors(self, num: int) -> List[int]:
		for i in range(int((num+2) ** (0.5)), 0, -1):  
			if not (num+1) % i: return [i, (num+1)//i] 
			if not (num+2) % i: return [i, (num+2)//i] 
		return []
  
--------------------------------------------------------------------------
def closestDivisors(self, num: int) -> List[int]:
    for i in range(round((num+1)**(0.5))+1, 0,-1):
        if (num+1)%i == 0:
            ans = [(num+1)//i, i]
            break
    for j in range(round((num+2)**(0.5))+1, 0,-1): 
        if (num+2)%j == 0:
            if abs((num+2)//j - j) < abs(ans[0]-ans[1]):
                ans = [(num+2)//j, j]
            break
    return ans
