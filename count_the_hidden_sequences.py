    def numberOfArrays(self, diff, lower, upper):
        A = list(accumulate(diff, initial = 0))
        return max(0, (upper - lower) - (max(A) - min(A)) + 1)
      
-------------------------------------------------------------------------------------------------

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        l = [0]
        for i in differences:
            l.append(l[-1]+i)
        return max(0,(upper-lower+1)-(max(l)-min(l)))

-----------------------------------------------------------------------------------------------------------------------    
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        t = [0]       
        
        for d in differences:            
            t.append(t[-1] + d)            
            
        minh = min(t)
        maxh = max(t)
        rang = maxh - minh
        
        return max(0,(upper-lower+1) - rang)
        
                
