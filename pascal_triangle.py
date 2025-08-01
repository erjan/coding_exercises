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

--------------------------------------------
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def generate_row(index: int) -> list[int]:
            factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000, 51090942171709440000, 1124000727777607680000, 25852016738884976640000, 620448401733239439360000, 15511210043330985984000000, 403291461126605635584000000, 10888869450418352160768000000, 304888344611713860501504000000, 8841761993739701954543616000000, 265252859812191058636308480000000, 8222838654177922817725562880000000, 263130836933693530167218012160000000, 8683317618811886495518194401280000000]

            def comb(n: int, r: int) -> int:
                return factorials[n] // (factorials[r] * factorials[n - r])

            row = []
            for i in range(index + 1):
                row.append(comb(index, i))
            return row

        result = []
        for i in range(numRows):
            result.append(generate_row(i))
        return result
---------------------------------

#my own another function 2025 1 aug

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        res = [[1],[1,1]]

        if numRows ==2:
            return res
        
        for i in range(3,numRows+1):
            prev = res[-1]
            cur = []
            
            cur.append(1)
            for j in range(len(prev)-1):
                 cur.append(prev[j] + prev[j+1])
            cur.append(1)

   

            res.append(cur)
        
        print(res)
        return res

