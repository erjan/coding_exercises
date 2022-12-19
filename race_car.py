'''
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

 
 '''

# Smart BFS
# O(t*log(t))
class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)])
        visited = set([0, 1])
        actions = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, v = q.popleft()
                if x == target:
                    return actions
                
                # Accelerate
                # NOTE: if accelerating in the negative regions or passing the target by more than two times, 
                # then this is never going to reach an answer
                # we won't add it to the queue
                newx = x + v
                newv = v * 2
                if 0 <= newx <= 2 * target and (state := (newx, newv)) not in visited:
                    visited.add(state)
                    q.append(state)


                # Reverse
                newv = -1 if v > 0 else 1
                if (state := (x, newv)) not in visited:
                    visited.add(state)
                    q.append(state)
                    
            actions += 1
                    
# DP
# O(t*log(t))
class Solution:
    def racecar(self, target: int) -> int:
        
        @cache
        def go(n):
            m = n.bit_length()
            # check if we can go directly to the target
            if 2 ** m - 1 == n:
                return m
            else:
                # otherwise we have two choices
                # we pass the point, and then we reverse (denoted by passing_moves)
                # or we go as close to the target as possible, reverse, go back up to m - 2 times, reverse again, and reach the point
                # note if we go back m - 1 times, we have reached the same point we started at.
                
                # 1. go past target (m moves), reverse (1 move), and reach the target (recurse)
                passing_moves = m + 1 + go(2 ** m - 1 - n)
                
                # 2. go as close to target as possible (m - 1 moves), reverse (1 move) and go back (i < m - 1 moves), reverse (1 move), and reach the target (recurse)
                closest_point = 2 ** (m - 1) - 1
                closest_moves = m - 1
                min_ = math.inf
                for i in range(m - 1):
                    backward = 2 ** i - 1
                    remain_moves = go(n - (closest_point - backward)) + i
                    min_ = min(min_, remain_moves)
                    
                closest_moves += min_ + 2
                
                return min(passing_moves, closest_moves)
            
        return go(target)
      
--------------------------------------------------------------------------------------------------------
class Solution:
def racecar(self, target: int) -> int:
    
    q = deque()
    q.append((0,0,1))
    while q:
        m,p,s = q.popleft()
        if p==target:
            return m
        rev = -1 if s>0 else 1
		
        q.append((m+1,p+s,s*2))
        
        if (p+s<target and s<0) or (p+s>target and s>0):        # If you are back to the target and speed is reverse or if you are ahead of target and speed is positive then reverse the speed
            q.append((m+1,p,rev))
    
    return -1
