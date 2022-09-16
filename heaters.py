'''
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.
'''

Algorithm
After sorting the inputs, we loop through the houses and find the minimum distance to the left and right closests heaters.
We mantain a pointer to lookup at the closests heaters, while looping through the houses:

i represents the index of the closest left heater
i+1 represents the index of the closest left heater
Analysis
There is no extra space used.
Given the two sort methods used, the runtime complexity is min(NlogN, MlogM) where N and M are the sizes of the two inputs.
If the array were initially sorted, this algorithm would have linear runtime.

def findRadius(houses, heaters):    
	houses.sort()
    heaters.sort()
    N, i, maxRadius = len(heaters), 0, 0

	for house in houses:
		while i+1 < N and heaters[i+1] < house:
            i += 1
        maxRadius = max(maxRadius, min([abs(h-house) for h in heaters[i:i+2]]))    

    return maxRadius
  
-----------------------------------------------------------------------------------
class Solution:
    def findRadius(self, A, B):
        # 1) Pre-sorting Step
        A.sort()
        B.sort()
        #
        # 2) Main Algorithm
        last  = len(B) - 1
        x1,x2 = 0,0
        res   = 0
        for y in A:
            while x2 < last and y > B[x2]:
                x1, x2 = x2, x2+1
            d1,d2 = abs(B[x1] - y), abs(B[x2] - y)
            res   = max( res , min(d1,d2) )
        return res
