'''
Given an integer n, return a list of all 
simplified fractions between 0 and 1 (exclusive) such that the denominator 
is less-than-or-equal-to n. You can return the answer in any order.
'''


from math import gcd
class Solution:
	def simplifiedFractions(self, n: int) -> List[str]:
		result, denominator = [], 2
		visited = set()
		while denominator <= n:
			for numerator in range(1, denominator):
				fraction = numerator/denominator

				# gcd(numerator, denominator) == 1 means simplified cuz no value except 1 can divide both numbers to give integers
				# we can't have "0.5/1.2" as a simplified fraction right? So thats why gcd comes in handy
				if gcd(numerator, denominator) == 1 and fraction not in visited: 
					result += [str(numerator) + "/" + str(denominator)]
					visited.add(fraction)

			denominator += 1 

		return result
--------------------------------------------------------------------------------------------------------------------------------------------
def simplifiedFractions(self, n: int) -> List[str]:
    s = set() # record the unique fraction
    ans = []
    for i in range(2,n+1): # we search the denominator from small to large
        for j in range(1,i): # if a fraction is not simplified, its simplified version must be searched before 
            if j/i not in s:
                s.add(j/i)
                ans.append(str(j) + "/" + str(i))
    return ans
