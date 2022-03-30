
'''
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents 
one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents 
the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing 
it by 5 using integer division.
'''


import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
            res = defaultdict(list)
            s = items
            for i in range(len(s)):
                item = s[i]

                id = item[0]
                score = item[1]

                res[id].append(score)

            for k in res.keys():
                heapq.heapify(res[k])
                temp = heapq.nlargest(5, res[k])
                res[k] = sum(temp)//5

            res = [[k, v] for k, v in res.items()]
            res.sort(key=lambda x: x[0])
            print(res)
            return res
          
#another solution - using insort
def highFive(self, items: List[List[int]]) -> List[List[int]]:
        D = collections.defaultdict(list)
        for student, score in items:
            bisect.insort(D[student], score) # insert in a list in increasing order.
        return [[student, sum(D[student][-5:])//5] for student in D]
      
      
#another

import heapq
from collections import defaultdict
def highFive(self, items: List[List[int]]) -> List[List[int]]:
	cache = defaultdict(list)  # {student_id: [top-5 scores]}
	
	for student_id, score in items:
		if len(cache[student_id]) < 5:  # make sure the size of heap for each student does not exceed 5.
			heapq.heappush(cache[student_id], score)
		else:
			heapq.heappushpop(cache[student_id], score)

	ans = []
	for student_id, scores in cache.items():
		average = sum(scores) // len(scores)
		ans.append((student_id, average))

	return ans
