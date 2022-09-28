'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
'''


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for i in s:
            print('-----------------------')
            print('cur char %s' % i)
            print('the stack is')
            print(stack)
            if not stack:
                print('stack empty - add char: %s' % i)
                stack.append([i, 1])
                continue

            elif stack[-1][0] == i:
                print('same as top of stack, so increase count for %s' % i)
                stack[-1][1] += 1
            else:
                print('add to the stack: [%s, 1] ' % i)
                stack.append([i, 1])

            if stack[-1][1] == k:
                print('pop the stack cuz equal to k: %d' % k)
                stack.pop()
        res = ''
        for i in stack:
            res += i[0] * i[1]
        return(res)

