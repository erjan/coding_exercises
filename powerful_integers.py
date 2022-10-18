'''
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.
'''

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        bx = int(log(bound)/log(x)) if x > 1 else 0
        by = int(log(bound)/log(y)) if y > 1 else 0 
        
        ans = set()
        for i in range(bx+1): 
            for j in range(by+1):
                if x**i + y**j <= bound: 
                    ans.add(x**i + y**j)
        return ans 
      
----------------------------------------------------------------------
   def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
       res , i , j = set() , 0 , 0
       tempx , tempy= x**i , y**j
       while tempx<bound:
           while tempx + tempy <= bound:
               #print("i:{} j:{} x**i:{} y**j:{} add:{}".format(i,j,tempx,tempy,tempx+tempy))
               res.add(tempx+tempy)
               j+=1
               tempy = y**j
               if y==1:  break
           i+=1
           tempx = x**i
           j = 0
           tempy = y**j
           if x==1: break
       return list(res)
    
--------------------------------------------------------------------------------------------------------

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xset, yset = set(), set()
        for i in range(20):
            if x**i < bound:
                xset.add(x**i)
        
        for i in range(20):
            if y**i < bound:
                yset.add(y**i)
        
        ans = set()
        for i in xset:
            for j in yset:
                if i+j <= bound:
                    ans.add(i+j)
        
        return list(ans)
      
----------------------------------------------------------------------------------------

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if not bound: return []
        m, n = 0, 0
        curx = 1
        if x > 1:
            while curx*x <= bound:
                curx *= x
                m += 1
        cury = 1
        if y > 1:
            while cury*y <= bound:
                cury *= y
                n += 1
        powerful = set()
        curx = 1
        for i in range(m+1):
            cury = 1
            for j in range(n+1):
                if curx + cury <= bound:
                    powerful.add(curx+cury)
                else:
                    break
                cury *= y
            curx *= x
        return list(powerful)
