'''
Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.
'''

class Solution: 
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # create an empty list to hold result
        result = []
        
        # create the permutation
        mList = [x for x in range(1, m + 1)]
        
        # iterate over each element from queries
        for x in queries:
            # append the index of query value from the permutation
            result.append(mList.index(x))
            # remove the element from the permutataion
            mList.remove(x)
            # add the query element in the begining of the permutation
            mList.insert(0, x)
        
        # return the stored index result of queries
        return result
      
------------------------------------------------------------------------------
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1,m + 1))
        def moveToStart(p,queryIndex):
            return p[queryIndex:queryIndex+1] + p[:queryIndex] + p[queryIndex+1:]
        answer = [0] * len(queries)
        i = 0
        for query in queries:
            queryIndex = p.index(query)
            p = moveToStart(p,queryIndex)
            answer[i] = queryIndex
            i += 1
        return answer    
