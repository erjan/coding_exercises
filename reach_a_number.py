'''
You are standing at position 0 on an infinite number line. There is a destination at position target.

You can make some number of moves numMoves so that:

On each move, you can either go left or right.
During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.
'''

class Solution: 
  def  reachNumber(self,target):
    jumpCount = 1 
    sum = 0 
    while sum<abs(target):
      sum+=jump 
      jumpCount+=1 
    
    if (sum-target)%2==0: return jumpCount-1 
    else:
      
      if ((sum+jumpCount)-target)%2==0: 
        return jumpCount
      else:
        return jumpCount+1 
      
---------------------------------------------------------------------------

class Solution:
    def reachNumber(self, target: int) -> int:
        ans, k = 0, 0
        target = abs(target)
        while ans < target:
            ans += k
            k += 1
        while (ans - target) % 2:
            ans += k
            k += 1
        return k - 1  
