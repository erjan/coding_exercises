You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

----------------------------------------------------------------------

  #my solution:

  class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        res = []
        n = len(grid)
        # original = [i for i in range(1,n*n+1)]

        original = set()
        a,b = -1,-1

        for i in range(n):
            row = grid[i]
            for val in row:
                if val not in original:
                    original.add(val)
                else:
                    a = val
        
        q = set([i for i in range(1,n*n+1)])
        diff = list(q.difference(original))[0]
        b = diff
        return [a,b]



-------------------------------------------------------------------------------------------

#better solution is to use some hash table and increase its freq as we go thru the array:

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        list: List[int]=[]
        n=len(grid)
        arr: list[int]=[0]*(n*n+1)

        for i in range(0, n):
            for j in range(0, n):
                arr[grid[i][j]]+=1
        
        for i in range(1, n*n+1):
            if arr[i]>1:
                list.insert(0, i)
            if arr[i]==0:
                list.insert(1, i)

        return list
  
