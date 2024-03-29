'''
You are working in a ball factory where you have n balls numbered from lowLimit up to 
highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits 
of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and 
the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
'''

# my STUPID SOLUTION 
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def f(n):
            s = 0
            a = str(n)
            for digit in a:
                digit = int(digit)
                s+= digit
            return s
        
        l = lowLimit
        h = highLimit
        
        a = [ 0 ]* 100 #for using this array i would get bad point - not knowing the better data structure is hashmap!
        for i in range(l, h+1):
            temp = f(i)
            a[temp] += 1


                
        print(f'max is %d' % max(a))
        return max(a)
        
#MUCH BETTER SOLUTION inspired with idea from submissions with hashmap:

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def numbersum(n):
            s = str(n)
            res = 0
            for digit in s:
                res += int(digit)
            return res
        
        
        #hashmap
        
        hashmap = defaultdict(int)
        
        for i in range(lowLimit, highLimit+1):
            value = numbersum(i)
            hashmap[value]+=1
            
        
        return max( hashmap.values())
                


