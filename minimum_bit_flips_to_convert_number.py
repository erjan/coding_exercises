
'''

A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
'''


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        binstart = bin(start)[2:]
        bingoal = bin(goal)[2:]
        
        count= 0
        
        mini = min(len(binstart), len(bingoal))
        
        if len(binstart) < len(bingoal):
            diff = abs(len(bingoal) - len(binstart))
            binstart = diff * '0' + binstart
        else:
            diff = abs(len(bingoal) - len(binstart))
            bingoal = diff * '0' + bingoal
            
            
        binstart = list(binstart)
        bingoal = list(bingoal)
        for i in range(len(binstart)-1,-1,-1):
            
            if binstart[i] != bingoal[i]:
                binstart[i] = str(int(binstart[i]) ^ int(bingoal[i]))
                count+=1
        return count
            
            
            
        
#another

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (bin(start^goal).count("1"))
      
      
      
#another - using rjust

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        total = 0

        for a, b in zip(bin(start)[2:].rjust(32, '0'), bin(goal)[2:].rjust(32, '0')):
            if a != b:
                total += 1

        return total
        
        
        
