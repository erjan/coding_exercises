'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.
'''

def depthSumInverse(self, nestedList):
	"""
	:type nestedList: List[NestedInteger]
	:rtype: int
	"""
	self.max_h = 0
	res = []  # (depth, val)

	def dfs(node, depth):
		if not node:
			return
		self.max_h = max(self.max_h, depth)
		if not node.isInteger():
			n_d = depth+1
			for n_i in node.getList():
				dfs(n_i, n_d)
		else:
			res.append((depth, node.getInteger()))

	for node in nestedList:
		dfs(node, 0)
	w = 0
	for dep, val in res:
		w += (self.max_h-dep+1) * val
	return w
-------------------------------------------------

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total, cur_total = 0, 0
        queue = deque(nestedList)
        
        while queue:
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele.isInteger():
                    cur_total += ele.getInteger() # we dont clear current total, so every round previous depth total would be accumulated again and again.
                else:
                    queue.extend(ele.getList())      
            total += cur_total
                
        return total
      
---------------------------------------

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        stack = [(elem, 1) for elem in nestedList]
        maxdepth = 0
        abyss = collections.defaultdict(list)
        
        while stack:
            ni, depth = stack.pop()
            maxdepth = max(maxdepth, depth)
            if not ni.isInteger():
                for e in ni.getList():
                    stack.append((e, depth + 1) )
            else:
                abyss[depth].append(ni.getInteger())
                
        result = 0
        for depth in abyss:
            for num in abyss[depth]:
                result += (maxdepth - depth + 1) * num
                
        return result
---------------------------------------------------

def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def getDepth(element):
            if element.isInteger():
                return 1
            return 1+max([getDepth(e) for e in element.getList()], default=0)
                        
        def getDepthSum(element, depth):
            if element.isInteger():
                nonlocal maxDepth
                return (maxDepth-depth+1)*element.getInteger()
            return sum(getDepthSum(e, depth+1) for e in element.getList())
            
        maxDepth = max(getDepth(e) for e in nestedList)
        return sum(getDepthSum(e, 1) for e in nestedList)
-------------------------------------------

Easy approach, we take the values as they come and take the level sums, we also keep track of the total depth.

class Solution(object):
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
	    # Use a deque for our BFS. 
        q = collections.deque()
		# Append our initial list onto the q.
        q.append((0, nestedList))
		# We'll store the sum of vals using the recorded depth as keys.
        vl = collections.defaultdict(int)
		# We will keep track of the depth as we'll need this for our calculations but need to determine the depth.
        d = 0
        while q:
            l, lst = q.popleft()
			# Store the intermediate vals (these will be the sublists on the current level) in a list.
            itmlst = []
			# For val in our current list determine if a int or list.
            for i in lst:
                if i.isInteger():
                    vl[l] += i.getInteger()
                else:
                    # We need to make sure we get all sublist extended into our itermediate list to ensure we capture the correct level/depth.
                    itmlst.extend(i.getList())
			# If we have items to add back to the q, append them incrementing the level.
            if itmlst:
                q.append((l + 1, itmlst))
			# increment the overall depth, this level completed.
            d += 1
        # Now keep track of the final total.
        total = 0
		# For the levels and totals we found, the weight will be the (total depth - level val was found).
		# eg. [[1,1],2,[1,1]]: d = 2, k = 0, v = 2 -> (2 - 0) * (2) -> t = 4 ; d = 2, k = 1, v = 4 -> (2 - 1) * (1+1+1+1) -> t = 4 + 4 = 8
        for k, v in vl.items():
            total += (d - k) * v
            
        return total
We could also do the same thing, but instead of using the intermediate list just track the max depth observed and change our post processing a little bit:

class Solution(object):
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        q = collections.deque()
        q.append((0, nestedList))
        depth = 0
        levelvals = collections.defaultdict(int)
        while q:
            level, l = q.popleft()
            for i in l:
                if i.isInteger():
                    levelvals[level] += i.getInteger()
                else:
                    depth = max(depth, level + 1)
                    q.append((level + 1, i.getList()))
        total = 0
		# eg. [[1,1],2,[1,1]]: d = 1, k = 0, v = 2 -> (1 - (0-1)) * (2) -> t = 4 ; d = 1, k = 1, v = 4 -> (1 - (1-1)) * (1+1+1+1) -> t = 4 + 4 = 8
        for k, v in levelvals.items():
            total += (depth - (k-1)) * v
        return total
-------------------------------------------------------------------------------------------------------------------------      
      
      
      
