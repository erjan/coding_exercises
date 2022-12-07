	'''
  In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
'''
  
  class Solution:
    def help(self, edge, parent):
        # return True if no cycle is found, return False otherwise
        for i in edge:
            x, y = i
            p1 = x
            while p1 != parent[p1]:
                p1 = parent[p1]
            if p1 == y:
                return False
            else:
                parent[y] = x
        return True
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = 0
        for i in edges:
            x, y = i
            num_nodes = max(num_nodes, x, y)
        parent = [0] + [i + 1 for i in range(num_nodes)]
        #get number of nodes
        
        temp = []
        for i in edges:
            x, y = i
            if parent[y] != y:
                temp = [i, [parent[y], y]]
            else:
                parent[y] = x
        #pull out the node(two edges) that has two parents 
        parent = [0] + [i + 1 for i in range(num_nodes)]
        edge = [i for i in edges if i not in temp]
        
        if len(edge) == len(edges):# if all nodes has only one parents -> there must be cycles in the directed graph, return the edge that causes this cycle
            for i in edges:
                x, y = i
                p1 = x
                while p1 != parent[p1]:
                    p1 = parent[p1]
                if (p1 == y):
                    return i
                else:
                    parent[y] = x
        else:# if there is a node that has two parents, delete one edge per time and do union find twice to find which edge to delete.
            a, b = [temp[0]] + edge, [temp[1]] + edge
            q, w = self.help(a, parent.copy()), self.help(b, parent.copy())
            if q and w:
                return temp[0]
            elif q:
                return temp[1]
            else:
                return temp[0]
              
