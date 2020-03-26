class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def helper(self,matrix,col):
            res = []
            for i in range(len(matrix)):
                res.extend(matrix[i])
            last = res[-1]
            res = res[:-1]
            res.insert(0, last)
            return chunks(self,res,col)

        def chunks(self,l,size):
            res = []
            for i in range(0,len(l),size):
                res.extend([l[i:i+size]])
            return res
        
        m = grid
        col = len(m[0])
        for i in range(k):
            m = helper(self,m,col)
            
        print(m)
        return m
    
        
