'''
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.
'''

As stated in the description, If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3., the hierarchy of regions can be described by a tree. In this case, one could move up the tree and find all ancestors of region1 and region2, and stop at the first match.

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = dict() #parent region
        for region in regions:
            for child in region[1:]:
                parent[child] = region[0] #trace upward along the tree 
                
        candidates = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            candidates.add(region1)
            
        while region2 not in candidates: region2 = parent[region2]
            
        return region2
-------------------------------------------------------------------

Fill hash with (children:parent)
Find all path of parents for both regions
Return mapping parent
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
		#Fill hash with child and parent
        myhash = {}
        for region in regions:
            for i in range(1,len(region)):
                myhash[region[i]] = region[0]

        parent1,parent2 = [region1],[region2]
        
        def findParents(region,parent):
            for element in myhash:
                if element == region:
                    if myhash[element] not in parent:
                        parent.append(myhash[element])
                    findParents(myhash[element],parent)
        
		#Fill all parents for both regions
        findParents(region1,parent1)
        findParents(region2,parent2)
        
		#Return mapping parent
        for region in parent1:
            if region in parent2:
                return region
------------------------------------------------------------------

Intuitive LCA Approach

Create a tree
Find the root of the tree
Store the paths of both the regions
Find the lowest common ancestor
Time complexity: O(N), where N is no of nodes/places
Space complexity: O(N)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        region_map = defaultdict(TreeNode)
        par_list = set()
        children_list = set()
        
        for region in regions:
            if region[0] not in region_map:
                region_map[region[0]] = TreeNode(region[0])
                par_list.add(region[0])
            for i in range(1,len(region)):
                if region[i] not in region_map:
                    region_map[region[i]] = TreeNode(region[i])
                region_map[region[0]].children.append(region_map[region[i]])
                children_list.add(region[i])
        
        
        par = par_list.difference(children_list)
        parent = [x for x in par][0]
        par_node = region_map[parent]
        l = []
        r = []
        
        def dfs(par, ele, x):
            if par.val == ele:
                return True
            for child in par.children:
                if dfs(child, ele,x):
                    x.append(child.val)
                    return True
        
        
        dfs(par_node, region1, l)
        l.append(par_node.val)
        dfs(par_node, region2, r)
        r.append(par_node.val)
        res = None
        while l and r and l[-1] == r[-1]:
            res = l.pop()
            r.pop()
        
        return res
            
-----------------------------------------------------------------

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        graph = defaultdict(set)
        reverse = defaultdict(set)
        for region in regions:
            for i in range(1, len(region)):
                graph[region[i]].add(region[0])
                reverse[region[0]].add(region[i])
           
            
        visited1 = set()
        visited2 = set()
        
        def dfs(start, visit):
            stack = [start]
            while stack:
                node = stack.pop()
                visit.add(node)
                for child in graph[node]:
                    stack.append(child)
            return visit
        
        visited1 = dfs(region1, visited1)
        visited2 = dfs(region2, visited2)

        cand = set()
        for v in visited2:
            if v in visited1:
                cand.add(v)
                
        for c in cand:
            pass

        while reverse[c]:
            for rev in reverse[c]:
                if rev in cand and c != rev:
                 
                    c = rev
                    break
                else:
                    pass
            else:
                return c
        return c
      
        
            
      
