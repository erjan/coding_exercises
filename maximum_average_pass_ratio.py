'''
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

'''

import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # Organize the heap based on the "ratio improvement factor"
        # i.e. The (new ratio) - (old ratio), the one that will improve the largest should be the one added to
        # Add a negative since all heaps are minimum-oriented in python
        classes = [[-((p+1)/(t+1) - (p/t)), p, t] for p, t in classes]
        heapq.heapify(classes)
        
        # Go through the amount of students we need to add
        for _ in range(extraStudents):
            # Remove the next largest opportunity
            c = heapq.heappop(classes)
            
            # Change all of the values
            c[1] += 1
            c[2] += 1
            # Update ratio factor
            c[0] = -((c[1]+1)/(c[2]+1) - (c[1]/c[2]))
            # Push this back on to the heap
            heapq.heappush(classes, c)
            
        # Calculate the total pass ratio after doing this
        total_ratio = 0
        n = 0
        for c in sorted(classes):
            n += 1
            total_ratio += (c[1] / c[2])
            
        return total_ratio / n
      
-------------------------------------------------------------------------------------------

class Solution:
	def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
		
		n = len(classes)
		
		impacts = [0]*n
		minRatioIndex = 0
		
		# calculate and store impacts for each class in form of tuples -> (-impactValue, passCount, totalCount)
		for i in range(n):
			passCount = classes[i][0]
			totalCount = classes[i][1]
			
			# calculate the impact  for class i
			currentRatio = passCount/totalCount
			expectedRatioAfterUpdate = (passCount+1)/(totalCount+1)
			impact = expectedRatioAfterUpdate - currentRatio
			
			impacts[i] = (-impact, passCount, totalCount)  # note the - sign for impact
			
		heapq.heapify(impacts)
		
		while(extraStudents > 0):
			# pick the next class with greatest impact 
			_, passCount, totalCount = heapq.heappop(impacts)
			
			# assign a student to the class
			passCount+=1
			totalCount+=1
			
			# calculate the updated impact  for current class
			currentRatio = passCount/totalCount
			expectedRatioAfterUpdate = (passCount+1)/(totalCount+1)
			impact = expectedRatioAfterUpdate - currentRatio
			
			# insert updated impact back into the heap
			heapq.heappush(impacts, (-impact, passCount, totalCount))
			extraStudents -= 1
		
		result = 0
			
		# for all the updated classes calculate the total passRatio 
		for _, passCount, totalCount in impacts:
			result += passCount/totalCount
			
		# return the average pass ratio
		return result/n
