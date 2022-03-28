#Given a year year and a month month, return the number of days of that month.

'''
The algorithm to determine leap year is below:

if (year is divisible by 4) and (year is not divisible by 100) then (it is a leap year);
if (year is divisible by 400) then (it is a leap year).
'''


from calendar import monthrange

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        
        
        return monthrange(year, month)[1]
      
      
      
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in {1,3,5,7,8,10,12}: return 31
        elif M != 2: return 30
        else: return 28 + (Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0)      
