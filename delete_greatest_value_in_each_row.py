'''
You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.
'''


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        for r in range(n):
            mx = -math.inf
            for i in range(m):
                curr = max(grid[i])
                mx = max(mx,curr)
                grid[i].pop(grid[i].index(curr))
            ans += mx
        return ans
                
                
                    
-----------------------------------------------------------------------------------------
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(0, len(grid)):
            grid[i].sort()
        n = len(grid[0])
        res = 0
        for j in range(0, n):
            ans = 0
            for i in range(0, len(grid)):
                ans = max(ans, grid[i].pop())
            res += ans
            
        return res
      
-------------------------------------------------------------------------------------------------------
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for listItem in grid:
            listItem.sort(reverse=True)
        answer=0;
        temp=[]
        col = len(grid[0])
        for i in range(col):
            list=[]
            for j in range(len(grid)):
                list.append(grid[j][i])
            temp.append(list)
        for list in temp:
            answer=answer+max(list)
        return answer
