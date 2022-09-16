'''
Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:

Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
Return the list answer. If there multiple valid answers, return any of them.
'''

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans, a, z = [0] * n, 1, k + 1
        for i in range(k+1):
            if i % 2:
                ans[i] = z
                z -= 1
            else:
                ans[i] = a
                a += 1
        for i in range(k+1,n):
            ans[i] = i + 1
        return ans
      
---------------------------------------------------------------------------
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        queue = [i for i in range(1, n+1)]
        if k == 1:
            return queue
        iterate = int(k/2)
        for i in range(0, iterate):
            tmp = queue.pop(0)
            if k%2 == 0:
                queue.insert(n-1-(2*i), tmp)
            else:
                queue.insert(n-2-(2*i), tmp)
        return queue
