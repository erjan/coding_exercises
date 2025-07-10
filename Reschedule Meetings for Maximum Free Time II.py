'''
You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.

Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

 '''
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        size = len(startTime)
        gapsArr,left = [],0
        for i in range(size):
            gap = startTime[i] - left
            gapsArr.append(gap)
            left = endTime[i]
        gapsArr.append(eventTime - endTime[-1])
        maxGapPrefix,maxGapSuffix = [0 for i in range(size)],[0 for i in range(size)]
        maxGapPrefix[0] = gapsArr[0]
        maxGapSuffix[size-1] = gapsArr[-1]

        # calculate left right max
        for i in range(1,size):
            maxGapPrefix[i]= max(maxGapPrefix[i-1],gapsArr[i])
        for i in range(size-1,0,-1):
            maxGapSuffix[i-1]= max(maxGapSuffix[i],gapsArr[i])
        
        ans = 0
        for i in range(size):
            curr = gapsArr[i]+gapsArr[i+1]
            barSize = endTime[i] - startTime[i]
            isValid = False
            if(i-1 >= 0):
                isValid = isValid or maxGapPrefix[i-1] >= barSize
            if(i+1 < size):
                isValid = isValid or maxGapSuffix[i+1] >= barSize
            if(isValid):
                curr += barSize
            ans = max(ans, curr)
        return ans
            

