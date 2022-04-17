There are n unique virus variants in an infinite 2D grid. You are given a 2D array points, where points[i] = [xi, yi] represents a virus originating at (xi, yi) on day 0. Note that it is possible for multiple virus variants to originate at the same point.

Every day, each cell infected with a virus variant will spread the virus to all neighboring points in the four cardinal directions (i.e. up, down, left, and right). If a cell has multiple variants, all the variants will spread without interfering with each other.

Given an integer k, return the minimum integer number of days for any point to contain at least k of the unique virus variants.

Seems this is definitely a competitive-programming level problem... not sure if there is an easier way to solve this one based on the small data (N<=16)

Without diagram I don't think I can explain my algo well, but I'm bad at that. I expect there would be a better post with better explanation

Basic idea is like this:
Given a day, the spread of each virus on the coordinate will be formed as a diamond-shape square with center at (x,y), and the distance of the center to each corner is day. What we want to do is to find if there is a point having k or more overlapping of these squares

For example (Capital X is the center):

Day 0:
    X
Day 1:
   x
x  X  x
   x
Day 2:

    x
  x x x
x x X x x
  x x x
    x
If it is a normal square, we can do a 2D sweep line on each square, inspired by LC391

So I just rotate the axis by 45 degree, where the transformation formula is newx = x+y, newy=y-x (if you learned some linear algebra before you might recall this...)

With this transformation, we got the point mapping as follows (old point pos -> new point pos):

left corner -> upper-left corner
bottom point -> bottom-left corner
right corner -> bottom-right corner
upper corner -> upper-right corner
From there, we can utilize sweep line to count the overlapping virus at each point we track at a given day.

From there, we can do binary search to find the minimum day...

TL;DR
If you didn't read, just don't read:)
No need to understand this solution if you're seeking a job. Just give the interviewer a sh!t if you are asked such a question.
(I'll revoke my word if there is a much easier way to solve this)

CODE

class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
		# binary search check helper function
        def check(day):
            lines = collections.defaultdict(collections.Counter)
            
            # 2d sweep line (lb,ub refers to lower bound and upper bound)
            for x, y in points:
                lbx, lby = (x, y - day) # left point
                ubx, uby = (x - day, y) # bottom point
                
				# lbx + lby == ubx + uby == new x axis's open line
                lines[lbx+lby][lby-lbx] += 1
                lines[ubx+uby][uby-ubx+1] -= 1 # 
                
				# lbx + lby == ubx + uby == new x axis's close line
                lbx, lby = (x + day, y) # right point
                ubx, uby = (x, y + day) # upper point
                lines[lbx+lby+1][lby-lbx] -= 1 
                lines[ubx+uby+1][uby-ubx+1] += 1
            
            # hold a new ranges to sweep all lines from left to right on new x axis
            ranges = collections.Counter()
			
			# for every critical points on new x axis (it's a diag on the original axis),
			# add the sweep lines on new y axis
            for diag in sorted(lines):
                for num, cnt in lines[diag].items():
                    ranges[num] += cnt
                
				# for every critical points, check whether there is an area having 
				# overlapping points >= k
                cur = 0
                for num in sorted(ranges):
                    cnt = ranges[num] 
                    cur += cnt

                    if cur >= k:
                        return True
            
            return False
                
		lo = 0
        hi = int(1e9)
		# binary search
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
Not 100% sure about the complexity, it probably would be O(log(MAX_POINT) * N^2log(N)), where MAX_POINT=1e9
And I feel the complexity can be reduced with some advanced data structure, for the inner sweep line part. But it's sufficient for passing this OJ...
 
 
 --------------------------------------------------------------------------
 class Solution:
    def minDayskVariants(self, P: List[List[int]], k: int) -> int:
        def gosper(x, last):
                if x == last: return -1
                s = x & -x
                r = s + x
                return r | (((x ^ r) >> 2) // s)
        n = len(P)
        x = (1<<k)-1
        last = x << (n-k)
        mn = float('inf')
        while x != -1:
            mx = 0
            for i in range(n-1):
                for j in range(i+1, n):
                    if x & 1<<i and x & 1<<j:
                        mx = max(mx, abs(P[i][0]-P[j][0])+abs(P[i][1]-P[j][1]))
            mn = min(mn, (mx+1)//2)
            x = gosper(x, last)
        return mn
 
-----------------------------------------------------
 Time compexity is O(N^3 * (log N + log max(|x|, |y|)).
Space complexity is O(N).

class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        def max_after_t_days(t):
            """
            Returns maximum number of viruses in one point after *t* days.
            """
            pbounds,mbounds = set(), set()
            rects = []
            for x,y in points:
                # rotate 45 degrees: transform to (p,m)=(x+y,x-y) coords
                # not every (p,m) corresponds to integer (x,y): must be (p^m)&1==0
                pmin,pmax = x+y-t,x+y+t
                mmin,mmax = x-y-t,x-y+t
                rects.append((pmin,mmin,pmax,mmax))
                pbounds.update({pmin,pmax+1})
                mbounds.update({mmin,mmax+1})
            
            # Will use coordinate compression
            pbounds = sorted(pbounds)
            mbounds = sorted(mbounds)
            M,N = len(pbounds),len(mbounds)
            assert(M>=2 and N>=2)
            
            best = 0
            # for each cell in a (rotated) grid
            for i in range(M-1):
                p = pbounds[i]
                for j in range(N-1):
                    m = mbounds[j]
                    if (pbounds[i+1]-p <= 1) and (mbounds[j+1]-m <=1 ) and ((p^m)&1):
                        # this cell does not contain any integer (x,y)  point
                        continue
                    v = 0 # number of viruses
                    for p1,m1,p2,m2 in rects:
                        if p1<=p<=p2 and m1<=m<=m2:
                            v += 1
                    if v>best:
                        best = v
            
            return best
        
        if max_after_t_days(0)>=k:
            return 0
        
        # will get an upper bound for the answer
        R = 0
        for i in range(len(points)-1):
            x0,y0 = points[i]
            x1,y1 = points[i+1]
            R += abs(x1-x0)+abs(y1-y0)
        assert max_after_t_days(R)==len(points)
		# R is just the length of the polyline connecting all points
		# -- it's not shorter than the distance between any pair of points
        
        # will use bisection to found the answer
        L = 0
        while R-L>1:
            M = L+(R-L)//2
            if max_after_t_days(M)<k:
                L = M
            else:
                R = M
        return R
