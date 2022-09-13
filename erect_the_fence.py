'''
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.'''

class Solution:
    @staticmethod
    def check_cross_product(a, b, o):
        ax = a[0] - o[0]
        ay = a[1] - o[1]
        bx = b[0] - o[0]
        by = b[1] - o[1]
        return ax*by - ay*bx
    
    @staticmethod
    def find_farthest_pt(pts, pt):
        far = None
        for val in pts:
            if not far:
                far = tuple(val)
            else:
                dist_new = (val[0] - pt[0]) ** 2 + (val[1] - pt[1]) ** 2
                dist_old = (far[0] - pt[0]) ** 2 + (far[1] - pt[1]) ** 2
                if dist_new > dist_old:
                    far = tuple(val)
        return far
    
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        
        ltm_pt = None
        for val in points:
            if not ltm_pt:
                ltm_pt = tuple(val)
            elif val[0] < ltm_pt[0]:
                ltm_pt = tuple(val)

        tree_dict = set()
        vis = {}
        curr_pt = ltm_pt
        while(curr_pt and curr_pt not in vis):
            tree_dict.add(curr_pt)
            found_pt = []
            for val in points:
                if tuple(val) != curr_pt:
                    if not found_pt:
                        found_pt.append(val)
                    else:
                        crp_prd = Solution.check_cross_product(found_pt[0], val, curr_pt)
                        if crp_prd > 0:
                            found_pt = []
                            found_pt.append(val)
                        elif not crp_prd:
                            found_pt.append(val)
            vis[curr_pt] = True
            farthest_pt = Solution.find_farthest_pt(found_pt, curr_pt)
            for val in found_pt:
                tup = tuple(val)
                tree_dict.add(tup)
            curr_pt = farthest_pt
        return tree_dict
