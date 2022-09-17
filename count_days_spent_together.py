'''
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
'''



class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        monthdays = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        start, end = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        
        start_month, start_day = int(start[:2]), int(start[3:])
        end_month, end_day = int(end[:2]), int(end[3:])
        
        if start > end: return 0
        elif start_month == end_month: 
            return end_day - start_day + 1
        else: 
            return (monthdays[start_month] - start_day) + sum([monthdays[i] for i in range(start_month + 1, end_month)]) + end_day + 1
