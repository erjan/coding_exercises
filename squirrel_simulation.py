'''
You are given two integers height and width representing a garden of size height x width. You are also given:

an array tree where tree = [treer, treec] is the position of the tree in the garden,
an array squirrel where squirrel = [squirrelr, squirrelc] is the position of the squirrel in the garden,
and an array nuts where nuts[i] = [nutir, nutic] is the position of the ith nut in the garden.
The squirrel can only take at most one nut at one time and can move in four directions: up, down, left, and right, to the adjacent cell.

Return the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one.

The distance is the number of moves.
'''

Algo
Since the squirrel needs to move nuts to the tree, the answer will be mostly sum(|nuts[i] - tree| for i in range(len(nuts))) with one exception as the squirrel initially moves to that nut. It is critical to properly choose this nuts to minimize the distance traveled by the squirrel.

Apparently, the nut which minimizes the difference of its distance to squirrel and its distance to tree should be chosen.

Implementation

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        ans, mn = 0, inf
        for x, y in nuts: 
            ans += 2*(abs(tree[0]-x) + abs(tree[1]-y))
            mn = min(mn, abs(squirrel[0]-x) + abs(squirrel[1]-y) - abs(tree[0]-x) - abs(tree[1]-y))
        return ans + mn
Analysis
Time complexity O(N)
Space complexity O(1)

------------------------------------------------------------------------

Might seem hard until you understand the problem, the constraint of having to go to the tree after picking up EVERY nut makes it a medium problem. The squirrel only needs to pick the first nut which would result in most savings.

def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

	max_saving = -inf
	sqx, sqy = squirrel 
	tx, ty = tree
	total_cost = 0
	for i, (x, y) in enumerate(nuts):
		nut_to_sqr = abs(x - sqx) + abs(y - sqy)
		nut_to_tree = abs(x - tx) + abs(y - ty)
		total_cost += nut_to_tree * 2
		saving = nut_to_tree - nut_to_sqr
		max_saving = max(max_saving, saving)

	return total_cost - max_saving

----------------------------------------------------------------

First Assume that Squirrel is at the Tree. So whats the total distance?

It will be twice the distance from each nut to Tree.
(path to pick it then travel back the same path)

For each nut:
total+= dist_to_nut*2

Now putting Squirrel into the scenario where it is somewhere else:-

So, there will be one nut the squirrel will travel to first and take it to the tree

As we added every distance twice, now we need to subtract it (first_nut_dist) once from the total and also add the distance travelled by squirrel to it
Now,

total = total - distance_of_first_nut_to_tree + squirrel_dist_to_first_nut

taking the negative sign outside

total = total - (distance_of_first_nut_to_tree - squirrel_dist_to_first_nut)

To get the minimum total distance, we have to maximize the bold value above.

Meaning, selecting that first nut among all the nuts which has the MAX value of (distance_of_nut_to_tree - squirrel_dist_to_that_nut)

def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        

        firstPath = float('-inf')
        
        total_dist = 0
        
        for nut in nuts:
            
            dist_to_Sq = abs(squirrel[0]-nut[0])+abs(squirrel[1]-nut[1])
            dist_to_Tr = abs(tree[0]-nut[0])+abs(tree[1]-nut[1])
                        
            if (dist_to_Tr-dist_to_Sq)>firstPath:
                firstPath = dist_to_Tr-dist_to_Sq        #finding the Max firstPath as this value 
                                                         # will be subtracted from total
            total_dist+=2*dist_to_Tr
            
        
        total_dist = total_dist - firstPath
        
        return total_dist
      
-------------------------------------------------------------------

First let's simplify the problem statement: "Which nut should the squirrel grab first?"

No matter what, because the squirrel can only carry one nut at a time, the squirrels path will look like this:

(a) Distance squirrel travels from it's start position to the first nut.
(b) 1 times the distance from the first nut to the tree
(c) 2 times the distance from all the other nuts to the tree

This is because for every nut besides the first one, the squirrel must start at the tree, go to the nut, and return to the tree.

That said, for each nut, we calculate (a), (b), and (c) and return the minimum (a) + (b) + (c).

