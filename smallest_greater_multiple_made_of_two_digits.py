'''
Given three integers, k, digit1, and digit2, you want to find the smallest integer that is:

Larger than k,
A multiple of k, and
Comprised of only the digits digit1 and/or digit2.
Return the smallest such integer. If no such integer exists or the integer exceeds the limit of a signed 32-bit integer (231 - 1), return -1.
'''


Explanation:
In order to get the smallest possible number with digits given, we must do a BFS based on length of the number and also the order of the digits, so kind of like a greedy search if you will. Afterwards, all we have to do is keep track of the numbers that we've already visited.

class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        mi = min(digit1, digit2)
        ma = max(digit1, digit2)
        qu = deque([mi, ma] if mi != ma else [mi])
        while qu:
            cur = qu.popleft()
            if cur == 0 or cur > 2 ** 31 - 1:
                continue
            if cur > k and cur % k == 0:
                return cur
            qu.append(cur * 10 + mi)
            if mi != ma:
                qu.append(cur * 10 + ma)
        return -1
      
-------------------------------------------------------
class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        deque=collections.deque()
        if digit1>0: deque.append(digit1)
        if digit2>0: deque.append(digit2)
        res=float('+inf')
        while deque:
            num=deque.popleft()
            if num>2**31 or num>res: continue
            if num%k==0 and num>k: 
                res=min(res,num)
            deque.append(num*10+digit1)
            deque.append(num*10+digit2)
        return res if res!=float('+inf') else -1
      
      --------------------------------------------------------------
      class Solution:
    def findInteger(self, k: int, d1: int, d2: int) -> int:
        l=[(2**32)-1]
        r=[float("inf")]
        def bt(i,z):
            if z>=l[0]:return
            if z%k==0 and z>k:
                r[0]=min(z,r[0])
                return
            for nn in [d1,d2]:
                if nn==0 and z==0:continue
                bt(i+1,(z*10)+nn)
        bt(0,0)
        return r[0] if r[0]!=float('inf') else -1
      
--------------------------------------------------------------------------------
Explanation
Find all possible combinations and find the smallest one
Implementation
class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        upper_bound = 2**31 - 1
        for i in range(1, 11):
            for val in sorted(int(''.join(val)) for val in itertools.product(f'{digit1}{digit2}', repeat=i)):
                if val >= upper_bound: return -1
                if val > k and not val % k: return val
        return -1            
