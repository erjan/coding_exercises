#Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(self,d):

            res = []
            for i in range(len(d)-1):
                temp = d[i] + d[i+1]
                res.append(temp)
            res.insert(0,1)
            res.insert( len(res),1)
            return res
        
        res = []
        res.append([1])
        
        if numRows == 0:
            return []
        
        for i in range(1,numRows):
            prev = res[i-1]
            temp = helper(self,prev)
            res.append(temp)
        return res
    
#ONE FUNCTION
  
def generate(numRows):
    res = []
    res.append([1]) 
    if numRows == 0:
        return []
        
    for i in range(1,numRows):
        prev = res[i-1]
     
        t = []
        for i in range(len(prev)-1):
            temp = prev[i] + prev[i+1]
            t.append(temp)
        t.insert(0,1)
        t.insert( len(t),1)

        res.append(t)
    print(res)
    return res
