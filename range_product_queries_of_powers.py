'''
Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.
'''

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        inp=bin(n).replace("0b", "")        
        pows, result = [] , []
        multiple, N = 1, len(inp)
        for i in range(N - 1, -1, -1):                        
            if i < N - 1:
                multiple *= 2            
            if inp[i] == '1':
                pows.append(multiple)                
        for s, e in queries:
            tmp = 1
            for i in range(s, e + 1):
                tmp *= pows[i]
            result.append( tmp % ((10 ** 9) +7 ))              
        return result
      
-----------------------------------------------------------------------

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

                                                        # Example: n = 46, queries = [[0,1],[2,2],[0,3]] 

        s = bin(n)[:1:-1]                               # <-- bin(46) = "0b101110" => bin(46)[:1:-1] = "011101"

                                
        powers = [i for i, ch in                        #              "0 1 1 1 0 1" 
                    enumerate(s) if ch == '1']          # <-- powers = [  1,2,3,  5]

        return [pow(2,sum(powers[a:b+1])                #       [ [0,  1],   [2,2]  ,   [0,          3]]
                    )%1000000007 for a,b in queries]    # <-- [2**(1 + 2), 2** 3   , 2**(1 + 2 + 3 + 5)] = [8, 8, 2048]
