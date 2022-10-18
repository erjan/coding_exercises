'''
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.
'''


class Solution:
def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
    
    forbidden = set(forbidden)
    limit = max(x,max(forbidden))+a+b
    seen = set()
    q = [(0,0,False)]
    while q:
        p,s,isb = q.pop(0)
        if p>limit or p<0 or p in forbidden or (p,isb) in seen:
            continue
        
        if p==x:
            return s
        
        q.append((p+a,s+1,False))
        if not isb:
            q.append((p-b,s+1,True))
        seen.add((p,isb))
    
    return -1
  
-----------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        limit = max(x, max(forbidden)) + a + b
        queue = [(0, 0, False)]
        while queue:
            pos, step, back = queue.pop(0)
            if pos > limit or pos < 0 or pos in forbidden or (pos, back) in visited:
                continue
            if pos == x:
                return step
            queue.append((pos+a, step+1, False))
            if not back: queue.append((pos-b, step+1, True))
            visited.add((pos, back))
        return -1
A traditional BFS solution by using queue. Each element in the queue contains:

pos: The current position of the bug;
step: The total step;
back: Check if the previous step is jumping backward.
The terminal conditions is declared in the question:

pos < 0: The bug cannot jump to the negative position;
pos in forbidden: The bug cannot jump to the forbidden position;
(pos, back) in visited: To prevent the bug repeatly jumps between the previous and current position, it is noticeable that jump forward or backward to the position is totally different;
pos > limit: As 0 <= x <= 2000, the maximum index of position will not beyond limit, which limit = max(x, max(forbidden)) + a + b.
