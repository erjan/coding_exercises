'''
You are given a list of integers heights representing 
building heights. A building heights[i] can see the ocean if every building on its right 
has shorter height. Return the building indices where you can see the ocean, in ascending order.
'''



class Solution:
    def solve(self, heights):
        if len(heights) == 0:
            return []
        stack = []

        heights = heights[::-1]
        stack.append([heights[0], 0])
        print('before')
        print(stack)
        print()
        for i in range(1, len(heights)):
            last = stack[-1]
            el = last[0]
            if heights[i] > el:
                print('appending %d' % heights[i])
                stack.append([heights[i], i])
        print()
        print(stack)

        for i in range(len(stack)):
            stack[i] = stack[i][1]
        print()
        print(stack)

        for i in range(len(stack)-1, -1, -1):
            stack[i] = len(heights) - stack[i] - 1
        print('stack')
        stack.sort()
        print(stack)
        return stack
      
---------------------------------------------------------------------------------
class Solution:
    def solve(self, heights):
        ans = []
        highest = -1
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                ans.append(i)
                highest = heights[i]
        return ans[::-1]
