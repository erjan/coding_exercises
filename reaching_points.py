'''
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).
'''


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        q = [(sx, sy)]
        visit = set()
        visit.add((sx, sy))
        
        while q:
            num = len(q)
            for i in range(num):
                x, y = q.pop(0)
                if x == tx and y == ty:
                    return True
                if x <= tx and y <= ty:
                    if (x, x+y) not in visit:
                        visit.add((x, x+y))
                        q.append((x, x+y))
                    if (x+y, y) not in visit:
                        visit.add((x+y, y))
                        q.append((x+y, y))
        
        return False
      
------------------------------------------------------------------------------------
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx + ty or ty >= sy + tx: # make sure we can still make substractions
            if tx > ty:
                tx = sx + (tx - sx) % ty # the smallest we can get by deducting ty from tx
            else:
                ty = sy + (ty - sy) % tx # the smallest we can get by subtracting tx from ty

        return tx == sx and ty == sy
