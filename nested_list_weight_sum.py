'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0
'''


Algo
This problem is recursive in nature.

Implementation 1 - recursive

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def fn(nl, wt): 
            """Return weight sum of nested list."""
            ans = 0
            for x in nl:
                if x.isInteger(): ans += wt * x.getInteger()
                else: ans += fn(x.getList(), wt+1)
            return ans 
        
        return fn(nestedList, 1)
Implementation 2 - iterative dfs

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = []
        for x in nestedList: stack.append((x, 1))
        
        ans = 0
        while stack: 
            x, wt = stack.pop()
            if x.isInteger(): ans += wt * x.getInteger()
            else: stack.extend([(xx, wt+1) for xx in x.getList()])
        return ans 
Implementation 3 - iterative bfs

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans = wt = 0
        queue = nestedList
        while queue: 
            wt += 1
            newq = []
            for x in queue: 
                if x.isInteger(): ans += wt * x.getInteger()
                else: newq.extend(x.getList())
            queue = newq
        return ans 
Analysis
Time complexity O(N)
Space complexity O(N) due to recursion stack

---------------------------------------------------------------------------------
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans=0
        def dfs(nestedList,depth):
            nonlocal ans
            j=0
            while j<len(nestedList):
                if nestedList[j].isInteger():
                    x=nestedList[j].getInteger()
                    ans+=x*depth
                else:
                    dfs(nestedList[j].getList(),depth+1)
                j+=1
        dfs(nestedList,1)
        return ans
      
-----------------------------------------------

The tricky part of this exercice is to understand the actual data structure. After reading a bit, you can get that you can easily go recursively into the different nested integers of the list.

So suppose you take [[1,1],2,[1,1]], you have basically 3 elements.

NestedList
NestedInt
NestedList
You only have to iterate for each of these elements, and increase the level each time you make a recursion.
Let's take [1,1], the first element.

It's a NestedInt? No, let's recurse again on the list by increasing the level by 1.
We now have 2 nested elements 1 and 1, let's apply recursion on each of the elements.
It's a NestedInt! Let's return this element * the level of recursion
It's a NestedInt! Let's return this element * the level of recursion
By returning the sum of everything, we're returning (1x2 + 1x2)
And voila! You only have to sum every NestedElement analyzed.

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def getValue(nestedInteger: NestedInteger, level: int):
            if nestedInteger.getInteger():
                return nestedInteger.getInteger() * level
            
            return sum(getValue(x, level+1) for x in nestedInteger.getList())
            
        return sum(getValue(x,1) for x in nestedList)
-----------------------------------------------------------------------------

The key thing to remember here is that there effectively two situations that you will always land in:

The current element could be an int. When we reach it we can just return the element * current_count.
The current element could be a list of ints. Here we would want to recursively call dfs() but with the next element in the nested list and with an incremented count.
These two scenarios will form the base cases when using a recursive DFS approach.

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0
        def dfs(i, nestedList, count=1):
            current_total = 0
			# Base case 1: Current element is an int
            if nestedList[i].isInteger():
                return nestedList[i].getInteger() * count
            # Base case 2: Current element is a list of ints
            if nestedList[i].getList():
                for j in range(len(nestedList[i].getList())):
                    current_total += dfs(j, nestedList[i].getList(), count+1)
            return current_total 
                    
        for i in range(len(nestedList)):
            total += dfs(i, nestedList)
        return total 
------------------------------------------------------------

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = collections.deque()
        
        for nested in nestedList:
            q.append(nested)
        
        res = 0
        depth = 1
        
        while q:
            for idx in range(len(q)):
                nested = q.popleft()
                if nested.isInteger():
                    res += nested.getInteger() * depth
                else:
                    lst = nested.getList()
                    for elem in lst:
                        q.append(elem)
            
            depth += 1
        
        return res
---------------------------------------------------

Simple(-ish) python stack-based DFS. The same idea as recursive DFS, but just saving the current nestedList and current i values onto the stack every time we iterate. We have to remember to append the nestedList back onto the stack even when i+1 == len(nestedList) because we need to know how many times to decrement depth. If we didn't re-append stack, then we would only decrement depth once when we have 3 lists that all end at the same value, like in [1,[4,[6]]]

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = [(nestedList, 0)]
        depth = 1
        ans = 0
        while stack:
            nl, i = stack.pop()
            while i < len(nl):
                ni = nl[i]
                if ni.isInteger():
                    ans += ni.getInteger() * depth
                    i += 1
                else:
                    stack.append((nl, i+1))
                    nl = ni.getList()
                    depth += 1
                    i = 0
            depth -= 1
        return ans
----------------------------------------------------------------      
      
      
      
      
