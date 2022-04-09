'''

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        lst = list(time.replace(":", ""))
        lst.sort()
                
        min_num = min(lst)

        #seconds
        for i in lst:
            if i > time[4]:
                return time[:4] + i
            
        #tens of seconds
        for i in lst:
            if i > time[3] and i < "6":
                return time[:3] + i + min_num
        
        #hours
        for i in lst:
            if i > time[1]:
                if time[0] != "2" or i < "4": 
                    return f"{time[0]}{i}:{min_num}{min_num}"

        #tens of hours            
        for i in lst:
            if i > time[0]:
                if i == "1" or i == "2" and min_num < "4":
                    return f"{i}{min_num}:{min_num}{min_num}"
                
        return f"{min_num}{min_num}:{min_num}{min_num}"
        
-------------------------------------------

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [int(t) for t in time if t != ":"]
        sortedDigits = sorted(digits)
        nextDigits = { sortedDigits[-1]: -1 }
        for i in range(len(sortedDigits) - 1):
            nextDigits[sortedDigits[i]] = sortedDigits[i+1]
        
        i = 3            
        while i >= 0:
            d = digits[i]
            if d < nextDigits[d]:
                nd = nextDigits[d]
                if i == 3:
                    break
                if i == 2 and nd < 6:
                    break             
                if i == 1 and digits[i-1] * 10 + nd < 24:
                    break                    
                if i == 0 and nd * 10 + digits[i+1] < 24:
                    break
            
            i -= 1
        
        if i >= 0:
            digits[i] = nextDigits[digits[i]]
       
        while i + 1 < 4:
            digits[i+1] = sortedDigits[0]
            i += 1
        
        res = list(map(str, digits))
        
        return "".join(res[:2]) + ":" + "".join(res[2:])
