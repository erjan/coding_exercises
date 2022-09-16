'''
Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

 
'''

class Solution(object):
    def numOfBurgers(self, t, c):
        
        if t==c==0:
            return [0,0]
        four=(t-2*c)//2  # no of jumbo burgers by solving 4x+2y=t and x+y=c
        two=c-four #number of small burgers
        if c>=t or (t-2*c)%2==1 or four<0 or two<0: #if cheese is less than tomatoes or if number of jumbo burgers is a decimal or number of burgers are negtive we return empty list
            return []
        
        return [four,two]
      
-------------------------------------------

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices%2:
            return []
        x=tomatoSlices//2
        diff=x-cheeseSlices
        if diff<0:
            return []
        if x-(2*diff)<0:
            return []

        return [diff,x-(2*diff)]
      
------------------------------------------------------------
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        eq1, eq2 = 0, 0
        a = tomatoSlices//2
        x =  a - cheeseSlices
        y = (2*cheeseSlices) - a

        if x >= 0 and y >= 0:
            eq1 = (4*x) + (2*y)
            eq2 = x + y

            if eq1 == tomatoSlices and eq2 == cheeseSlices:
                return [x,y]
        else:
            return []
