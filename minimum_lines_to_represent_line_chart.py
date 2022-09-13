'''
You are given a 2D integer array stockPrices
where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A 
line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:
'''


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        # key point: never use devision to judge whether 3 points are on a same line or not, use the multiplication instead !!
        
        n = len(stockPrices)
        stockPrices.sort(key = lambda x: (x[0], x[1]))
        
        if n == 1:
            return 0
        
        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        num = 1
        
        for i in range(1, n-1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i+1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i+1][0]
            
            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                num += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y
        
        return num
      
--------------------------------------------------------------------
def minimumLines(self, A: List[List[int]]) -> int:
        n = len(A)
        res = n - 1
        A.sort()
        for i in range(1, n - 1):
            a, b, c = A[i-1], A[i], A[i+1]
            if (b[0] - a[0]) * (c[1] - b[1]) == (c[0] - b[0]) * (b[1] - a[1]):
                res -= 1
        return res