def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

	def manhattan(a,b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	res = float('inf')
	dist = [manhattan(n, tree) for n in nuts] # Distance from each nut to the tree
	total = sum(dist)
	all_except = [total-d for d in dist]      # Sum of distance to tree for all nuts except for nuts[i] (the starting nut)
	
	# Try choosing each nut as the "starting nut" and calculate the total distance
	for i in range(len(nuts)):
		a = manhattan(squirrel, nuts[i])
		b = dist[i]
		c = 2*all_except[i]
		res = min(res, a+b+c)

	return res
---------------------------------------------------------------------------------

First Assume that Squirrel is at the Tree. So whats the total distance?

It will be twice the distance from each nut to Tree.
(path to pick it then travel back the same path)

For each nut:
total+= dist_to_nut*2

Now putting Squirrel into the scenario where it is somewhere else:-

So, there will be one nut the squirrel will travel to first and take it to the tree

As we added every distance twice, now we need to subtract it (first_nut_dist) once from the total and also add the distance travelled by squirrel to it
Now,

total = total - distance_of_first_nut_to_tree + squirrel_dist_to_first_nut

taking the negative sign outside

total = total - (distance_of_first_nut_to_tree - squirrel_dist_to_first_nut)

To get the minimum total distance, we have to maximize the bold value above.

Meaning, selecting that first nut among all the nuts which has the MAX value of (distance_of_nut_to_tree - squirrel_dist_to_that_nut)

def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        

        firstPath = float('-inf')
        
        total_dist = 0
        
        for nut in nuts:
            
            dist_to_Sq = abs(squirrel[0]-nut[0])+abs(squirrel[1]-nut[1])
            dist_to_Tr = abs(tree[0]-nut[0])+abs(tree[1]-nut[1])
                        
            if (dist_to_Tr-dist_to_Sq)>firstPath:
                firstPath = dist_to_Tr-dist_to_Sq        #finding the Max firstPath as this value 
                                                         # will be subtracted from total
            total_dist+=2*dist_to_Tr
            
        
        total_dist = total_dist - firstPath
        
        return total_dist
-------------------------------------------------------------------

'''
w: hashmap, greedy
h: some observations (| | mean the manhattan distance):
    1) there is only one nut A that has the distance of |squirrel - nut A| + |tree - nut A|
    2) for other nuts, the distance is 2|tree-nut|
    3) what we basically need to find is the nut A s.t.  |tree - nut A| - |squirrel - nut A| is maximized
'''
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        dic1 = {}
        dic2 = {}
        i = 0
        j = -float('inf')
        for idx, nut in enumerate(nuts):
            dic1[idx] = 2 * self.calDistance(nut, tree)
            dic2[idx] =  self.calDistance(nut, squirrel)
            if dic1[idx] // 2 - dic2[idx] > j:
                i = idx
                j = dic1[idx] // 2 - dic2[idx]
                                
        return sum(dic1.values()) - j
    
    def calDistance(self, pt1, pt2):
        return abs(pt1[0]-pt2[0])+abs(pt1[1]-pt2[1])
------------------------------------------------------

Imaging the squirrel is starting at tree position, no matter which nuts to get first, the total distance will be 2 * tree to each nut, which is 'sum' in my code.
Now we need to get the max distance difference between the squirrel to one of the nuts, and that nuts to the tree, where max = Tree_dis - squirrel dis, and total distance = sum - (Tree_dis - squirrel_dis) = sum - Tree_dis + squirrel_dis.

So the important part is to find the max distance difference between the squirrel to one of the nuts, and that nuts to the tree. Height and width are not useful here.

"""

def minDistance(self, height, width, tree, squirrel, nuts):
maxs = 0
sums = 0
for nut in nuts:
trees = abs(tree[0]-nut[0]) + abs(tree[1]-nut[1])
sums += 2*trees
dis = abs(squirrel[0]-nut[0]) + abs(squirrel[1]-nut[1])
if trees - dis > maxs:
maxs = trees - dis
return sums - maxs if maxs else sums + abs(trees-dis)
"""

      
      
