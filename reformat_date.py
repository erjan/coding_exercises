'''
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
'''

#my own solution

class Solution:
    def reformatDate(self, date: str) -> str:
            s = date.split()

            day = s[0]
            day_num = ''

            for i in range(len(day)):
                if day[i].isnumeric():
                    day_num += day[i]

            day_num = str(day_num)
            print(day_num)

            if int(day_num) < 10:
                day_num = '0' + str(day_num)

            month = s[1]

            month_d = ["Jan", "Feb", "Mar", "Apr", "May",
                       "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month_index = month_d.index(month)+1
            if month_index < 10:
                month_index = '0' + str(month_index)
            print(month_index)

            year = s[2]
            res = ''

            res += year + '-' + str(month_index) + '-' + day_num
            print(res)
            return res

#another better from discussions
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        d = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        if int(date[-3][:-2]) < 10:
            date[-3] = "0"+date[-3]
        return date[-1]+"-"+d[date[-2]]+"-"+date[-3][:-2]
