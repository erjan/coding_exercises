'''
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
'''


from collections import deque, defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        if n <= 1:
            return 0
        rst = 0
        childs = defaultdict(list)
        for idx, parent in enumerate(manager):
            childs[parent].append(idx)

        q = deque([(headID, informTime[headID])])
        while q:
            cur_id, cur_time = q.popleft()
            # calculate max
            rst = max(rst, cur_time)
            for child in childs[cur_id]:
                q.append((child, cur_time + informTime[child]))
        return rst
      
-----------------------------------------------------------------------------------------

class Solution:
	def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

		graph = defaultdict(list)
		for e,m in enumerate(manager):
			graph[m].append(e)

		q = [[headID,0]]
		res = 0
		while q:
			newq = []
			local = 0
			for m,t in q:
				res = max(res,t)
				for e in graph[m]:
					newq.append([e,t+informTime[m]])

			q = newq[::]

		return res
  
