'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
 '''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
		stack = []
        res = []
        for i,v in enumerate(s):
            res.append(v)  # save the charactors to final resutls
            if v == '(':
                stack.append(i) # always save left '(' index, to decided if this need to remove or not 
            if v == ')':
                if stack:
                    stack.pop() # as stack saved left '(', so here is good to pop one no matter the index value, just pop the left as a pair
                else:
                    res[-1] = ''  # as stack is empty, now we see additional right ')', need replace res[-1] with a empty str, 
					                    # why not pop out? 
										# if we do pop, once we loop to the end of the string
										# if we still have some  left '(' in stack, 
										# while we do replace array value, it may mess up. 
										# here, we need keep our res index consistent with the original str 's'.
		
		# if we have some left '(' index stack, which means not paired ones, let's remove these ones
        while stack:
            res[stack.pop()] = ''
		
        return "".join(res)
