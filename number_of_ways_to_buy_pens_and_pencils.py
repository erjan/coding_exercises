'''
You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.

Return the number of distinct ways you can buy some number of pens and pencils.
'''

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0;
        penscost = 0;
        while penscost <= total:
            remainingAmount = total - penscost;
            pencils = remainingAmount//cost2 + 1;
            ways += pencils;
            penscost += cost1;
        return ways
      
-----------------------------------------
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        x=max(cost1,cost2)
        y=min(cost1,cost2)
        z=total//y
        count=1
        for i in range(z):
            a=total
            #print(count)
            a-=(y*i)
            z1=a//x+1
            count+=z1
            #print(count,z1)
        
        return count
      
------------------------------------------------------
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        dp=[1]*(total+1)
        dp[0]=1
        
        for coin in [cost1, cost2]:
            for i in range(coin, total+1):
                dp[i]+=dp[i-coin]
                
        return dp[-1]
