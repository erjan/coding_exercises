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
