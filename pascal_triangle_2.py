'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
'''

class Solution:
    
    def getRow(self, rowIndex: int) -> List[int]:
        
        def generate_helper(self,numRows):
            res = []
            res.append([1]) 
            if numRows == 0:
                return []

            for i in range(1,numRows+1):
                prev = res[i-1]

                t = []
                for i in range(len(prev)-1):
                    temp = prev[i] + prev[i+1]
                    t.append(temp)
                t.insert(0,1)
                t.insert( len(t),1)

                res.append(t)
            return res
        
        k = rowIndex
        if k <=33:
            if k == 0:
                return [1]
            
            result = generate_helper(self,k)
            return result[k]
            
