'''
Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

from statistics import median

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        # cost to serve specific houses with one mailbox
        def cost_one_box(houses):
            box = int(median(houses))
            return sum(abs(house - box) for house in houses)

        # C[i][j] = cost of serving houses 0...i with mailboxes 0...j
        C = [[0 for _ in range(k)] for _ in range(len(houses))]
        for j in range(k):
            C[0][j] = 0
        for i in range(len(houses)):
            C[i][0] = cost_one_box(houses[:i+1])
        
        # C[i][j] = min([C[i'][j-1] + cost of serving houses i'+1...i with mailbox j] for i' in [0 (or j-1)...i-1]) 
        for i in range(1, len(houses)):
            for j in range(1, k):
                C[i][j] = min(C[_i][j-1] + cost_one_box(houses[_i+1:i+1]) for _i in range(min(i-1,j-1), i))
                
        return C[-1][-1]
                

----------------------------------------------------------------------------------------------------------------------------
Firstly we will create cost[i][j].

cost[i][j] = total travel distance by putting one mailbox in between i & j houses.

It means cost[i][j] is the total travel distance from between houses[i:j] to a mailbox when putting the mailbox among houses[i:j], the best way is put the mail box at median position among houses[i:j].

Now after creating costs table, we can directly go with the number of mailboxes left and starting index of the free houses.

It's something like backtracking.

We are checking each possible combination of putting the mailbox.

Since constraint is low, we can go with O(n^3).

'''

class Solution:
def minDistance(self, houses: List[int], k: int) -> int:
    
    n = len(houses)
    houses.sort()
    cost = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            mid_house = houses[(i+j)//2]
            for t in range(i,j+1):
                cost[i][j]+= abs(mid_house-houses[t])
    
    @lru_cache(None)
    def dp(k,ind):
        if k==0 and ind==n: return 0
        if k==0 or ind==n: return float('inf')
        res = float('inf')
        for j in range(ind,n):
            c = cost[ind][j]
            res = min(res, c + dp(k-1,j+1))
        
        return res
    
    return dp(k,0)
