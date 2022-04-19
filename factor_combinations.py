'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

 

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
'''


Iterative:

def getFactors(self, n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n/i],
                todo += (n/i, i, combi+[i]),
            i += 1
    return combis
Recursive:

def getFactors(self, n):
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n/i],
                factor(n/i, i, combi+[i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])
----------------------------------------------------------
def getFactors(self, n):
    ans, stack, x = [], [], 2
    while True:
        if x > n / x:
            if not stack:
                return ans
            ans.append(stack + [n])
            x = stack.pop()
            n *= x
            x += 1
        elif n % x == 0:
            stack.append(x)
            n /= x
        else:
            x += 1
-----------------------------------------------------------------------
Key is: the output combination is in ascending order, so when we find a factor, the next factor (in next recursion) has to >= current factor

Then we can do the dfs search:

def getFactors(self, n):        
    res = []
    self.helper(n, 2, res, [])
    return res[:-1] # the last factor is n itself
    
def helper(self, n, bound, res, temp):
    if n == 1:
        res.append(temp)
        return
    for fac in range(bound, int(n**0.5)+1):
        if n%fac == 0:
            self.helper(n/fac, fac, res, temp+[fac])
    self.helper(1, n, res, temp+[n]) # allow itself to be a factor as well
----------------------------------------------------------------------------------
def getFactors(self, n):
    res = []
    self.dfs(self.factors(n)[1:-1], n, 0, [], res)
    return res
 
def dfs(self, nums, n, index, path, res):
    tmp = reduce(lambda x,y:x*y, path, 1)
    if tmp > n:
        return  # backtracking
    if tmp == n and path:
        res.append(path)
        return  # backtracking 
    for i in xrange(index, len(nums)):
        self.dfs(nums, n, i, path+[nums[i]], res)
        
def factors(self, n):
    res = []
    for i in xrange(1, n+1):
        if n % i == 0:
            res.append(i)
    return res
----------------------------------------------------------------
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        results = []
        self.dfs(n, [], 2, results)
        return results
        
    def dfs(self, n, subset, start, result):

        while start * start <= n:
            if n % start == 0:
                result.append(subset + [start, n//start])
                self.dfs(n//start, subset + [start], start, result)

            start += 1

        return result
        
                
    
    
            
    
