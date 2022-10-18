'''
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
'''


# if target value is smaller than startValue we can only subtract from the number
if startValue>target:
    return startValue-target

# we will iterate backwards to reach the startValue (greedy approach)
total_steps=0
while target!=startValue:
	if target<startValue:
		total_steps+=startValue-target
		target=startValue
	elif target%2==1:
		total_steps+=1
		target+=1
	else:
		target//=2
		total_steps+=1
return total_steps

-------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while X < Y:
            ans += 1
            if Y % 2: Y += 1
            else: Y //= 2
        return X - Y + ans
      
----------------------------------------------------------------------------------      

	class Solution:
      def brokenCalc(self, startValue: int, target: int) -> int:
          if(startValue>=target):
              return startValue-target


          else:
              count=0
              while(target!=startValue):
                  if(startValue>=target):
                      count+=(startValue-target)
                      break
                  if(target%2==0):
                      target=target//2
                      count+=1
                  else:
                      target=target+1
                      count+=1
          return count
        
------------------------------------------------------------------------------------------------------
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        #For this you can simply think for a situation where in start you are at peak and you have to come down from peak and there is only one possibility for that which move down and that's why we do this
        if startValue >= target:
            return startValue - target
        if target % 2== 0:
            return 1 + self.brokenCalc(startValue , target // 2)
        else:
            return 1 + self.brokenCalc(startValue , target + 1)

------------------------------------------------------------------------------------

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        if startValue >=target:
            return startValue -target
        
        else:
            
            count = 0
            while (target!= startValue):
                
                if startValue >=target:
                    count +=(startValue-target)
                    break
                    
                if target %2 == 1:
                    count+=1
                    target+=1
                    
                elif target %2 == 0:
                    count+=1                               
                    target = target//2
                    
            return count                
