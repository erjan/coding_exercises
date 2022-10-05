'''
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s 
consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the
substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in 
the substring. A plate is considered between candles if there is at least one candle to its left and at least 
one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates 
between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.
'''

class Solution:
  def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
      n = len(s)
      res = [0] * len(queries)
      prefix_sum = [0] * n
      candles_left = [-1] * n
      candles_right = [-1] * n

      prefix_sum[0] = 1 if s[0] == '*' else 0
      candles_left[0] = 0 if s[0] == '|' else -1
      candles_right[n - 1] = n - 1 if s[n - 1] == '|' else n

      for i in range(1, n):
          prefix_sum[i] = prefix_sum[i - 1] + (1 if s[i] == '*' else 0)
          candles_left[i] = i if s[i] == '|' else candles_left[i - 1] 

      for i in range(n - 2, -1, -1):
          candles_right[i] = i if s[i] == '|' else candles_right[i + 1]

      for i in range(len(queries)):

          start = candles_right[queries[i][0]]
          end = candles_left[queries[i][1]]

          res[i] = prefix_sum[end] - prefix_sum[start] if start < end else 0

      return res
------------------------------------------------------------------------------------------------------
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        #brute force
        n = len(s)
        candles = []
        out = []
        for i in range(n):
            if s[i]=='|':
                candles.append(i)    
        
        def just_smaller_than(candles,i):
            l,r = 0,len(candles)-1
            while l<=r:
                m = (l+r)//2
                if candles[m]==i:
                    return m
                elif candles[m]>i:
                    r=m-1
                else:
                    l=m+1
            return r
        
        def just_larger_than(candles,i):
            l,r = 0,len(candles)-1
            while l<=r:
                m = (l+r)//2
                if candles[m]==i:
                    return m
                elif candles[m]>i:
                    r=m-1
                else:
                    l=m+1
            return l
        
        for s,e in queries:
            #find the index of the first candle of the given interval, in the candles array
            firstIndx = just_larger_than(candles,s)
            
            #find the index of the last candle of the given interval, in the candles array
            lastIndx = just_smaller_than(candles,e)
            
            #if no candles in the given interval 
            if firstIndx>=len(candles) or candles[lastIndx]>e or candles[firstIndx]<s:
                out.append(0)
                continue

            #number of candles
            num_candles = lastIndx-firstIndx-1 
            # print("num candles in range",num_candles)
            
            #number of items between first and last candle - this interval would contain both plates and candles
            items = candles[lastIndx]-candles[firstIndx]-1
            
            #Remove the candles from the above interval to get the plates
            num_plates = max(0,items-num_candles)
            out.append(num_plates)
        
        return out
    
