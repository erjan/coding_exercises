'''
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.
'''


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        cur_time = 0
        res = []

        for duration,lastday in courses:
            heappush(res,-duration)
            cur_time += duration
            if cur_time > lastday:
                longest_duration_course_taken = -heappop(res)
                cur_time -= longest_duration_course_taken

        return len(res)
                
-----------------------------------------------------------------------------------------------------
