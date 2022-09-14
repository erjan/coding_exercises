'''
You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.

Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.

Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.

The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

 
 '''


# example : 241 + 97
class Solution:
    def minimizeResult(self, exp: str) -> str:
        
        lo, n, mini, ans = 0, len(exp), float('inf'), ''               # lo:  for placing opening paranthesis; hi : hi for placing closing paranthesis
        
        while exp[lo] != '+':                                          # move lo till we get '+', like invalid '241(+9'
            hi = n
            while exp[hi-1] != '+':                                    # for each left paranthesis we place the right paranthesis and evaluate
                left = exp[:lo] if lo else '1'                         # left: left part to opening paranthesis, why if else? case:  '(241 +', left is blank so we take 1
                right = exp[hi:] if hi != n else '1'                   # right: Similarly for closing, case: '+ 97)'
                val = eval(left + '*(' + exp[lo: hi] + ')*' + right)   # evaluate the expression
                if val < mini:                                         # compare it with previous minimum 
                    mini = val                                         # update mini
                    ans = exp[:lo] + '(' + exp[lo: hi] + ')' + exp[hi:]# update ans
                hi -= 1                                                # decrement hi pointer
            lo += 1                                                    # increment lo pointer
        return ans
      
-------------------------------------------------------
class Solution:
    def minimizeResult(self, expression: str) -> str:
        idx = expression.index('+')
        pre = expression[:idx]
        post = expression[idx+1:]
		
        tmp = [] 
        ans = float('inf') 
        for i in range(0, len(pre)):
            for j in range(1, len(post)+1):
                tmp.append(pre[:i] + '*' + '(' + pre[i:] + '+' + post[:j] + ')' + '*' +post[j:])
                
        res = ''
        for c in tmp:
            c = c.strip('*')                        
            if eval(c) <= ans:
                res = c.replace('*', "")
                ans = eval(c)
                            
        return res     
