'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        
        res = 0
        
        stack = list()
        stack.append(-1)
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                
                else:
                    res = max(res, i - stack[-1])
        return res
------------------------------------------------------------

from time import sleep

TIME = 0.9


def f(s):

    res = 0
    sleep(TIME)
    stack = list()
    stack.append(-1)

    for i in range(len(s)):
        print()
        print()
        print(
            '----------------index %d, cur char: %s-------------------------' % (i, s[i]))
        sleep(TIME)

        if s[i] == '(':
            sleep(TIME)
            print('found (')
            stack.append(i)
        else:
            sleep(TIME)
            print('popping stack')
            stack.pop()
            print('stack now: ')
            print(stack)

            if len(stack) == 0:
                sleep(TIME)
                print('stack empty add i: %d' % i)
                stack.append(i)

            else:
                sleep(TIME)
                res = max(res, i - stack[-1])
                print('updating res, res now: %d ' % res)
    print()
    print('res %d ' % res)
    return res


if __name__ == "__main__":

    s = ")()())))(()()()()()()()"
        #0123456789

    f(s)
