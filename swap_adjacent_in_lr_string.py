'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
'''

def canTransform(self, start: str, end: str) -> bool:
        if start.count('X') != end.count('X'): 
            return False
        
        n = len(start)
        i = j = 0
        
        while i < n and j < n: 
            if start[i] == 'X': 
                i += 1
                continue
            if end[j] == 'X':
                j += 1
                continue
            
            if start[i] != end[j]: return False
            if start[i] == 'L' and i < j: return False
            if start[i] == 'R' and i > j:  return False
            
            i += 1
            j += 1
        
        return True
      
----------------------------------------------

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        count_R = count_L = 0
		
        for i in range(len(start)):
            if start[i] == 'R':
                if count_L > 0:
                    return False
                count_R += 1
            if end[i] == 'R':
                count_R -= 1
                if count_R < 0:
                    return False
            if end[i] == 'L':
                if count_R > 0:
                    return False
                count_L += 1
            if start[i] == 'L':
                count_L -= 1
                if count_L < 0: 
                    return False
        if count_R or count_L:
            return False
        return True
      
-------------------------------------------------------------

class Solution:
def canTransform(self, start: str, end: str) -> bool:

    so , eo , sind, eind = [],[],[],[]
    for i in range(len(start)):
        if start[i] != 'X':
            so.append(start[i])
            sind.append(i)
        if end[i] != 'X':
            eo.append(end[i])
            eind.append(i)
    if so != eo:
        return False
    
    for j in range(len(so)):
        if so[j] == 'L' and eind[j]>sind[j]:
            return False
        if so[j] == 'R' and eind[j]<sind[j]:
            return False
    
    return True
  
