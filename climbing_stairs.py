'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
 
        if n == 0:
            return 0
        if n == 1:
            return 1
               
        else:
            ways = [0,1]
            
            for i in range(2,n+2):
                ways.append(ways[i-1] + ways[i-2] )
            print(ways)
            return ways[len(ways)-1]
        
# i did not solve it myself, but important tip: just look at the logic of climbing! we can go 1 step back or 2 step backs. hence the relation

# https://www.youtube.com/watch?v=uHAToNgAPaM minute 4-5
