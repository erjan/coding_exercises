'''
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
'''

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        query_results = {}
        heap = []
        
        i = 0
        for q in sorted(queries):
            query_results[q] = -1
            # populate heap with (size, end) so we can get the smallest valid interval for the query 
            while i < len(intervals) and q >= intervals[i][0]:
                start, end = intervals[i]
                heapq.heappush(heap, (1 + end - start, end))    
                i += 1
            # clean up heap by popping invalid results. Any results not valid now will not be valid for
            # any future queries, since we are looping through the queries in ascending order. 
            while heap and q > heap[0][1]:
                heapq.heappop(heap)
            # After cleanup, the front of the heap is guarnteed to be the smallest sized interval 
            # that is valid for the given query. 
            if heap:
                query_results[q] = heap[0][0]
        
        # we must return the query results in the same order we got them
        return [query_results[q] for q in queries]
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
	def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
		hashMap = {}
		intervals.sort()

		minHeap = []

		i_l = len(intervals)
		i = 0
		for q in sorted(queries):
			while i < i_l and intervals[i][0] <= q:
				start, end = intervals[i]
				heapq.heappush(minHeap, [(end-start+1), end])
				i += 1

			while minHeap and minHeap[0][1] < q:
				heapq.heappop(minHeap)

			hashMap[q] = minHeap[0][0] if minHeap else -1

		return [hashMap[q] for q in queries]
	
-------------------------------------------------------------------------------------------
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [-1] * len(queries)
        intervals.sort(key = lambda i: i[1] - i[0])
        queries = sorted([q, i] for i, q in enumerate(queries))
        for left, right in intervals:
            idx = bisect.bisect(queries, [left])
            while idx < len(queries) and queries[idx][0] <= right:
                ans[queries.pop(idx)[1]] = right - left + 1
        return ans
	
---------------------------------------------------------------------------------------------------------

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i:i[0])
        result = {}
        heap = []
        i = 0
        for q in sorted(queries):
            # add the intervals into heap for the given query
            while i < len(intervals) and intervals[i][0] <= q:
                interval_start,interval_end = intervals[i] 
                heapq.heappush(heap,(interval_end-interval_start+1,interval_end))
                i+=1
            # pop out the invalid intervals from the heap against which the given query will not overlap the interval
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            # after the while loop ends we will at all potential intervals that satisfy the query
            # take the min if heap in not null otherwise -1
            min_val = heap[0][0] if heap else -1
            result[q] = min_val
        return [result[q] for q in queries]
