'''

You are given a 2D integer array trees where trees[i] = [xi, yi] represents the location of the ith tree in the garden.

You are asked to fence the entire garden using the minimum length of rope possible. The garden is well-fenced only if all the trees are enclosed and the rope used forms a perfect circle. A tree is considered enclosed if it is inside or on the border of the circle.

More formally, you must form a circle using the rope with a center (x, y) and radius r where all trees lie inside or on the circle and r is minimum.

Return the center and radius of the circle as a length 3 array [x, y, r]. Answers within 10-5 of the actual answer will be accepted.

'''

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        trees = list(set((x, y) for x, y in trees)) # remove duplicates
        shuffle(trees) # randomized algo
        
        def fn(i, R): 
            """Solve smallest circle problem via Welzl's algorithm."""
            if len(R) == 3: # circle from 3 points
                (x0, y0), (x1, y1), (x2, y2) = R
                A = x0*(y1-y2) - y0*(x1-x2) + x1*y2 - x2*y1
                B = (x0*x0 + y0*y0)*(y2-y1) + (x1*x1 + y1*y1)*(y0-y2) + (x2*x2+y2*y2)*(y1-y0)
                C = (x0*x0 + y0*y0)*(x1-x2) + (x1*x1 + y1*y1)*(x2-x0) + (x2*x2+y2*y2)*(x0-x1)
                D = (x0*x0 + y0*y0)*(x2*y1-x1*y2) + (x1*x1+y1*y1)*(x0*y2-x2*y0) + (x2*x2+y2*y2)*(x1*y0-x0*y1)
                return (-B/(2*A), -C/(2*A), sqrt((B*B+C*C-4*A*D)/(4*A*A)))
            if i == len(trees): 
                if len(R) == 0: return (0, 0, 0)
                if len(R) == 1: return (R[0][0], R[0][1], 0)
                if len(R) == 2: 
                    (x0, y0), (x1, y1) = R
                    return ((x0+x1)/2, (y0+y1)/2, sqrt((x0-x1)**2+(y0-y1)**2)/2)
            x, y, r = fn(i+1, R)
            if (trees[i][0]-x)**2 + (trees[i][1]-y)**2 < r**2: return (x, y, r)
            return fn(i+1, R + [trees[i]])
            
			return fn(0, [])
    
    '''
    There are many problems on leetcode which are much more 
    important than this stupid pure mathematical problem..Don't waste your hours searching on net for a problem which won't be asked in interview
    '''
    
    
    class Solution {
    
    public double[] outerTrees(int[][] trees) {
        return welzl(trees, new ArrayList<>(), 0);
    }
    
    private double[] welzl(int[][] p, List<int[]> r, int offset) {
        if (offset == p.length || r.size() == 3) {
            return trivial(r);
        }
        
        double[] disk = welzl(p, r, offset + 1);
        
        if (inside(disk, p[offset])) {
            return disk;
        }
        
        r.add(p[offset]);
        disk = welzl(p, r, offset + 1);
        r.remove(r.size() - 1);
        return disk;
    }
    
    private double[] trivial(List<int[]> r) {
        if (r.isEmpty()) return null;
        
        if (r.size() == 1) {
            return new double[] {r.get(0)[0], r.get(0)[1], 0};
        }
        
        if (r.size() == 2) {
            return getDiskFromTwoPoints(r.get(0), r.get(1));
        }
        
        double[] disk01 = getDiskFromTwoPoints(r.get(0), r.get(1));
        if (inside(disk01, r.get(2))) return disk01;
        double[] disk02 = getDiskFromTwoPoints(r.get(0), r.get(2));
        if (inside(disk02, r.get(1))) return disk02;
        double[] disk12 = getDiskFromTwoPoints(r.get(1), r.get(2));
        if (inside(disk12, r.get(0))) return disk12;
        
        return getDiskFromThreePointsOnTheBoundary(r.get(0), r.get(1), r.get(2));
    }
    
    private double[] getDiskFromTwoPoints(int[] p1, int[] p2) {
        double x1 = p1[0], y1 = p1[1];
        double x2 = p2[0], y2 = p2[1];
        double r2 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
        return new double[] {(x1 + x2) / 2.0, (y1 + y2) / 2.0, Math.sqrt(r2) / 2.0};
    }
    
    private double[] getDiskFromThreePointsOnTheBoundary(int[] p1, int[] p2, int[] p3) {
		// 在p2和p3的中垂线上找一点q使得q到p1，p2，p3距离相等
        double[] center = getCenter(p2[0] - p1[0], p2[1] - p1[1], p3[0] - p1[0], p3[1] - p1[1]);
        center[0] += p1[0];
        center[1] += p1[1];
        double r2 = (center[0] - p1[0]) * (center[0] - p1[0]) + (center[1] - p1[1]) * (center[1] - p1[1]);
        return new double[] {center[0], center[1], Math.sqrt(r2)};
    }
    
    private double[] getCenter(double bx, double by, double cx, double cy) {
        double b = bx * bx + by * by;
        double c = cx * cx + cy * cy;
        double d = bx * cy - by * cx;
        return new double[] {(cy * b - by * c) / (2 * d), (bx * c - cx * b) / (2 * d)};
    }
    
    private boolean inside(double[] circle, int[] point) {
        if (circle == null) return false;
        double r = circle[2] * circle[2];
        double dist = (circle[0] - point[0]) * (circle[0] - point[0]) 
            + (circle[1] - point[1]) * (circle[1] - point[1]);
        return dist <= r;
    }
}
