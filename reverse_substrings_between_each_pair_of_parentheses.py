'''
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 
 '''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list()
        res = ''
        for i in range(len(s)):
            if s[i] == ')':
                tmp = ""
                while stack[-1] != '(':
                    t = stack.pop()
                    print(t)
                    tmp += t

                stack.pop()
                for j in tmp:
                    stack.append(j)
            else:
                stack.append(s[i])

        return "".join(stack)

       
-----------------------------------------------------------------------------
class Solution:
    def reverseParentheses(self, s: str) -> str:
        i, n, stack = 0, len(s), []
        
        while i < n:
            if  s[i] == '(':  # if its opening parentheses, just append
                stack.append(s[i])
            elif s[i] == ')': # if its closing parentheses
                st = ''
                while stack!=[] and stack[-1]!='(': #while stack is not empty and stack's top is NOT an opening parentheses
                    st += stack.pop() #pop the element and append to a temporary string
                stack.pop() #pop the last remaining ( in some cases
                stack += list(st) #append the popped elements to stack
            else:
                stack.append(s[i]) #pushing all letters into stack
            i += 1
        return ''.join(stack)
       
--------------------------------------------------------------------------------------------------
class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        stack = list()

        while i < len(s):
            if s[i] != ')':
                stack.append(s[i])
            elif s[i] == ')':
                st = ''
                while len(stack) != 0 and stack[-1] != '(':
                    st += stack.pop()

                stack.pop()#pop last '('
                stack += list(st)
            i+=1

        return ''.join(stack)

-----------------------------------------------------------------------------------
#11 july 2024
#this prints out the full stack trace

def f(s):


        stack = []

        for ch in s:
            print('----------------------')
            if ch == '(':
                print('adding ( to stack')
                stack.append('(')
                print('stack now :')
                print(stack)
            elif ch == ')':
                print('emptying stack..')
                temp = ''
                while stack and stack[-1]!='(':

                    x= stack.pop()
                    print('popping from stack: ' + x)
                    temp += x
                stack.pop()
                print('adding to the stack this: ')
                print(list(temp))
                stack += list(temp)

            else:
                print('adding to stack: ' + ch)
                stack.append(ch)
                print('stack now :')
                print(stack)

        return ''.join(stack)

s = "(ed(et(oc))el)"


f(s)

python t5.py
----------------------
adding ( to stack
stack now :
['(']
----------------------
adding to stack: e
stack now :
['(', 'e']
----------------------
adding to stack: d
stack now :
['(', 'e', 'd']
----------------------
adding ( to stack
stack now :
['(', 'e', 'd', '(']
----------------------
adding to stack: e
stack now :
['(', 'e', 'd', '(', 'e']
----------------------
adding to stack: t
stack now :
['(', 'e', 'd', '(', 'e', 't']
----------------------
adding ( to stack
stack now :
['(', 'e', 'd', '(', 'e', 't',
'(']
----------------------
adding to stack: o
stack now :
['(', 'e', 'd', '(', 'e', 't',
'(', 'o']
----------------------
adding to stack: c
stack now :
['(', 'e', 'd', '(', 'e', 't',
'(', 'o', 'c']
----------------------
emptying stack..
popping from stack: c
popping from stack: o
adding to the stack this:
['c', 'o']
----------------------
emptying stack..
popping from stack: o
popping from stack: c
popping from stack: t
popping from stack: e
adding to the stack this:
['o', 'c', 't', 'e']
----------------------




adding to stack: e
stack now :
['(', 'e', 'd', 'o', 'c', 't', 'e', 'e']
----------------------
adding to stack: l
stack now :
['(', 'e', 'd', 'o', 'c', 't', 'e', 'e', 'l']
----------------------
emptying stack..
popping from stack: l
popping from stack: e
popping from stack: e
popping from stack: t
popping from stack: c
popping from stack: o
popping from stack: d
popping from stack: e
adding to the stack this:
['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']
