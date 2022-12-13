'''
You are given a valid boolean expression as a string expression consisting of the characters '1','0','&' (bitwise AND operator),'|' (bitwise OR operator),'(', and ')'.

For example, "()1|1" and "(1)&()" are not valid while "1", "(((1))|(0))", and "1|(0&(1))" are valid expressions.
Return the minimum cost to change the final value of the expression.

For example, if expression = "1|1|(0&0)&1", its value is 1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1. We want to apply operations so that the new expression evaluates to 0.
The cost of changing the final value of an expression is the number of operations performed on the expression. The types of operations are described as follows:

Turn a '1' into a '0'.
Turn a '0' into a '1'.
Turn a '&' into a '|'.
Turn a '|' into a '&'.
Note: '&' does not take precedence over '|' in the order of calculation. Evaluate parentheses first, then in left-to-right order.
'''


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        loc = {}
        stack = []
        for i in reversed(range(len(expression))):
            if expression[i] == ")": stack.append(i)
            elif expression[i] == "(": loc[stack.pop()] = i 
        
        def fn(lo, hi): 
            """Return value and min op to change value."""
            if lo == hi: return int(expression[lo]), 1
            if expression[hi] == ")" and loc[hi] == lo: return fn(lo+1, hi-1) # strip parenthesis 
            mid = loc.get(hi, hi) - 1 
            v, c = fn(mid+1, hi)
            vv, cc = fn(lo, mid-1)
            if expression[mid] == "|": 
                val = v | vv 
                if v == vv == 0: chg = min(c, cc)
                elif v == vv == 1: chg = 1 + min(c, cc)
                else: chg = 1 
            else: # expression[k] == "&"
                val = v & vv
                if v == vv == 0: chg = 1 + min(c, cc)
                elif v == vv == 1: chg = min(c, cc)
                else: chg = 1
            return val, chg
                    
        return fn(0, len(expression)-1)[1]
