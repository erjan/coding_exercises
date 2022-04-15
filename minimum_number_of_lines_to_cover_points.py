'''
You are given an array points where points[i] = [xi, yi] represents a point on an X-Y plane.

Straight lines are going to be added to the X-Y plane, such that every point is covered by at least one line.

Return the minimum number of straight lines needed to cover all the points.
'''

Explanation
The data scale for this question is very small (maximum 10 points, range in [-100, 100])
By basic Math, we all know Two points define a line. This tells us:
If there are n points, the maximum number of lines we need will be
math.ceil(n / 2)
If we use k line to cover m points, then the maximum number of lines we need now will be
k + math.ceil((n-m)/2)
Whenever there is a line that covers more than 2 points, it will be very useful
A line can be defined as y = a*x + b
With above intuition, we will then
Calculate a and b in formula y = a*x + b, given two points (x1, y1) and (x2, y2)
a = (y2-y1) / (x2-x1)
b = y1 - a * x1
If x1 == x2, just set a = x1, b = sys.maxsize meaning these two points are on the same vertical line
The representation is not Mathmatically correct. It just a unique way to represent vertical lines here.
Gathering all lines that covers more than 2 points, save in lines
Given 10 points, the maximum number of lines that cover more than 2 points will be 9, as shown below
xxx
xxx
xxxx
This will lead to a mask size of 2 ** 9 == 512, which is still pretty small scale
Use bitmasking to try out all possible combinations on lines
Meanwhile, calculate the minimum number of lines needed to cover all points
Implementation
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n, line_points = len(points), collections.defaultdict(set)               
        for i in range(n):                                                        # calculate `line_points`
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x1 == x2:                                                      # handle divided by zero case
                    a, b = x1, sys.maxsize                                        # for `b`, you can use any number not in range of [-100, 100]
                else:
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1
                line_points[(a, b)].add((x1, y1))
                line_points[(a, b)].add((x2, y2))
        lines = [line for line, points in line_points.items() if len(points) > 2] # filtering out lines that cover more than 3 points
        ans, m = math.ceil(n / 2), len(lines)                                     # based on Math, set default value for ans
        for i in range(1, 2**m):                                                  # bitmasking on `lines` (try out all combinations)
            j, cnt = 0, bin(i).count('1')                                         # cnt = number of line used for current masking
            cur_points = set()                                                    # current points covered on selected lines
            while i > 0:
                if i % 2:
                    cur_points |= line_points[lines[m-1-j]]                       # set union operaion on '1' bits
                i >>= 1                        
                j += 1
            ans = min(ans, cnt + math.ceil( (n-len(cur_points))/2 ))              # check if current masking is better
        return ans
      
--------------------------------------
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        slope_calc = lambda p1, p2: (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else math.inf

        def helper(lines, points):
            if len(points) == 0:
                return len(lines)
            
            point = points[0]
            
            
            # add to existing line            
            for p, slope in lines:
                s = slope_calc(point, p)
                if s == slope:
                    return helper(lines, points[1:])
            
            # if we have a single point and it doesn't belong to an existing
            # line, we must have another line to cover it.
            if len(points) == 1:
                return len(lines) + 1

            # creating new line in the case we have two or more points
            # (cover two at once). iterating through all possibilities.
            best = math.inf
            for i in range(1, len(points)):
                p = points[i]
                slope = slope_calc(point, p)
                lines.append((point, slope))
                best = min(best, helper(lines, points[1:i] + points[i + 1:]))
                lines.pop(-1)
            
            return best

        return helper([], points) if len(points) > 1 else 1
      
----------------------------------------------------------------
class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        # 最终状态一定会被分为 一条只包含若干个个点的线 和 其他若干条线 两部分
        # 所以只需要穷举每一个状态的所有分成两部分的方法，找到最小的即可
        # 初始值就是把所有仅包含一条线的状态初始成 1
        n = len(points)
        kpoint = {}
        dp = defaultdict(lambda:inf)
        
        for i in range(n):
            for j in range(i+1,n):
                p1,p2 = points[i],points[j]
                if p1[0] == p2[0]:
                    k = inf
                else:
                    k = (p1[1] - p2[1])/(p1[0]-p2[0])
                kpoint[(i,j)] = k
                kpoint[(j,i)] = k
        def isOneLine(state):
            ct = state.bit_count()
            if ct ==1 or ct == 2:
                return True
            else:
                prev = None
                ks = set()
                for j in range(n):
                    if (state >> j) & 1 != 0:
                        if prev is not None:
                            k = kpoint[(prev,j)]
                            if len(ks) == 0:
                                ks.add(k)
                            elif k not in ks:
                                return False
                        else:
                            prev = j
                return True
        for state in range(1<<n):
            if isOneLine(state):
                dp[state] = 1
                
        dp[0] = 0

        for state in range(1<<n):
            subset = state
            while subset > 0:
                dp[state] = min(dp[state], dp[subset] + dp[state-subset])
                subset = (subset - 1) & state
            
        return dp[(1<<n)-1]
