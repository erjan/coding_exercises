'''
You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.
'''


Suggestions to make it better are always welcomed.

Think of it as a tree and now create a dictionary of ppid. Key is ppid and values are the list of its immediate children.
Now search through the dictionary in BFS fashion to get all the processes that will be killed.

def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
	mapping = collections.defaultdict(list)
	for i in range(len(ppid)):
		mapping[ppid[i]].append(pid[i])

	queue = [kill]
	result = []
	while queue:
		kill = queue.pop(0)
		result.append(kill)
		if kill in mapping:
			queue += mapping[kill]

	return result

----------------------------------------------

First, create a map from parent process to all of its children.
Then either do DFS as below, or BFS and find all the killed processes.

def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
	child_processes = defaultdict(list)
	for p, pp in zip(pid, ppid):
		child_processes[pp].append(p)

	def killp(p):
		procs = [p]
		for cp in child_processes[p]:
			procs += killp(cp)
		return procs

	return killp(kill)
----------------------------------------------------

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        childrenOf = {}
        
        for pos in range(len(pid)):
            
            # parent is key
            childrenOf.setdefault(ppid[pos], [])          
            childrenOf[ppid[pos]].append(pid[pos])
        

        killList = [kill]
        
        # root is kill
        if childrenOf[0] == killList:
            return pid
        
        res = []
        
        while killList:
            parent = killList.pop()
            res.append(parent)
            
            if parent in childrenOf:
                for child in childrenOf[parent]:
                    killList.append(child)

        return res
------------------------------------------------------

class Solution:
    def killProcess(self, pids: List[int], ppids: List[int], kill: int) -> List[int]:
        """
        find all the children of pid
        recursively kill them
        kill pid
        """
		# tree[pid] stores all the children of process pid
        tree = defaultdict(list)
        for i, ppid in enumerate(ppids):
            tree[ppid].append(pids[i])
        
        def killrec(pid):
            for child in tree[pid]:
                yield from killrec(child)
            yield pid
            
        return list(killrec(kill))
----------------------------------------------

def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        from collections import defaultdict as dd
        graph=dd(list)
        for i in range(len(pid)):
            graph[ppid[i]].append(pid[i])
        
        res=[kill]
        def dfs(node):
            if node not in graph:
                return 
            res.extend(graph[node])
            for child in graph[node]:
                dfs(child)
        dfs(kill)   
        return res
1)Create a directional graph with given pid and ppid.
2)Then perform DFS on that graph with starting node as kill node.
3)Keep appending child of graph to resultant list.
4)Return list optained as result.
-------------------------------------------------------

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        dic=defaultdict(list)
        for i in range(len(ppid)):
            dic[ppid[i]].append(pid[i])
        ans=[]
        def dfs(node,flag):
            if flag:
                ans.append(node)
            if node==kill:
                ans.append(node)
                for n in dic[node]:
                    dfs(n,True)
            else:
                for n in dic[node]:
                    dfs(n,flag)
        dfs(0,False)
        return ans

      
      
