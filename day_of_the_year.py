'''
Given a string date representing a Gregorian calendar
date formatted as YYYY-MM-DD, return the day number of the year.
'''


from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        res = datetime.strptime(date, '%Y-%m-%d')
        return res.timetuple().tm_yday