-----------------------------------------------------------------              
  
  """
    If you feel my approach can be improved, please let me know in the comments, I will be more than happy to know. 
	Also, if my complexity analysis is incorrect please put it in the comments. I am still in the learning phase and will be glad to polish myself. 
	I have commented this code heavily to make it more readable and 
	if I have to look back at this after a year, I should not be confused with regard to what has been done.
    """
    
    """
    What we have to do in this question???
    in the question, they have mentioned the presence of a rooted tree. Rooted trees are of two types- out tree and in tree.
    An out tree is a tree where all the edges point away from the root
    Now, Looking at the examples presented, I concluded we have to create an out-tree
    
    Now, remember, tree does not have any cycle. 
    Thus, we can conclude that we have to create a tree with the following Conditions
    1) All tree nodes are connected. Therefore, find the bridges and you MUST NOT remove the bridges
    2) If cycle exists, an edge has to be removed to break the cycle
    3) Make sure we create an out-tree. If 2 edges point to the same node, remove one of them  to obey the           concept of out-tree
    
    What are strongly onnected components?
    In a directed graph if a circle is formed then all the nodes in the given circle are said to be strongly connected. 
    When it is an undirected graph, we say connected but since here we have a directed graph, we're saying strongly connected.
    
    How to approach this question??
    Based on the above, we have decided cycles/bridges are to be found. 
	Now there exists an algorithm for  the same called Tarjan's algorithm to find strongly connected components. 
    Before I start this algorithm, it is necessary to make an adjacency list. I have created the same using a dicitonary.
	
    Step1: create a graph
    step2: use tarjans algorithm
    step 3: create a neat array (with proper mapping (u,v)) of strongly connected components
    step 4: create an array of edges disobeying the out root tree condition
    step 5: apply filtering to find the answer
    """
    
    #STEP 1
    #creation of a graph
    graph = {}
    for edge in edges:
        start = edge[0] -1
        end = edge[1] -1
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
        if end not in graph:
            graph[end] = []
    
    node_count = len(graph)
    
    #STEP 2A
    #Tarjan's algorithm 
    def tarjan(graph,node_count):
        id = [0]

        ids = [-1] * node_count
        low = [-1] * node_count 
        onStack = [False] * node_count 
        stack = []

        for i in range(node_count):
            if ids[i] == -1:
                dfsTarjan(i,stack,onStack,ids,low,id,graph)
        return low
    
    #STEP 2B
    #Tarjan's algorithm
    def dfsTarjan(at,stack,onStack,ids,low,id,graph):
        stack.append(at)
        onStack[at] = True
        ids[at] = low[at] = id[0]
        id[0]+=1 

        for to in graph[at]:
            if ids[to] == -1:
                dfsTarjan(to,stack,onStack,ids,low,id,graph)
            if onStack[to]: 
                low[at] = min(low[at], low[to])

        if ids[at] == low[at]:  
            while stack:
                node = stack.pop()
                onStack[node] = False
                low[node] = ids[at] 
                if node == at: break
    
    """
    getting the lowlink array using Tarjan's algorithm. 
	If 2 indices have the same value in a low lnk array, we can state with certainty that they are connected. 
    """
    lowLinkArray = tarjan(graph,node_count)
    edgesReversed = edges[::-1]
    #STEP3
    #We have a lowLink array but we need proper mapping of edges that form strongly connected components/
    stronglyConnected = []
    for edge in edgesReversed:
        start = edge[0]-1
        end = edge[1]-1
        if lowLinkArray[start] == lowLinkArray[end]:
            stronglyConnected.append(edge)
    #At this point the list named stronglyConnected has a list of all components that form the cycle
    
    #STEP 4A
    #Finding the edges that do not obey the condition of outrooted tree
    """   
    We have created a dictionary called OutRootedDisobey. The values are the nodes that point towards the key. 
	If we have more than one value pointing to the same node, clearly there is a problem and we have  found the edge that we want to remove.
    """ 
    OutRootedDisobey = {}
    for edge in edges:
        start = edge[1]
        end = edge[0]
        if start not in OutRootedDisobey:
            OutRootedDisobey[start] = [end]
        else:
            OutRootedDisobey[start].append(end)
    
    #STEP 4B
    #We need a clear mapping in the form of (u,v) for the edges disbobeying the outroot condition
    #iterate over the dictionary and if the length of values is greater than 1 then create a mapping         
    notOutRoot = []
    for key,values in OutRootedDisobey.items():
        if len(values)>1:
            for value in values:
                notOutRoot.append([value,key])
    
    #this section ensures we send the proper edge.
    """
    
    At this point we know which edges do not obey outRoot (present in notOutRoot)
    At this point we also know the edges that are a part of a cycle (present in stronglyConnected)
    
    we want to start iterating from the last element because the question asks for the one edge that occurs first if we start from the last.
	While iterating check for the following 3 points.
    
    1) If an edge exists in a cycle and also does not obey the out rooted tree condition, that's the edge to be hunted first!
    2) If we are lucky to find all edges obeying the out root tree condition but the edge is a part of some cycle, remove that particular edge. 
    
    (here, there might be more than one edges that can be removed but the question clearly asks you to remove the one that occurs at the last)
    3) Lastly, if we are lucky to not find any cycle but we find an edge disobeying the outRoot tree condition, remove it
    """
    
    #STEP 5
    for edge in edgesReversed:
        if edge in stronglyConnected and edge in notOutRoot:
            return edge
        elif edge in stronglyConnected and len(notOutRoot) == 0:
            return edge
        elif edge in notOutRoot and len(stronglyConnected) == 0:
            return edge
        
        
    """
    Complexity analysis
    V = total vertices
    E = Total edges
    Time:
    
    Step 1: O(E)
    step 2: O(V+E)
    step 3: O(E)
    step 4: OutRootedDisobey = O(E)
            NotOutRoot = O(E) #not sure about this
    step 5: O(E)
    Edge reversal: O(E)
    
    NET time: O(E) + O(V+E) + O(E) + O(E) + O(E) + O(E) + O(E) = O(V+E)
    ----------------------------------------------------------
    Space:
    Step 1: O(E)
    step 2: O(V)
    step 3: O(E) in worst case the entire graph is connected
    step 4: OutRootedDisobey = O(1)
            AND for NotOutRoot, at the most one edge wont obey the condition so O(1)
    step 5: O(1)
    Edge reversal: O(E)
    
    NET SPACE: (E) + O(V) + O(E) + O(E) = O(V+E)      
    """
