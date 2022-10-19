'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
'''

class Solution:
    def findMinDifference(self, t: List[str]) -> int:
        tab=[]
        for i in t:
            tab.append(int(i[0:2])*60+int(i[3:]))
        tab.sort()
        n=len(tab)
        res=1440+tab[0]-tab[n-1]
        for i in range(1,n):
            res=min(res,(tab[i]-tab[i-1]))
        return res 
      
----------------------------------------------------------------------------------------
class Solution:
	def findMinDifference(self, timePoints: List[str]) -> int:
		timePoints.sort()

		def getTimeDiff(timeString1, timeString2):
			time1 = int(timeString1[:2]) * 60 + int(timeString1[3:])
			time2 = int(timeString2[:2]) * 60 + int(timeString2[3:])

			minDiff = abs(time1 - time2)

			return min(minDiff, 1440 - minDiff)

		result = getTimeDiff(timePoints[0], timePoints[-1]) # edge case, we need to check minDiff of first and last time after sorting

		for i in range(len(timePoints)-1):
			curMin = getTimeDiff(timePoints[i], timePoints[i+1])

			if curMin < result:
				result = curMin

		return result
---------------------------------------------------------------------------------------------------
from math import inf
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, timePoint in enumerate(timePoints):
            #Change each timepoint to an integer representation of the number of minutes since midnight.
            hours, mins = timePoint.split(':')
            timeInMins = int(hours) * 60 + int(mins)
            timePoints[i] = timeInMins
            
        timePoints.sort()
        smallestDiff = inf
        
        #Compare contiguous pairs and update smallest time difference if necessary.
        for i in range(1, len(timePoints)):
            smallestDiff = min(smallestDiff, timePoints[i] - timePoints[i - 1])
            
        #Special case: smallest difference may occur between largest time and smallest time by wrapping around past midnight.
        smallestDiff = min(smallestDiff, 60 * 24 - timePoints[-1] + timePoints[0])
        
        return smallestDiff
      
----------------------------------------------------------------------------------------      
