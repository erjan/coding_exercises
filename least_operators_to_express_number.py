'''
Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happen before addition and subtraction.
It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.
'''

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        
        @cache
        def fn(val): 
            """Return min ops to express val."""
            if val < x: return min(2*val-1, 2*(x-val))
            k = int(log(val)//log(x))
            ans = k + fn(val - x**k)
            if x**(k+1) < 2*val: 
                ans = min(ans, k + 1 + fn(x**(k+1) - val))
            return ans 
        
        return fn(target)
      
-----------------------------------------------------------------------
# written by : Dhruv vavliya

x = 5
target = 501

from functools import lru_cache
@lru_cache(None)
def go(x,target):
    if target == 1:
        return 1                               # 5/5 (only 1 possible soln)

    op =0
    current=x
    while current < target:
        current*=x                              # 5*5*5*5
        op+=1
    if current == target:                       # if target achieve
        return op

    # almost nearest target ,then increase
    if op == 0:                                 # 5/5 + ....  (2 operations)
        ans = 2 + go(x,target-1)
    else:
        ans = op + go(x,target-current//x)     # (target-current) but current*5 extra multiplied

    # increase than target, then decrease
    if current-target < target:                # if (current - target) lies outside of target then,only consider one case
        ans = min(ans ,op+1 + go(x,current-target))    # op+1 for additionally *x then decrease
    return ans


def express_number(x ,target):
    return go(x,target)

print(express_number(x,target))
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def solve(self,x,target):
        if target in self.dp : return self.dp[target]
        
        # when target == 1 we can solve just by doing x/x  
        if target == 1: return 1
        
         # current value = x and operations performed  = 0
        cur = x
        op = 0
       
        # if cur < target : the best decision is to multiply
        while cur < target:    
            cur *= x
            op += 1
        
        # if cur == target : we reached using minimum possible operations 
        if cur == target :
            return op
        
        if op == 0:
            # cur is already larger than target
            # x/x + make(target-1) : make 2 operations + solve(target-1)
            ans = 2 + self.solve(x,target - 1)
        else:
            # we try to reach nearest val via multiply less than target
            # and find ans for remaining i.e. target - cur/x 
            # here op becomes op - 1 so op - 1 + 1 becomes op
            ans = op + self.solve(x,target-(cur//x))
            
        if cur - target < target :
            # diff between cur and target is less than target
            # i.e. we can make cur and remove cur - target
            tmp = op + 1 + self.solve(x,cur - target)
            if tmp < ans : ans = tmp
        
        # finally use dp for memoization
        self.dp[target] = ans
        return ans
